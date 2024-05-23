import numpy as np
from PIL import Image

npy_file = r'D:\kennys\temporary\lung_nodule\tianchi\utils\test\images_0073_0964.npy'

array = np.load(npy_file)

# 检查数组的形状
print(array.shape)  # (3, 512, 512)

# 将浮点数转换为 uint8
# 需要将值缩放到 0-255 范围
scaled_array = np.zeros_like(array, dtype=np.uint8)
for i in range(array.shape[0]):
    channel = array[i]
    channel = (channel - np.min(channel)) / (np.max(channel) - np.min(channel))  # 归一化到0-1范围
    channel = (channel * 255).astype(np.uint8)  # 缩放到0-255范围并转换为uint8
    scaled_array[i] = channel

# 遍历数组的第一个维度，将每个通道保存为独立的 PNG 文件
for i in range(scaled_array.shape[0]):
    img_array = scaled_array[i]

    # 将数组转换为 PIL 图像对象
    img = Image.fromarray(img_array)

    # 保存图像
    img.save(f'channel_{i}.png')

print("Images saved successfully.")