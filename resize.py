import cv2 as cv
import os
import glob

path = r'data/zhulianzhen/mri/masks/*.png'
for i in glob.glob(path):
    im1 = cv.imread(i)
    im2 = cv.resize(im1,(512,512))
    cv.imwrite(os.path.join(r'data/zhulianzhen/mri/masks', os.path.basename(i)), im2)