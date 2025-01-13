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

print(samplerate)
print(record_wakeword_time)

print(type(samplerate))
print(type(record_wakeword_time))

s = int(samplerate)
print(s)
print(type(s))

r = int(record_wakeword_time)
print(r)
print(type(r))

# chengji = samplerate * record_wakeword_time
cj = s * r
# print(chengji)
print(cj)