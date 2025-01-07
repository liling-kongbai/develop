import os
import configparser

def read_config():
    # 获取当前文件所在目录 
    address = os.path.dirname(os.path.abspath(__file__))
    # 组装config.ini路径，也可以直接写配置文件的具体路径，不用自动获取
    config_dir = os.path.join(address, 'config.ini')
 
 
    # 创建configparser对象
    cf = configparser.ConfigParser()
    # 读取config.ini
    cf.read(config_dir, encoding="utf-8")
    return cf