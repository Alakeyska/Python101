# <<<---------------------------------------------------------------------------->>>
# Threshold 1
# import cv2
# from matplotlib import pyplot as plt

# PATH = "lab2-1.jpg"
# # path = "grayscale.jpg"
# PATH = 'cat.png'

# i = 0
# img = cv2.imread(PATH, flags=cv2.IMREAD_REDUCED_GRAYSCALE_2)
# # manual
# ret, thresh1 = cv2.threshold(img, 127, 255, cv2.THRESH_BINARY)
# ret, thresh2 = cv2.threshold(img, 127, 255, cv2.THRESH_BINARY_INV)
# ret, thresh3 = cv2.threshold(img, 127, 255, cv2.THRESH_TRUNC)
# ret, thresh4 = cv2.threshold(img, 127, 255, cv2.THRESH_TOZERO)
# ret, thresh5 = cv2.threshold(img, 127, 255, cv2.THRESH_TOZERO_INV)
# # auto
# ret_otsu, thresh6 = cv2.threshold(img, 111, 255, cv2.THRESH_OTSU)
# ret_triangle, thresh7 = cv2.threshold(img, 111, 255, cv2.THRESH_TRIANGLE)

# cv2.imshow('orig', img)
# cv2.imshow('thresh6', thresh6)
# cv2.imshow('thresh7', thresh7)

# print(ret_otsu)
# cv2.waitKey(0)

# <<<---------------------------------------------------------------------------->>>
# Threshold 2

# import cv2
# from matplotlib import pyplot as plt

# path = 'emoji.jpg'
# i = 0
# img = cv2.imread(path, flags=cv2.IMREAD_REDUCED_GRAYSCALE_4)
# adaptive1 = cv2.adaptiveThreshold(img, 255, cv2.ADAPTIVE_THRESH_MEAN_C, cv2.THRESH_BINARY, 13, 5)
# adaptive2 = cv2.adaptiveThreshold(img, 255, cv2.ADAPTIVE_THRESH_GAUSSIAN_C, cv2.THRESH_BINARY, 21, 4)
# ret, thresh = cv2.threshold(img, 127, 255, cv2.THRESH_BINARY)

# cv2.imshow('orig', img)
# cv2.imshow('adaptive1', adaptive1)
# cv2.imshow('adaptive2', adaptive2)
# cv2.imshow('binary', thresh)
# cv2.waitKey(0)

# <<<---------------------------------------------------------------------------->>>
# Canny
# Найти границы и разметку
# import cv2

# path_clear = "edges.PNG"
# path_arrows='arrows.jpg'

# img_arrows=cv2.imread(path_arrows, cv2.IMREAD_GRAYSCALE)
# img_arrows_blur = cv2.GaussianBlur(img_arrows, (13, 13), 0)
# canny_arrows_blur = cv2.Canny(img_arrows_blur, threshold1=50, threshold2=150, apertureSize=3)


# cv2.imshow('img_clear',img_arrows)
# cv2.imshow('img_clear_blur',img_arrows_blur)
# cv2.imshow('canny_clear_blur',canny_arrows_blur)
# cv2.waitKey(0)

# <<<---------------------------------------------------------------------------->>>
# Контуры
import cv2
path='figures.png'
img=cv2.imread(path,cv2.IMREAD_COLOR)
# cv2.imshow('orig',img)
# cv2.waitKey()

img_g=cv2.imread(path,cv2.IMREAD_GRAYSCALE)
_,img_t=cv2.threshold(img_g,100,255,cv2.THRESH_BINARY_INV)
# cv2.imshow('thrash',img_t)
# cv2.waitKey()


contours, hierarchy = cv2.findContours(img_t, cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_NONE)
# cv2.drawContours(img,contours,1, (0,255,0),3)
for idx, countur in enumerate(contours):
    x, y, w, h = cv2.boundingRect(countur)
    arcL = cv2.arcLength(countur, True)
    s = cv2.contourArea(countur)
    print(x,y,w,h)
    print(arcL)
    print(s)
    cv2.drawContours(img,contours,idx, (0,255,0),3)
    cv2.imshow('orig',img)
    cv2.waitKey()
    print('\n\n\n\n')
