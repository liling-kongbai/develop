import os
import csv
import torchaudio



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




import torch
from torch.utils.data import Dataset, DataLoader

class audio_Dataset(Dataset):
    def __init__(self, data, labels, train, transform=None):
        # 初始化数据集，可能包括数据预处理
        
        
        if train:
            self.data = [os.path.join(project_path, 'develop\\train', i, '_', j + '.wav') for i, j in zip(data, labels)]
        else:
            self.data = [os.path.join(project_path, 'develop\\test', i, '_', j + '.wav') for i, j in zip(data, labels)]

        self.labels = labels
        self.transform = transform

    def __len__(self):
        return len(self.data)

    def __getitem__(self, idx):
        sample_data = self.data[idx]
        sample_label = self.labels[idx]









        
        waveform, _ = torchaudio.load(sample_data)
        vie = torchaudio.transforms.Spectrogram()


# 在返回之前要不要正则化，要不要把预处理放在这里？？？！！！











        if self.transform:
            sample_data = self.transform(sample_data)

        # 返回时通常要将数据转换为张量类型
        return torch.tensor(sample_data, dtype=torch.int64), torch.tensor(sample_label, dtype=torch.uint8)









# 创建数据集实例
dataset = audio_Dataset(list(map(int, readCSV('train_dataset_feature_csv.csv'))), list(map(int, readCSV('train_dataset_label_csv.csv'))))

# 使用 DataLoader 加载数据集
dataloader = DataLoader(dataset, batch_size=1, shuffle=True)











# 更改自定义数据集，如果可以应该集成预处理步骤