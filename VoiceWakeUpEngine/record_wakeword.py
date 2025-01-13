from config import read_config
import os
from audio_preprocessing import count, record
import time

config = read_config()
wakeword_dataset_address = config.get('address', 'wakeword_dataset_address')
wakeword_dataset_address = os.path.join(os.path.dirname(os.path.abspath(__file__)), wakeword_dataset_address)
record_wakeword_time = config.get('record_time', 'record_wakeword_time')
samplerate = config.get('audio', 'samplerate')
channels = config.get('audio', 'channels')
record_wakeword_time = int(record_wakeword_time)
samplerate = int(samplerate)
channels = int(channels)

wakeword_dataset_count = count(wakeword_dataset_address)
print(f'当前wakeword_count音频数据集的数量有{wakeword_dataset_count}条。')

record_count = int(input('请输入要录制的音频数量：'))
for i in range(record_count):
    input(f'现在录制第{i + 1}条，请回车开始！')
    record(record_wakeword_time, samplerate, channels, os.path.join(wakeword_dataset_address, str(int(time.time())) + '.wav'))
    if i + 1  == record_count:
        print('录制结束。')