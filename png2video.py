import cv2
import os

# 设置图片目录和视频输出路径
image_folder = 'D:\\kennys\\temporary\\lung_nodule\\tianchi\\utils\\exp1'
video_name = 'ct_series.avi'

# 获取图片文件列表并排序
images = [img for img in os.listdir(image_folder) if img.endswith(".png")]
images.sort()  # 确保按顺序排列

# 获取第一张图片以获取图像尺寸
first_image_path = os.path.join(image_folder, images[0])
frame = cv2.imread(first_image_path)
height, width, layers = frame.shape

# 定义视频编码器和输出视频参数
fourcc = cv2.VideoWriter_fourcc(*'XVID')  # 选择视频编码格式，'XVID' 是常见格式之一
video = cv2.VideoWriter(video_name, fourcc, 4, (width, height))  # 1 为帧率，可根据需要调整

# 逐帧写入视频
for image in images:
    image_path = os.path.join(image_folder, image)
    frame = cv2.imread(image_path)
    video.write(frame)

# 释放视频写入对象
video.release()

print(f"Video saved as {video_name}")
