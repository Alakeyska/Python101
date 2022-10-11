# Используя любое изображение. Напишите программу, которая будет выводить изображение на экран следующим образом:
# в цвете в полном размере на 5 секунд, затем закрыть;
# в оттенках серого в полном размере на 7 секунд, затем закрыть;
# в цвете в 2 раза меньше, чем исходный размер, на 9 секунд, затем закрыть;
# в оттенках серого в 4 раза меньше, чем исходный размер, на 11 секунд, затем закрыть.


import cv2

path = 'S:\\git_intensive\\sd_course\\cv1\\image.jpg'
window_name = 'window1'

if __name__ == '__main__':
    img = cv2.imread(path, flags=cv2.IMREAD_COLOR)
    cv2.imshow(window_name, img)
    key = cv2.waitKey(500)

    img = cv2.imread(path, flags=cv2.IMREAD_GRAYSCALE)
    cv2.imshow(window_name, img)
    key = cv2.waitKey(700)

    img = cv2.imread(path, flags=cv2.IMREAD_REDUCED_COLOR_2)
    cv2.imshow(window_name, img)
    key = cv2.waitKey(900)
    #
    img = cv2.imread(path, flags=cv2.IMREAD_REDUCED_GRAYSCALE_4)
    cv2.imshow(window_name, img)
    key = cv2.waitKey(1100)