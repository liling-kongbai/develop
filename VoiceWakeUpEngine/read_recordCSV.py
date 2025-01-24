import os
import csv



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

readCSV('train_dataset_feature_csv.csv')
readCSV('train_dataset_label_csv.csv')








import torch
from torch.utils.data import Dataset, DataLoader

class audio_Dataset(Dataset):
    def __init__(self, data, labels, transform=None):
        # 初始化数据集，可能包括数据预处理
        self.data = data
        self.labels = labels
        self.transform = transform

    def __len__(self):
        return len(self.data)

    def __getitem__(self, idx):
        sample_data = self.data[idx]
        sample_label = self.labels[idx]

        if self.transform:
            sample_data = self.transform(sample_data)

        # 返回时通常要将数据转换为张量类型
        return torch.tensor(sample_data, dtype=torch.float32), torch.tensor(sample_label, dtype=torch.long)



# 创建数据集实例
dataset = audio_Dataset(readCSV('train_dataset_feature_csv.csv'), readCSV('train_dataset_label_csv.csv'))

# 使用 DataLoader 加载数据集
dataloader = DataLoader(dataset, batch_size=2, shuffle=True)

# 遍历 DataLoader
for batch in dataloader:
    batch_data, batch_labels = batch
    print(f"Batch data: {batch_data}\nBatch labels: {batch_labels}")