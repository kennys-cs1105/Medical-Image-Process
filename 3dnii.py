import scipy, shutil, os
import sys, getopt
import imageio
from tqdm import tqdm
import nibabel as nib
import numpy as np


def niito2D(filepath, outputpath):
    inputfiles = os.listdir(filepath)  # 遍历文件夹数据
    outputfile = outputpath
    print('Input file is   : ', inputfiles)
    print('Output folder is: ', outputfile)
    file_count = 0  # 文件计数器

    for inputfile in inputfiles:
        image = nib.load(filepath + inputfile)
        image_array = image.get_fdata()  # 数据读取
        # print(len(image_array.shape))
        file_count = file_count + 1
        (x, y, z) = image_array.shape  # 获得数据shape信息：（长，宽，维度-切片数量）

        # 不同3D体数据有用的切片数量不同，自行查看，自行设定起止数量
        total_slices = 23  # 总切片数
        slice_counter = 0 # 从第几个切片开始

        loop = tqdm(range(slice_counter, slice_counter + total_slices))  # 单纯为了花哨的写法
        for current_slice in loop:
            if (slice_counter % 1) == 0:
                data = image_array[:, :, current_slice].astype(np.uint8)  # 保存该切片，可以选择不同方向。当前保存Sag方向，可自行调整顺序

                if (slice_counter % 1) == 0:
                    # 切片命名
                    image_name = inputfile[:-6] + "{:0>3}".format(str(current_slice + 1)) + ".png"
                    # 保存
                    imageio.imwrite(image_name, data)

                    # 移动到输出文件夹
                    src = image_name
                    shutil.move(src, outputfile)
                    slice_counter += 1

                    loop.set_description(f'文件数：[{file_count}/{len(inputfiles)}]')
    print('Finished converting images')


if __name__ == '__main__':
    input_path = './second/'
    output_path = 'output/'
    niito2D(input_path, output_path)

"""
change the file path when runing
change the total num of slice and choose which one needed
"""







