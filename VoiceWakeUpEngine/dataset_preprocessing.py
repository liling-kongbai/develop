from config import readConfig
from audio_preprocessing import filenameList, overlop
import random
import os
import datetime

config = readConfig()


path_choice = int(input('请输入要合成音频的数据集（1，训练集；2，测试集）：'))
if path_choice == 1:
    dataset_path = config.get('path', 'train_dataset_path')
elif path_choice == 2:
    dataset_path = config.get('path', 'test_dataset_path')


overlop_count = int(input('请输入要合成的音频数量：'))



wakeword_dataset_path = config.get('path', 'wakeword_dataset_path')
no_wakeword_dataset_path = config.get('path', 'no_wakeword_dataset_path')
background_dataset_path = config.get('path', 'background_dataset_path')

project_path = os.path.dirname(os.path.abspath(__file__))


wakeword_filename_list = filenameList(os.path.join(project_path, wakeword_dataset_path))
no_wakeword_filename_list = filenameList(os.path.join(project_path, no_wakeword_dataset_path))
background_filename_list = filenameList(os.path.join(project_path, background_dataset_path))


for i in range(overlop_count):


    background_audio_filename = random.choices(background_filename_list)[0]
    background_audio_path = os.path.join(project_path, background_dataset_path, background_audio_filename)


    probability = random.random()
    if probability > 0.5:
        feature_audio_filename = random.choices(wakeword_filename_list)[0]
        feature_audio_path = os.path.join(project_path, wakeword_dataset_path, feature_audio_filename)
        overlop(background_audio_path, feature_audio_path, os.path.join(project_path, dataset_path, datetime.datetime.now().strftime("%Y%m%d%H%M%S%f") + '_1' + '.wav'))
    else:
        feature_audio_filename = random.choices(no_wakeword_filename_list)[0]
        feature_audio_path = os.path.join(project_path, no_wakeword_dataset_path, feature_audio_filename)
        overlop(background_audio_path, feature_audio_path, os.path.join(project_path, dataset_path, datetime.datetime.now().strftime("%Y%m%d%H%M%S%f") + '_0' + '.wav'))
