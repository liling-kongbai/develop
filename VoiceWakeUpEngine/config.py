import os
import configparser

def readConfig():
    project_address = os.path.dirname(os.path.abspath(__file__))
    config_ini = os.path.join(project_address, 'config.ini')
    config = configparser.ConfigParser()
    config.read(config_ini, encoding="utf-8")
    return config