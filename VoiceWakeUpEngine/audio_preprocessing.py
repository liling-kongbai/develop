import os
import sounddevice
import scipy
from pydub import AudioSegment


# 统计音频数据集的数量
def filenameList(dataset_address):
    os.makedirs(name=dataset_address, exist_ok=True)
    filename = os.listdir(dataset_address)
    return filename

# makedirs(name, mode=0o777, exist_ok=False)递归地创建目录
# name(str)要创建的目录路径，如果路径中有多个目录层级，会递归地创建所有不存在的目录
# mode(int)设置目录的权限模式，默认为0o777，表示目录对所有用户都是可读，可写，可执行的
# exist_ok(bool)为True，目录已存在时，函数不会引发FileExistsError错误，而是正常返回，默认为False

# listdir()列出指定目录下的所有文件和文件夹名称
# path可选，指定要列出文件和文件夹的目录路径，如果省略该参数或传递`.`，则默认为当前工作目录
# 返回列表，包含指定目录下的所有文件和文件夹名称，不包括`.`，当前目录，`..`，父目录


# 录音
def record(record_wakeword_time, samplerate, channels, filename):
    audio = sounddevice.rec(frames=record_wakeword_time * samplerate, samplerate=samplerate, channels=channels)
    sounddevice.wait()
    scipy.io.wavfile.write(filename, samplerate, audio)

# rec(frames=None, samplerate=None, channels=None, dtype=None, out=None, mapping=None, blocking=False, callback=None, kwargs)录制音频
# frames(int)录制的帧数，为None，表示录制到用户停止
# samplerate(int)采样率，为None，使用默认采样率
# channels(int/None)录制的声道数，为None，使用默认声道数
# dtype(str)录制的数据类型，为None，使用默认数据类型
# out(ndarray)用于输出录制的音频数据的numpy数组，为None，不进行输出
# mapping(list)用于映射声道顺序的列表，为None，使用默认声道顺序
# blocking(bool)是否进行阻塞式录制，默认为False，表示非阻塞式，为True，函数会等待录制完成后再返回
# callback(callable)在录制过程中处理音频数据的回调函数，默认为None，表示不进行回调处理

# wait(ignore_errors=False)等待所有活动的音频流完成，包括输入和输出
# ignore_errors(bool)默认为False，为True，在等待过程中，即使发生错误，也会继续等待

# write(filename, rate, data)将NumPy数组写入WAV文件
# filename(str/open file handle)输出的WAV文件名或已打开的文件句柄
# rate(int)采样率，以样本/秒为单位
# data(ndarray)一维或二维NumPy数组，可是整数或浮点数据类型

def overlop(background_audio_address, feature_audio_address, label_audio_address):
    background_audio = AudioSegment.from_file(background_audio_address)
    feature_audio = AudioSegment.from_file(feature_audio_address)
    overlop_audio = background_audio.overlay(feature_audio)
    overlop_audio.export(label_audio_address)