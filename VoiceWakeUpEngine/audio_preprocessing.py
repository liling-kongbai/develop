import os
import sounddevice
import scipy

def count(dataset_address):
    os.makedirs(dataset_address, exist_ok=True)

    fileList = []
    for root, _, files in os.walk(dataset_address):
        for file in files:
            filename = os.path.join(root, file)
            fileList.append(filename)
    return fileList

# 录音
def record(seconds, rate, file_name, channels):
    audio = sounddevice.rec(int(seconds * rate), samlerate=rate, channels=channels)
    sounddevice.wait()
    # 用于等待音频流（录音或播放）完成
    scipy.io.wavfile.write(file_name, rate, audio)