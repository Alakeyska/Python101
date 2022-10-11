# С помощью средств библиотек OpenCV и NumPy создайте изображение. На белом фоне нарисуйте:


import cv2
import numpy as np

blue_color = (255, 0, 0)
green_color = (0, 255, 0)
red_color = (0, 0, 255)
black_color = (0, 0, 0)

font = cv2.FONT_HERSHEY_SIMPLEX
fontScale = 1
text_thickness = 2
window_name = 'window1'

if __name__ == '__main__':
    img_white = np.full((480, 640, 3), (255, 255, 255), 'uint8')
   
#    окружности
    cv2.circle(img_white, (320, 100), 50, blue_color, 3)
    cv2.putText(img_white, 'circle', (380, 100), font, fontScale, black_color, text_thickness)

    cv2.circle(img_white, (320, 400), 50, blue_color, 3)
    cv2.putText(img_white, 'circle', (380, 400), font, fontScale, black_color, text_thickness)

# квадраты
    cv2.rectangle(img_white, (55, 167), (190, 302), green_color, 3)
    cv2.putText(img_white, 'square', (50, 150), font, fontScale, green_color, text_thickness)

    cv2.rectangle(img_white, (455, 167), (590, 302), green_color, 3)
    cv2.putText(img_white, 'square', (480, 350), font, fontScale, green_color, text_thickness)

    cv2.rectangle(img_white, (0, 0), (640, 480), black_color, 3)


    cv2.line(img_white, (0, 0), (640, 480), green_color, 3)
    cv2.putText(img_white, 'line', (300, 200), font, fontScale, black_color, text_thickness)

    cv2.line(img_white, (640, 0), (0, 480), red_color, 3)
    cv2.putText(img_white, 'line', (300, 200), font, fontScale, red_color, text_thickness)

    cv2.imshow(window_name, img_white)
    key = cv2.waitKey(0)
    