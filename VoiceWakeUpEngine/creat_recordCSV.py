from config import readConfig
import os
import re
import csv
from audio_preprocessing import filenameList



config = readConfig()

project_path = os.path.dirname(os.path.abspath(__file__))

pattern = re.compile(r'_(\d+)\.wav$')



def creat_csv(csv_path, list_data):
    with open(csv_path, mode="w", newline="", encoding="utf-8") as csv_file:
        csv_writer = csv.writer(csv_file)
        for line in list_data:
            csv_writer.writerow([line])
    print(f"文件创建完成!")



def creat_train_csv():
    train_dataset_feature_csv = os.path.join(project_path, 'train_dataset_feature_csv.csv')
    train_dataset_label_csv = os.path.join(project_path, 'train_dataset_label_csv.csv')

    train_dataset_path = config.get('path', 'train_dataset_path')
    train_dataset_path = os.path.join(project_path, train_dataset_path)

    feature_list = filenameList(train_dataset_path)
    label_list = []
    
    for file_name in feature_list:
        match = pattern.search(file_name)
        if match:
            label_list.append(int(match.group(1)))
        else:
            raise ValueError(f"文件名：'{file_name}'不符合预期格式")

    creat_csv(train_dataset_feature_csv, feature_list)
    creat_csv(train_dataset_label_csv, label_list)



def creat_test_csv():
    test_dataset_feature_csv = os.path.join(project_path, 'test_dataset_feature_csv.csv')
    test_dataset_label_csv = os.path.join(project_path, 'test_dataset_label_csv.csv')

    test_dataset_path = config.get('path', 'test_dataset_path')
    test_dataset_path = os.path.join(project_path, test_dataset_path)

    feature_list = filenameList(test_dataset_path)
    label_list = []
    
    for file_name in feature_list:
        match = pattern.search(file_name)
        if match:
            label_list.append(int(match.group(1)))
        else:
            raise ValueError(f"文件名：'{file_name}'不符合预期格式")

    creat_csv(test_dataset_feature_csv, feature_list)
    creat_csv(test_dataset_label_csv, label_list)


creat_train_csv()
creat_test_csv()