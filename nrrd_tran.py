import nrrd
import PIL
from PIL import Image
import os
import cv2

# data_path=r'raw/ludeyun/ct/9 Fl_ThorAngio  1.0  Bv36  4.nrrd'
data_path = r'226/14-DA.nrrd'
# save_path='./data/save'     # 图片数据的保存文件夹
save_path = '226/mask-14DA'

# 检查路径
assert os.path.exists(data_path), data_path+' : path error !'
if not os.path.exists(save_path):
	os.makedirs(save_path)
	
data, options = nrrd.read(data_path)
for i in range(data.shape[2]):
	img=Image.fromarray(data[:,:,i]*255) # 截取第j个通道的前i张图
	temp_path=save_path + '/' + str(i) +'.png'
	img.convert('RGB').save(temp_path) # 保存图像数据

# raw\zhulianzhen\mri\Segmentation_2.seg.nrrd