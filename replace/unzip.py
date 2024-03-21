# -*- coding: utf-8 -*-
# 解压图片并复制到新的目录
import os
import zipfile
import shutil

import shutil

def unzip_and_copy(source_dir, dest_dir):
    # 确保目标目录存在，如果不存在则创建
    if not os.path.exists(dest_dir):
        os.makedirs(dest_dir)
    
    # 遍历源目录下的所有文件
    for root, dirs, files in os.walk(source_dir):
        for filename in files:
            if filename.lower().endswith('.zip'):  # 如果是 zip 文件
                zip_file_path = os.path.join(root, filename)
                extract_dir = os.path.splitext(zip_file_path)[0]  # 解压目录名
                
                # 解压 zip 文件
                with zipfile.ZipFile(zip_file_path, 'r') as zip_ref:
                    zip_ref.extractall(extract_dir)
                
                # 将解压后的文件复制到目标目录
                for root2, dirs2, files2 in os.walk(extract_dir):
                    for file in files2:
                        file_path = os.path.join(root2, file)
                        filename = os.path.basename(file_path)
                        print("file_path '%s'" % (filename))
                        # 构建目标目录中的文件路径
                        dest_file_path = os.path.join(dest_dir, filename)
                        # 确保目标目录存在
                        if not os.path.exists(os.path.dirname(dest_file_path)):
                            os.makedirs(os.path.dirname(dest_file_path))
                        if os.path.exists(dest_file_path):
                            new_filename = generate_new_filename(filename, dest_dir)
                            dest_file_path = os.path.join(dest_dir, new_filename)   
                        # 复制文件
                        shutil.copy2(file_path, dest_file_path)
                        print("已复制文件 '%s' 到 '%s'" % (file_path, dest_file_path))

def empty_directory(directory):
    for filename in os.listdir(directory):
        file_path = os.path.join(directory, filename)
        try:
            if os.path.isfile(file_path):
                os.remove(file_path)
                # print("已删除文件:", file_path)
        except Exception as e:
            print("删除文件时出错:", e)

def generate_new_filename(filename, directory):
    basename, extension = os.path.splitext(filename)
    i = 1
    while True:
        new_filename = f"{basename}_{i}{extension}"
        new_file_path = os.path.join(directory, new_filename)
        if not os.path.exists(new_file_path):
            return new_filename
        i += 1
if __name__ == "__main__":
    # 源目录
    source_directory = "../sources/old"
    
    # 目标目录
    dest_directory = "../sources/new"
    
    empty_directory(dest_directory)
    # 执行解压和复制操作
    unzip_and_copy(source_directory, dest_directory)

