from config import readConfig
from audio_preprocessing import filenameList, overlop
import random
import os
import time

config = readConfig()


address_choice = int(input('请输入要合成音频的数据集（1，训练集；2，测试集）：'))
if address_choice == 1:
    dataset_address = config.get('address', 'train_dataset_address')
elif address_choice == 2:
    dataset_address = config.get('address', 'test_dataset_address')


overlop_count = int(input('请输入要合成的音频数量：'))



wakeword_dataset_address = config.get('address', 'wakeword_dataset_address')
no_wakeword_dataset_address = config.get('address', 'no_wakeword_dataset_address')
background_dataset_address = config.get('address', 'background_dataset_address')

project_address = os.path.dirname(os.path.abspath(__file__))


wakeword_filename_list = filenameList(os.path.join(project_address, wakeword_dataset_address))
no_wakeword_filename_list = filenameList(os.path.join(project_address, no_wakeword_dataset_address))
background_filename_list = filenameList(os.path.join(project_address, background_dataset_address))


for i in range(overlop_count):


    background_audio_filename = random.choices(background_filename_list)[0]
    background_audio_address = os.path.join(project_address, background_dataset_address, background_audio_filename)


    probability = random.random()
    if probability > 0.5:
        feature_audio_filename = random.choices(wakeword_filename_list)[0]
        feature_audio_address = os.path.join(project_address, wakeword_dataset_address, feature_audio_filename)
        overlop(background_audio_address, feature_audio_address, os.path.join(project_address, dataset_address, str(int(time.time())) + '_1' + '.wav'))
    else:
        feature_audio_filename = random.choices(no_wakeword_filename_list)[0]
        feature_audio_address = os.path.join(project_address, no_wakeword_dataset_address, feature_audio_filename)
        overlop(background_audio_address, feature_audio_address, os.path.join(project_address, dataset_address, str(int(time.time())) + '_0' + '.wav'))