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
    features_list = []
    labels_list = []
    
    for file_name in feature_list:
        base_name = file_name.split(".")[0]

        if base_name:
            features_list.append(base_name)
        else:
            raise ValueError(f"文件名：'{file_name}'不符合预期格式")
        
        match = pattern.search(file_name)

        if match:
            labels_list.append(int(match.group(1)))
        else:
            raise ValueError(f"文件名：'{file_name}'不符合预期格式")

    creat_csv(train_dataset_feature_csv, features_list)
    creat_csv(train_dataset_label_csv, labels_list)



def creat_test_csv():
    test_dataset_feature_csv = os.path.join(project_path, 'test_dataset_feature_csv.csv')
    test_dataset_label_csv = os.path.join(project_path, 'test_dataset_label_csv.csv')

    test_dataset_path = config.get('path', 'test_dataset_path')
    test_dataset_path = os.path.join(project_path, test_dataset_path)

    feature_list = filenameList(test_dataset_path)
    features_list = []
    labels_list = []
    
    for file_name in feature_list:
        base_name = file_name.split(".")[0]
        if base_name:
            features_list.append(base_name)
        else:
            raise ValueError(f"文件名：'{file_name}'不符合预期格式")
        match = pattern.search(file_name)
        if match:
            labels_list.append(int(match.group(1)))
        else:
            raise ValueError(f"文件名：'{file_name}'不符合预期格式")
            
    creat_csv(test_dataset_feature_csv, features_list)
    creat_csv(test_dataset_label_csv, labels_list)


creat_train_csv()
creat_test_csv()



# import os
# import re
# import csv
# import configparser

# # 假设 filenameList 和 creat_csv 是已定义的函数
# # def filenameList(path):
# #     # 返回路径下所有文件名的列表
# #     pass

# # def creat_csv(file_path, data_list):
# #     # 将数据列表写入 CSV 文件
# #     with open(file_path, 'w', newline='') as f:
# #         writer = csv.writer(f)
# #         writer.writerow(data_list)

# # 定义通用函数
# def create_dataset_csv(dataset_type):
#     # 根据数据集类型获取路径和文件名
#     feature_csv_name = f'{dataset_type}_dataset_feature_csv.csv'
#     label_csv_name = f'{dataset_type}_dataset_label_csv.csv'
#     dataset_path_key = f'{dataset_type}_dataset_path'
    
#     feature_csv_path = os.path.join(project_path, feature_csv_name)
#     label_csv_path = os.path.join(project_path, label_csv_name)
    
#     dataset_path = config.get('path', dataset_path_key)
#     dataset_path = os.path.join(project_path, dataset_path)
    
#     # 获取特征文件名列表
#     feature_list = filenameList(dataset_path)
#     label_list = []
    
#     for file_name in feature_list:
#         match = pattern.search(file_name)
#         if match:
#             label_list.append(int(match.group(1)))
#         else:
#             raise ValueError(f"文件名：'{file_name}'不符合预期格式")
    
#     # 创建 CSV 文件
#     creat_csv(feature_csv_path, feature_list)
#     creat_csv(label_csv_path, label_list)

# # 调用通用函数
# def creat_train_csv():
#     create_dataset_csv('train')

# def creat_test_csv():
#     create_dataset_csv('test')