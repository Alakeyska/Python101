# Найти границы и разметку
import cv2

def show_dict(dict):
    for k,v in dict.items():
        cv2.imshow(k,v)
        cv2.waitKey()
   
path_clear = "edges.PNG"
path_arrows='arrows.jpg'

img_clear = cv2.imread(path_clear, cv2.IMREAD_REDUCED_GRAYSCALE_2)
img_clear_blur = cv2.GaussianBlur(img_clear, (13, 13), 0)
canny_clear_blur = cv2.Canny(img_clear_blur, threshold1=20, threshold2=60, apertureSize=3)
clear = {'original': img_clear, 'GaussianBlur': img_clear_blur, 'Canny': canny_clear_blur}

img_arrows=cv2.imread(path_arrows, cv2.IMREAD_REDUCED_GRAYSCALE_2)
img_arrows_blur = cv2.GaussianBlur(img_arrows, (13, 13), 0)
canny_arrows_blur = cv2.Canny(img_arrows_blur, threshold1=50, threshold2=100, apertureSize=3)
arrows={'original':img_arrows,'GaussianBlur':img_arrows_blur,'Canny':canny_arrows_blur}

show_dict(clear)
show_dict(arrows)

# debug
# for x in range(10,100,1):
#     canny_arrows_blur = cv2.Canny(img_arrows_blur, threshold1=x, threshold2=x*2, apertureSize=3)
#     cv2.imshow(str(x),canny_arrows_blur)
#     if cv2.waitKey()==ord('q'):
#         break
#     cv2.destroyWindow(str(x))
