# Используя известные Вам фильтры, избавиться от черных точек на изображении
import cv2
import numpy as np
from matplotlib import pyplot as plt


def ShowImg(img,win_name):
    cv2.imshow(win_name, img)
    cv2.waitKey()


path = "S:\\git_intensive\\sd_course\\cv1\\filters\\img1.png"
img = cv2.imread(path, cv2.IMREAD_COLOR)

# BLUR
img_blur = cv2.blur(img, (13, 13))
ShowImg(img_blur, 'blur')
# MEDIAN FILTER
img_median = cv2.medianBlur(img, 11)
ShowImg(img_median,'median')
# GAUSSIAN
img_gaussian = cv2.GaussianBlur(img, (17, 17), 0)
ShowImg(img_gaussian,'gaussian')
# BILATERAL
img_bilateral = cv2.bilateralFilter(img, d=20, sigmaColor=90, sigmaSpace=20)
ShowImg(img_bilateral,'bilateral')


# for i in range(20):
#     x=i*10
#     # img_median = cv2.medianBlur(img, x, 0)
#     img_bilateral = cv2.bilateralFilter(img, d=20, sigmaColor=x, sigmaSpace=x)
    
#     ShowImg(img_bilateral,'bila')