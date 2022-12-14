
# Используя фильтр гауса и двусторонний очистите изоображение от шума

import cv2
import numpy as np
from matplotlib import pyplot as plt


def ShowImg(img,win_name):
    cv2.imshow(win_name, img)
    cv2.waitKey()


# path = "S:\\git_intensive\\sd_course\\cv1\\filters\\img2.png"
path = "С:\\work\\img2.PNG"

img = cv2.imread(path, cv2.IMREAD_REDUCED_COLOR_2)

# GAUS
img_gauss = cv2.GaussianBlur(img, (11, 11), 0)
# BILATERAL
img_bilateral = cv2.bilateralFilter(img, d=6, sigmaColor=60, sigmaSpace=60)
ShowImg(img_gauss,'gauss')
ShowImg(img_bilateral,'bilateral')
ShowImg(img,'orig')


# for i in range(40):
#     x = i*10
#     img_bilateral = cv2.bilateralFilter(img, d=20, sigmaColor=x, sigmaSpace=x)
#     cv2.imshow(str(i),img_bilateral)
#     if cv2.waitKey() == ord('q'):
#         break
    
