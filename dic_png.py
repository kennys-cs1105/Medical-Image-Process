import os
import SimpleITK
import numpy as np
import cv2
from tqdm import tqdm
import shutil


def convert_from_dicom_to_jpg(img, low_window, high_window, save_path):
    lungwin = np.array([low_window * 1, high_window * 5])
    newimg = (img - lungwin[0]) / (lungwin[1] - lungwin[0])  # 归一化
    newimg = (newimg * 255).astype('uint8')  # 将像素值扩展到[0,255]
    stacked_img = np.stack((newimg,) * 3, axis=-1)
    cv2.imwrite(save_path, stacked_img, [int(cv2.IMWRITE_JPEG_QUALITY), 100])


if __name__ == '__main__':
    # dicom文件目录
    # dicom_dir = '1_bmode/'
    dicom_dir = './106/arterial phase/'

    path = "106_image1"
    if os.path.exists(path):
        shutil.rmtree(path)
    os.makedirs(path)
    for i in tqdm(os.listdir(dicom_dir)):
        dcm_image_path = os.path.join(dicom_dir, i)  # 读取dicom文件
        name, _ = os.path.splitext(i)
        output_jpg_path = os.path.join(path, name + '.png')
        ds_array = SimpleITK.ReadImage(dcm_image_path)  # 读取dicom文件的相关信息
        img_array = SimpleITK.GetArrayFromImage(ds_array)  # 获取array
        # SimpleITK读取的图像数据的坐标顺序为zyx，即从多少张切片到单张切片的宽和高，此处我们读取单张，因此img_array的shape
        # 类似于 （1，height，width）的形式
        shape = img_array.shape
        img_array = np.reshape(img_array, (shape[1], shape[2]))  # 获取array中的height和width
        high = np.max(img_array)
        low = np.min(img_array)
        convert_from_dicom_to_jpg(img_array, low, high, output_jpg_path)  # 调用函数，转换成jpg文件并保存到对应的路径

# import os
# import pydicom       #用于读取DICOM(DCOM)文件
# import argparse
# # import scipy.misc    #用imageio替代
# import imageio
# import shutil


# def convert(imgway_1, imgway_2):
#     # imgway_1为源文件夹
#     # imgway_2为jpg文件夹
#     # imgway_1 = opt.origin
#     # imgway_2 = opt.JPG

#     path = imgway_2
#     if os.path.exists(path):
#         shutil.rmtree(path)
#     os.makedirs(path)

#     i = 0

#     for filename in os.listdir(r"%s" % imgway_1):

#         # name = str(i)
#         name = filename[:-4]

#         ds = pydicom.read_file("%s/%s" % (imgway_1, filename), force=True)  # 读取文件

#         img = ds.pixel_array.astype('uint8')

#         imageio.imwrite("%s/%s.png" % (path, name), img)

#         i += 1

#         print("True")

#         if i == 300:  # 转换300张
#             break

# # if __name__ == '__main__':
# #     parser = argparse.ArgumentParser()
# #     parser.add_argument('--origin', type=str, default='data/%s/arterial phase', help='train photos')
# #     parser.add_argument('--JPG', type=str, default='data_png/%s/image', help='test photos')
# #     opt=parser.parse_args()
# #     print(opt)

#     # def convert(imgway_1,imgway_2):
#     # #imgway_1为源文件夹
#     # #imgway_2为jpg文件夹
#     #     imgway_1=opt.origin
#     #     imgway_2 = opt.JPG
#     #
#     #     path = imgway_2
#     #     if os.path.exists(path):
#     #         shutil.rmtree(path)
#     #     os.makedirs(path)
#     #
#     #     i=0
#     #
#     #     for filename in os.listdir(r"%s" % imgway_1):
#     #
#     #     # name = str(i)
#     #         name=filename[:-4]
#     #
#     #         ds = pydicom.read_file("%s/%s" % (imgway_1, filename))          #读取文件
#     #
#     #         img = ds.pixel_array.astype('uint8')
#     #
#     #         imageio.imwrite("%s/%s.png" % (path, name), img)
#     #
#     #         i+=1
#     #
#     #         print("True")
#     #
#     #         if i==300:      #转换300张
#     #             break
# for i in range(44,108):
#     convert('data/%s/arterial phase'%i,'data_new/%s/image'%i)
