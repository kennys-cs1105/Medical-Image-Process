"""
1. 已有npy文件D:\kennys\temporary\lung_nodule\tianchi\dataset\test\LKDS-11111_label.npy
2. 格式为uint8[1,175,512,512]
3. 要求将其转换为nii.gz文件
4. python代码
"""

import numpy as np
import SimpleITK as sitk
import os

# 定义文件路径
npy_file_path = r'D:\kennys\temporary\lung_nodule\tianchi\dataset\test\deeplung_mask.npy'
nii_file_path = r'D:\kennys\temporary\lung_nodule\tianchi\dataset\test\deeplung_mask.nii.gz'

# 加载 .npy 文件
data = np.load(npy_file_path)

# 确认数据格式
print(f"Data shape: {data.shape}")
print(f"Data type: {data.dtype}")
# print(data[0].shape)
data = data.astype(int)

# 将 NumPy 数组转换为 SimpleITK 图像
sitk_image = sitk.GetImageFromArray(data)
# sitk_image = sitk.GetImageFromArray(data[0])

# 保存为 .nii.gz 文件
sitk.WriteImage(sitk_image, nii_file_path)

print(f"Saved NIfTI image to {nii_file_path}")

