import os

# 定义目标目录
target_directory = './subset9'

list_file_path = os.listdir(target_directory)
# print(list_file_path)

# for filename in list_file_path:
#     print(filename)


# 重命名文件
for file_name in list_file_path:
    # print(file_name)

    new_file_name = file_name[34:]
    # print(new_file_name)

    old_file_path = os.path.join(target_directory, file_name)
    new_file_path = os.path.join(target_directory, new_file_name)

    # 重命名文件
    os.rename(old_file_path, new_file_path)

    print(f"Renamed: {old_file_path} -> {new_file_path}")
