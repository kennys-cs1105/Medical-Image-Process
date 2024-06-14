# Medical-Image-Process

*Created by KennyS*

Processing Medical Image

---

## Introduction

1. png2video.py

- png序列转化为视频(连续帧)

2. npy_meta.py

- npy数据转化为metaimage格式, 用于可视化
- 根据npy格式 [b, z, y, x] [z, y, x]
- origin spacing等信息按需设置

3. npy_png.py

- npy数据转化为png, 可视化

4. rename_luna.py

- Rename LUNA16 dataset file name

5. make_nnunet_mask.py

- Make nnunet mask via coord_x, coord_y, coord_z, diameter
- Convert *.npy -> *.nii.gz

6. volume_metrics.py

- Calculate Volume Metrics for Medical Image
