#HEIC to JPG image format batch conversion script for Python 3. Tested on Windows 10.
#需要下载安装这个，: https://www.imagemagick.org/



#转换heic到jpg，并删除jgp，jpeg的gps信息，删除heic原始文件

import os
import subprocess

def convert_and_remove_gps(directory):
    for root, dirs, files in os.walk(directory):
        for filename in files:
            file_path = os.path.join(root, filename)
            if filename.lower().endswith('.heic'):
                print(f'Converting {file_path}...')
                subprocess.run(['magick', file_path, '-strip', f'{os.path.splitext(file_path)[0]}.jpg'])
                os.remove(file_path)
            elif filename.lower().endswith('.jpg') or filename.lower().endswith('.jpeg'):
                print(f'Removing GPS information from {file_path}...')
                subprocess.run(['magick', file_path, '-strip', file_path])

# 使用当前目录作为根目录，递归遍历所有 HEIC、JPG 和 JPEG 文件并进行转换和移除操作
convert_and_remove_gps('.')


