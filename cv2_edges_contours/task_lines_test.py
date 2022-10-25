import cv2
path='3.png'
img=cv2.imread(path,cv2.IMREAD_COLOR)
cv2.imshow('orig',img)
cv2.waitKey()
img_g=cv2.imread(path,cv2.IMREAD_GRAYSCALE)
_,img_t=cv2.threshold(img_g,100,255,cv2.THRESH_BINARY_INV)
cv2.imshow('thrash',img_t)
cv2.waitKey()


contours, hierarchy = cv2.findContours(img_t, cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_NONE)
cv2.drawContours(img,contours,-1, (0,255,0),3)
cv2.imshow('orig',img)
cv2.waitKey()