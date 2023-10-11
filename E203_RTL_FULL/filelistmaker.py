import os
import glob

def get_v_files(folder):
    v_files = []
    # 遍历文件夹及其子文件夹中的.v文件
    for root, dirs, files in os.walk(folder):
        for file in files:
            if file.endswith('.v'):
                file_path = os.path.abspath(os.path.join(root, file))
                file_path = file_path.replace('\\', '/')  # 替换路径中的\为/
                v_files.append(file_path)
    return v_files

def write_to_file(file_list, output_file):
    # 将路径写入文件
    with open(output_file, 'w') as f:
        for file_path in file_list:
            f.write(file_path + '\n')

# 指定文件夹路径
folder_path = './'

# 获取.v文件列表
v_files_list = get_v_files(folder_path)

# 输出到文件
output_file_path = 'vflist'
write_to_file(v_files_list, output_file_path)