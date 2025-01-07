import torch
from torch import nn
from torch.nn import functional as F

class DFCNN_block(nn.Module):
    def __init__(self, in_channels, out_channels):
        super().__init__()
        self.conv1 = nn.Conv2d(in_channels, out_channels, kernel_size=3, padding='same')
        self.bn1 = nn.BatchNorm2d(out_channels)
        self.conv2 = nn.Conv2d(out_channels, out_channels * 2, kernel_size=3, padding='same')
        self.bn2 = nn.BatchNorm2d(out_channels * 2)
        self.max_pool = nn.MaxPool2d(kernel_size=2, padding='valid', stride=2)

    def forword(self, x):
        y = F.relu(self.bn1(self.conv1(x)))
        y = F.relu(self.bn2(self.conv2(y)))
        y = self.max_pool(y)
        return y

class DFCNN(nn.Module):
    def __init__(self, in_channels, out_channels):
        super().__init__()
        self.block1 = DFCNN_block(in_channels, out_channels)
        self.block2 = DFCNN_block(out_channels * 2)
        self.block3 = DFCNN_block(out_channels * 4)
        self.block4 = DFCNN_block(out_channels * 8)
        self.block5 = DFCNN_block(out_channels * 16)
        self.fc1 = nn.Linear(input / 32 * 1024, input / 16 * 512)
        self.fc2 = nn.Linear(input / 16 * 512, input / 8 * 126)
        self.fc3 = nn.Linear(input / 8 * 256, input / 4 * 128)
        self.fc4 = nn.Linear(input / 4 * 128, input / 2 * 64)
        self.fc5 = nn.Linear(input / 2 * 64, input * 32)
        self.fc6 = nn.Linear(input * 32, input * 8)
        self.fc7 = nn.Linear(input * 8, input * 2)
        self.fc8 = nn.Linear(input * 2, input / 2)
        self.fc9 = nn.Linear(input / 2, input / 8)
        self.fc10 = nn.Linear(input / 8, input / 32)
        self.fc11 = nn.Linear(input / 32, 2)
# F.softmax