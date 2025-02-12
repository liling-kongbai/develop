from config import readConfig
import os
from audio_preprocessing import filenameList, record
import datetime

config = readConfig()
no_wakeword_dataset_path = config.get('path', 'no_wakeword_dataset_path')
no_wakeword_dataset_path = os.path.join(os.path.dirname(os.path.abspath(__file__)), no_wakeword_dataset_path)
record_no_wakeword_time = config.get('record_time', 'record_no_wakeword_time')
samplerate = config.get('audio', 'samplerate')
channels = config.get('audio', 'channels')
record_no_wakeword_time = int(record_no_wakeword_time)
samplerate = int(samplerate)
channels = int(channels)

filename_list = filenameList(no_wakeword_dataset_path)
print(f'当前no_wakeword_count音频数据集的数量有{len(filename_list)}条。')

record_count = int(input('请输入要录制的音频数量：'))
for i in range(record_count):
    input(f'现在录制第{i + 1}条，请回车开始！')
    record(record_no_wakeword_time, samplerate, channels, os.path.join(no_wakeword_dataset_path, datetime.datetime.now().strftime("%Y%m%d%H%M%S%f") + '.wav'))
    if i + 1  == record_count:
        print('录制结束。')