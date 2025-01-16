import re

# 示例文件名
file_name = 'C:\\Users\\kongbai\\study\\develop\\VoiceWakeUpEngine\\dataset\\test\\1736996407_0.wav'
# 定义正则表达式模式
pattern = re.compile(r'_(\d+)\.wav$')

# 使用正则表达式提取标签
def extract_label_from_filename(filename):
    match = pattern.search(filename)
    # ?????
    if match:
        return int(match.group(1))
    else:
        raise ValueError(f"文件名 {filename} 不符合预期格式")

# 示例使用
label = extract_label_from_filename(file_name)
print(f"文件 {file_name} 的标签是: {label}")