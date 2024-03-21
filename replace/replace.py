
# -*- coding: utf-8 -*-
# 替换图片
import os
import shutil

def replace_files(source_dir, target_dir):
    # 用于存储目标目录中已替换的文件名
    replaced_files = []

    # 遍历目标目录中的所有文件
    for root, _, files in os.walk(target_dir):
        for file in files:
            target_file_path = os.path.join(root, file)
            source_file_path = os.path.join(source_dir, file)
            
            # 如果源文件存在，则替换目标目录中的文件
            if os.path.exists(source_file_path):
                print(f"替换 {target_file_path}")
                shutil.copy2(source_file_path, target_file_path)
                replaced_files.append(file)

    # 找出目标目录中未匹配到的文件
    unreplaced_files = []
    for root, _, files in os.walk(source_dir):
        for file in files:
            if file not in replaced_files:
                unreplaced_files.append(file)

    return unreplaced_files

# 目录A和目录B
directory_A = '../sources/output'
directory_B = '/Users/bairdweng/Desktop/miya/miya/MZAudio/Images.xcassets/Mine/Intimate'

unreplaced_files = replace_files(directory_A, directory_B)

# 打印未匹配到的文件
print("\n在目标目录中未找到匹配的文件:")
for file in unreplaced_files:
    print(file)