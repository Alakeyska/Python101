
# Возьмите любое цветное изображение и представьте его в оттенках серого размера, уменьшенного в 4 раза. По нажатию на клавишу «s» должно выполняться сохранение нового изображения в формате .png, а по нажатию на клавишу «m» - закрытие всех окон.

import cv2

path = 'S:\\git_intensive\\sd_course\\cv1\\image.jpg'
new_path='S:\\git_intensive\\sd_course\\cv1\\image_new.png'

img=cv2.imread(path,cv2.IMREAD_REDUCED_GRAYSCALE_2)
cv2.imshow('win1',img)
while True:
    key = cv2.waitKey()
    if key == ord('s'):
        res=cv2.imwrite(new_path,img)
    elif key == ord('m'):
        print('Good bye!')
        break