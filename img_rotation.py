from PIL import Image
import os,shutil

# im.transpose(Image.ROTATE_180)
# Image.FLIP_LEFT_RIGHT,表示将图像左右翻转
# Image.FLIP_TOP_BOTTOM,表示将图像上下翻转
# Image.ROTATE_90,表示将图像逆时针旋转90°
# Image.ROTATE_180,表示将图像逆时针旋转180°
# Image.ROTATE_270,表示将图像逆时针旋转270°
# Image.TRANSPOSE,表示将图像进行转置(相当于顺时针旋转90°)
# Image.TRANSVERSE,表示将图像进行转置,再水平翻转
print(''
                      '########图像旋转方式#########\n'
                      '1：图像左右镜像\n'
                      '2：图像上下镜像\n'
                      '3：图像逆时针旋转90°\n'
                      '4：图像逆时针旋转180°\n'
                      '5：图像逆时针旋转270°\n'
                      '#############################\n'
                      '说明：通过数字选择菜单 \n')
xz=int(input('请选择选择方式：'))
def circle(srcPath,dstPath):
    for filename in os.listdir(srcPath):
        #如果不存在目的目录则创建一个，保持层级结构
        if not os.path.exists(dstPath):
                os.makedirs(dstPath)

        #拼接完整的文件或文件夹路径
        srcFile=os.path.join(srcPath,filename)
        dstFile=os.path.join(dstPath,filename)
 
        # 如果是文件就处理
        if os.path.isfile(srcFile):
            try:
                sImg=Image.open(srcFile)
                if xz==1:
                    ss=sImg.transpose(Image.FLIP_LEFT_RIGHT)
                elif xz==2:
                    ss=sImg.transpose(Image.FLIP_TOP_BOTTOM)
                elif xz==3:
                    ss=sImg.transpose(Image.ROTATE_90)
                elif xz==4:
                    ss=sImg.transpose(Image.ROTATE_180)
                elif xz==5:
                    ss=sImg.transpose(Image.ROTATE_270) 
                ss.save(dstFile)
                print(dstFile+" 转换成功！")
            except Exception:
                print(dstFile+"失败！")
        if os.path.isdir(srcFile):
            circle(srcFile, dstFile)

if __name__ == '__main__':
    # 遍历待加入图片
    dirss=input('请输入图片所在文件夹：')
    dirss2=input('请输入压缩后图片输出文件夹：')
    circle(dirss, dirss2)
