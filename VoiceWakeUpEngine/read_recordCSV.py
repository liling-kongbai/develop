import os
import csv
import torchaudio
import torch
from torch.utils.data import Dataset, DataLoader

from torch import nn
from torch.nn import functional as F

device = torch.device('cuda' if torch.cuda.is_available() else 'cpu')

project_path = os.path.dirname(os.path.abspath(__file__))



def readCSV(path):
    file_path = os.path.join(project_path, path)

    data = []

    with open(file_path, mode='r', encoding='utf-8') as file:
        csv_reader = csv.reader(file)
        for row in csv_reader:
            data.extend(row)
    print(data)
    return data



class audio_Dataset(Dataset):
    def __init__(self, data, labels, train, transform=None):
        if train:
            self.data = [os.path.join(project_path, 'dataset\\train', i + '_' + j + '.wav') for i, j in zip(data, labels)]
        else:
            self.data = [os.path.join(project_path, 'dataset\\test', i + '_' + j + '.wav') for i, j in zip(data, labels)]
        self.labels = labels
        self.transform = transform

    def __len__(self):
        return len(self.data)

    def __getitem__(self, idx):
        sample_data = self.data[idx]
        sample_label = self.labels[idx]
        waveform, _ = torchaudio.load(sample_data)
        if self.transform:
            waveform = self.transform(waveform)
        return waveform, torch.tensor(int(sample_label), dtype=torch.uint8)




# 预加重：一阶高通滤波器
class FirstOrderHighPassFilter:
    def __init__(self, mu):
        self.mu = mu
        self.buffer = None

    def __call__(self, input_signal):
        if self.buffer is None:
            self.buffer = torch.zeros_like(input_signal)
        output_signal = (1 - self.mu) * (input_signal - self.buffer)
        self.buffer = input_signal
        return output_signal


class SpectrogramTransform:
    def __init__(self, n_fft=1024, hop_length=512, win_length=1024, window_fn=torch.hamming_window, power=2):
        self.spectrogram = torchaudio.transforms.Spectrogram(
            n_fft=n_fft,
            hop_length=hop_length,
            win_length=win_length,
            window_fn=window_fn,
            power=power
        )

    def __call__(self, waveform):
        return self.spectrogram(waveform)



class CombinedTransform:
    def __init__(self, high_pass_filter, spectrogram_transform):
        self.high_pass_filter = high_pass_filter
        self.spectrogram_transform = spectrogram_transform

    def __call__(self, waveform):
        filtered_waveform = self.high_pass_filter(waveform)
        spectrogram = self.spectrogram_transform(filtered_waveform)
        return spectrogram

mu = 0.9
n_fft = 1024
hop_length = 512
win_length = 1024
window_fn = torch.hamming_window
power = 2

# 创建转换实例
high_pass_filter = FirstOrderHighPassFilter(mu)
spectrogram_transform = SpectrogramTransform(n_fft, hop_length, win_length, window_fn, power)
combined_transform = CombinedTransform(high_pass_filter, spectrogram_transform)


train_dataset = audio_Dataset(readCSV('train_dataset_feature_csv.csv'), readCSV('train_dataset_label_csv.csv'),
                              train=True,
                              transform=combined_transform)
test_dataset = audio_Dataset(readCSV('test_dataset_feature_csv.csv'), readCSV('test_dataset_label_csv.csv'),
                             train=False,
                             transform=combined_transform)



train_dataloader = DataLoader(train_dataset, batch_size=2, shuffle=True)
test_dataloader = DataLoader(test_dataset, batch_size=2, shuffle=True)



for batch_idx, (data, label) in enumerate(train_dataloader):
    print(f"Batch {batch_idx + 1}:")
    for idx, (single_data, single_label) in enumerate(zip(data, label)):
        print(f"  Element {idx + 1}: Data = {single_data.size()}, Label = {single_label}")
    print("-" * 50)



class DFCNN(nn.Module):
    def __init__(self, num_classes):
        super().__init__()
        self.conv1 = nn.Conv2d(in_channels=1, out_channels=16, kernel_size=3, stride=1, padding=1)
        self.conv2 = nn.Conv2d(in_channels=16, out_channels=32, kernel_size=3, stride=1, padding=1)
        self.conv3 = nn.Conv2d(in_channels=32, out_channels=64, kernel_size=3, stride=1, padding=1)
        self.pool = nn.MaxPool2d(kernel_size=2, stride=2)
        self.fc1 = nn.Linear(64 * 64 * 107, 512)
        self.fc2 = nn.Linear(512, num_classes)
        self.dropout = nn.Dropout(p=0.5)

    def forward(self, x):
        x = self.pool(F.relu(self.conv1(x)))
        x = self.pool(F.relu(self.conv2(x)))
        x = self.pool(F.relu(self.conv3(x)))
        x = x.view(x.size(0), -1)
        x = F.relu(self.fc1(x))
        x = self.dropout(x)
        x = self.fc2(x)
        return x



print('网络部分开始')
network = DFCNN(num_classes=2).to(device)
print('损失函数部分开始')
Loss = nn.CrossEntropyLoss()
print('优化器部分开始')
lr = 0.005
optimizer = torch.optim.Adam(network.parameters(), lr)



print('训练部分开始')


model_path = os.path.join(project_path, 'model', 'model_state_dict.pth')


if os.path.exists(model_path):
    network.load_state_dict(torch.load(model_path))

network.train()
num_epochs = 2
for epoch in range(num_epochs):
    i = 1
    for features, labels in train_dataloader:
        features, labels = features.to(device), labels.to(device)
        optimizer.zero_grad()
        output = network(features)
        loss = Loss(output, labels)
        loss.backward()
        optimizer.step()
        i += 1
        if i % 2 == 0:
            print(f'第{epoch + 1}轮，第{i}个损失：{loss}')
    print(f'第{epoch + 1}轮最后一次损失：{loss}')
torch.save(network.state_dict(), os.path.join(project_path, 'model', 'model_state_dict.pth'))



print('测试部分开始')
network.eval()
correct = 0
total = 0
with torch.no_grad():
    for features, labels in test_dataloader:
        features, labels = features.to(device), labels.to(device)
        outputs = network(features)
        _, predicted = torch.max(outputs, dim=1)
        total += labels.size(0)
        correct += (predicted == labels).sum().item()
acc = correct / total
print(f'acc:{acc}')
