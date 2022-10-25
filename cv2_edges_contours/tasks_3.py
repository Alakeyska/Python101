# 3----4

import numpy as np
import cv2
img = "C:\\Users\\Katya\\Desktop\\course2022\\5-2.jpg"
img2 = cv2.imread(img, cv2.IMREAD_GRAYSCALE)
cv2.imshow("image2", img2)
pic2=cv2.medianBlur(img2, 17)
cv2.imshow("image3", pic2)
pic3 = cv2.GaussianBlur(pic2, (5, 5), 7)
cv2.imshow("image4", pic3)
edges2 = cv2.Canny(img2, 11,20, 3)
cv2.imshow("image6", edges2)
k = cv2.waitKey(0)
if k == ord('m'): # Дождаться выхода ключа ESC
    cv2.destroyAllWindows()

# 2----

import cv2
image_text = "C:\\Users\\Katya\\Desktop\\COMPUTER VISION\\lr2\\text_cat.jpg"
image = cv2.imread(image_text, cv2.IMREAD_REDUCED_GRAYSCALE_2)
new_image1=cv2.adaptiveThreshold(image, 255, cv2.ADAPTIVE_THRESH_MEAN_C,
cv2.THRESH_BINARY, 11, 21)
new_image2=cv2.adaptiveThreshold(image, 255, cv2.ADAPTIVE_THRESH_GAUSSIAN_C,
cv2.THRESH_BINARY, 11, 8)
cv2.imshow("text", image)
cv2.imshow("adaptive image MEAN", new_image1)
cv2.imshow("adaptive image GAUSSIAN", new_image2)
cv2.waitKey(0)

# 1----

import cv2
# write in terminal
# python -m pip install -U pip
# python -m pip install -U matplotlib
from matplotlib import pyplot as plt
image = "C:\\Users\\Katya\\Desktop\\COMPUTER VISION\\lr2\\katinka.jpg"
image2 = "C:\\Users\\Katya\\Desktop\\COMPUTER VISION\\lr2\\katinka2.jpg"
img=cv2.imread(image, cv2.IMREAD_REDUCED_GRAYSCALE_2)
img2=cv2.imread(image2, cv2.IMREAD_REDUCED_GRAYSCALE_2)
ret_1, img_1 = cv2.threshold(img, 120, 255, cv2.THRESH_BINARY)
ret_2, img_2 = cv2.threshold(img, 120, 255, cv2.THRESH_BINARY_INV)
ret_3, img_3 = cv2.threshold(img, 66, 255, cv2.THRESH_TOZERO)
ret_4, img_4 = cv2.threshold(img, 66, 255, cv2.THRESH_TOZERO_INV)
ret_5, img_5 = cv2.threshold(img, 255, 255, cv2.THRESH_TRIANGLE)
ret_6, img_6 = cv2.threshold(img, 0, 255, cv2.THRESH_OTSU)
img_a_1 = cv2.adaptiveThreshold(img2, 255, cv2.ADAPTIVE_THRESH_GAUSSIAN_C,
cv2.THRESH_BINARY, 11, 9)
img_a_2 = cv2.adaptiveThreshold(img2, 255, cv2.ADAPTIVE_THRESH_MEAN_C,
cv2.THRESH_BINARY, 11, 9)
images1 = [img, img_1, img_2, img_3, img_4, img_5, img_6]
titles = ['Original Image','BINARY','BINARY INV',
'TOZERO','TOZERO INV','TRIANGLE','OTSU']
for i in range(7):
    plt.subplot(2,4, i+1)
    plt.imshow(images1[i], 'gray')
    plt.title(titles[i])
    plt.xticks([]),plt.yticks([])
plt.show()
print(ret_1, ret_2, ret_3, ret_4, ret_5, ret_6)
# cv2.imshow("result window", img)
# adaptive image
# cv2.imshow("result window", img2)
# cv2.imshow("result window 1", img_1)
# cv2.imshow("result window 2", img_2)
# cv2.imshow("result window 3", img_3)
# cv2.imshow("result window 4", img_4)
# cv2.imshow("result window 5", img_5)
# cv2.imshow("result window 6", img_6)
images2 = [img2, img_a_1, img_a_2]
titles2 = ['Original Image','THRESH GAUSSIAN C','THRESH MEAN C']
for i in range(3):
    plt.subplot(1,3, i+1)
    plt.imshow(images2[i], 'gray')
    plt.title(titles2[i])
    plt.xticks([]),plt.yticks([])
plt.show()
# cv2.imshow("result window 7", img_a_1)
# cv2.imshow("result window 8", img_a_2)
# cv2.waitKey(0)