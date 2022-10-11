# Используя известные Вам фильтры, избавиться от черных точек на изображении
import cv2
import numpy as np
from matplotlib import pyplot as plt


def ShowImg(img,win_name):
    cv2.imshow(win_name, img)
    cv2.waitKey()


path = "S:\\git_intensive\\sd_course\\cv1\\filters\\img3.png"
img = cv2.imread(path, cv2.IMREAD_COLOR)

# BLUR
img_blur = cv2.blur(img, (23, 23))
ShowImg(img_blur, 'blur')
# MEDIAN FILTER
img_median = cv2.medianBlur(img, 23)
ShowImg(img_median,'median')
# GAUSSIAN
img_gaussian = cv2.GaussianBlur(img, (17, 17), 0)
ShowImg(img_gaussian,'gaussian')
# BILATERAL
img_bilateral = cv2.bilateralFilter(img, d=20, sigmaColor=90, sigmaSpace=20)
ShowImg(img_bilateral,'bilateral')

