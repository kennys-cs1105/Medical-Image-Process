import nrrd
import nibabel as nib
import numpy as np

# nrrd 文件保存路径
data_path=r'./raw/chenyuanchun/mri/t1/401T1W_TSE_9.nrrd'
save_path='./data/1.nii'

data,options=nrrd.read(data_path)  # 读取 nrrd 文件
img=nib.Nifti1Image(data,np.eye(4)) # 将 nrrd 文件转换为 .nii 文件
nib.save(img,save_path) # 保存 nii 文件
