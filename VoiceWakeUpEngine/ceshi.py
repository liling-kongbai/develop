from config import readConfig
from audio_preprocessing import filenameList, overlop


config = readConfig()


address_choice = int(input('请输入要合成音频的数据集（1，训练集；2，测试集）：'))
if address_choice == 1:
    dataset_address = config.get('address', 'train_dataset_address')
elif address_choice == 2:
    dataset_address = config.get('address', 'test_dataset_address')


overlop_count = int(input('请输入要合成的音频数量：'))


background_dataset_address = config.get('address', 'background_dataset_address')
wakeword_dataset_address = config.get('address', 'wakeword_dataset_address')
no_wakeword_dataset_address = config.get('address', 'no_wakeword_dataset_address')


wakeword_filename_list = filenameList(wakeword_dataset_address)
no_wakeword_filename_list = filenameList(no_wakeword_dataset_address)

for i in range(overlop_count):
    label_audio_address = 'C:\\Users\\kongbai\\study\\develop\\VoiceWakeUpEngine\\dataset\\test\\hahha.wav'
    overlop(background_audio_address, feature_audio_address, label_audio_address)