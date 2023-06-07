# import nibabel as nib
# import os
# import imageio

# img_path = './second/1.nii'
# img = nib.load(img_path)
# # img_fdata = img.get_fdata().transpose(1,0)
# img_fdata = img.get_fdata()
# saving_path  = './second/'
# print(img.shape)


# imageio.imwrite(os.path.join(saving_path,'0_png_Label.png'),img_fdata)

import os
import cv2
import numpy as np
import nibabel as nib
import SimpleITK as sitk
from PIL import Image

file_root = r'trans/' 
save_path = r'trans/png/'
#file_list
file_list = os.listdir(file_root)
print(file_list)
for img_name in file_list:
    if img_name.endswith('.nii.gz'):
        img_path = file_root + img_name
        print(img_path)
        #data = np.load(img_path)
        #img1 = nib.load(img_path) 
        #img = img1.get_fdata()
        img1 = sitk.ReadImage(img_path)
        img = sitk.GetArrayFromImage(img1)
        img = (img - img.min())/(img.max()-img.min())
        #print(img.min(),img.max())
        img = img * 255
        cv2.imwrite(save_path +img_name +'.png', img)           
