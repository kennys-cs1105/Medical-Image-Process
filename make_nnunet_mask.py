import numpy as np
import os
from glob import glob
from tqdm import tqdm
import SimpleITK as sitk

def create_mask(clean_path, label_path, mask_path, sitk_path):
    # 读取数据
    clean_data = np.load(clean_path, allow_pickle=True)
    label_data = np.load(label_path, allow_pickle=True)

    # 获取数据维度
    _, depth, height, width = clean_data.shape

    # 初始化掩码
    mask = np.zeros((1, depth, height, width), dtype=np.uint8)

    # 解析坐标和直径
    coord_x, coord_y, coord_z, diameter = label_data[0]

    # 计算球体半径
    radius = diameter / 2

    # 生成掩码
    for z in range(depth):
        for y in range(height):
            for x in range(width):
                if ((x - coord_x)**2 + (y - coord_y)**2 + (z - coord_z)**2) <= radius**2:
                    mask[0, z, y, x] = 1
 
    # 保存掩码
    np.save(mask_path, mask)   
    # print(type(mask))
    
    sitk_img = sitk.GetImageFromArray(mask[0])
    sitk.WriteImage(sitk_img, sitk_path)


def process_directory(directory):
    # 获取所有_clean.npy文件的路径
    clean_files = glob(os.path.join(directory, '*_clean.npy'))

    for clean_file in tqdm(clean_files):
        # 获取文件名（不包括扩展名）
        file_id = os.path.basename(clean_file).replace('_clean.npy', '')
        
        # 对应的label文件路径
        label_file = os.path.join(directory, f'{file_id}_label.npy')
        
        # 对应的mask文件路径
        mask_file = os.path.join(directory, f'{file_id}_mask.npy')

        sitk_file = os.path.join(directory, f'{file_id}_mask.nii.gz')
        
        if os.path.exists(label_file):
            create_mask(clean_file, label_file, mask_file, sitk_file)
        else:
            print(f"Label file not found for {clean_file}")

# 设置CT文件夹路径
ct_directory = './utils/CT'

# 处理CT文件夹中的所有文件
process_directory(ct_directory)
