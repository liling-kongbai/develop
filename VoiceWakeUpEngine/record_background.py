from ceshi import read_config
from audio_preprocessing import collect, record
import time


cf = read_config()
background_dataset_address = cf('address', 'wakeword_dataset_address')
record_background_record_time = cf('record_time', 'record_background_record_time')


background_list = collect(background_dataset_address)
print(f'当前background音频数量：{len(background_list)}')

record_time = int(input('请输入要录制的音频数量：'))
for i in range(record_time):
    input(f'第{i + 1}条， 回车开始……')
    # 聪明的功能，手动跳过
    record(f'{background_dataset_address}/{int(time.time())}.wav', record_background_record_time)