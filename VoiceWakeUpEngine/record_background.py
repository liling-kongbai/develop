from config import readConfig
import os
from audio_preprocessing import filenameList, record
import time

config = readConfig()
background_dataset_address = config.get('address', 'background_dataset_address')
background_dataset_address = os.path.join(os.path.dirname(os.path.abspath(__file__)), background_dataset_address)
record_background_time = config.get('record_time', 'record_background_time')
samplerate = config.get('audio', 'samplerate')
channels = config.get('audio', 'channels')
record_background_time = int(record_background_time)
samplerate = int(samplerate)
channels = int(channels)

filename_list = filenameList(background_dataset_address)
print(f'当前background音频数据集的数量有{filename_list}条。')

record_count = int(input('请输入要录制的音频数量：'))
for i in range(record_count):
    input(f'现在录制第{i + 1}条，请回车开始！')
    record(record_background_time, samplerate, channels, os.path.join(background_dataset_address, str(int(time.time())) + '.wav'))
    if i + 1  == record_count:
        print('录制结束。')