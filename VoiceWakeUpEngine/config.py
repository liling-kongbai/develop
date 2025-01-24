import os
import configparser

def readConfig():
    project_path = os.path.dirname(os.path.abspath(__file__))
    config_ini = os.path.join(project_path, 'config.ini')
    config = configparser.ConfigParser()
    config.read(config_ini, encoding="utf-8")
    return config