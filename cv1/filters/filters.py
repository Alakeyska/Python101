import cv2

IMAGE = "S:\\git_intensive\\sd_course\\cv1\\filters\\test_filters.jpg"

# img_grayscale = cv2.imread(IMAGE, cv2.IMREAD_REDUCED_GRAYSCALE_2)
# cv2.imshow("IMAGE", img_grayscale)
# img_blur = cv2.blur(img_grayscale, (11, 11))
# cv2.imshow("BLUR", img_blur)


# img_median = cv2.medianBlur(img_grayscale, 11)
# cv2.imshow("MEDIAN", img_median)

IMAGE_2 = "S:\\git_intensive\\sd_course\\cv1\\filters\\dots.JPG"
img_grayscale_median = cv2.imread(IMAGE_2, cv2.IMREAD_REDUCED_GRAYSCALE_2)
img_dots_median = cv2.medianBlur(img_grayscale_median, 3)
cv2.imshow("DOTS_MEDIAN", img_grayscale_median)
cv2.imshow("DOTS", img_dots_median)

# img_gauss = cv2.GaussianBlur(img_grayscale, (3, 3), 0)
# cv2.imshow("GAUSS", img_gauss)

# img_bilateral = cv2.bilateralFilter(img_grayscale, d=50, sigmaColor=50, sigmaSpace=50)
# cv2.imshow("BILATERAL", img_bilateral)


cv2.waitKey(0)