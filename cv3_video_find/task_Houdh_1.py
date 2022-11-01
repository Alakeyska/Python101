# Цель этого задания - научиться использовать функции поиска линий на практике.
#
# Для выполнения этого задания возьмите видео из задания 3 к лабораторной 5 (если вы не выполняли это задание,
# возьмите видео у однокурсников). Ваша задача - найти линию на этом видео с помощью преобразования Хафа.
# Можно найти несколько линий, которые проходят по границам полосы разметки.

import cv2
import math

def draw_line_P(x0, y0, x1, y1, img, color=(0, 0, 255), thickness=1, lineType=cv2.LINE_AA):
    cv2.line(img, (x0, y0), (x1, y1), color, thickness, lineType)

path = "road.mp4"
path_garbage = "garbage_road.mp4"
path_line = "line_video.mp4"

cap = cv2.VideoCapture(path_line)

while cap.isOpened():
    ret, frame = cap.read()
    if not ret:
        print("Can't receive frame (stream end?). Exiting ...")
        break
    frame = cv2.resize(frame, (800, 800))
    gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
    blur = cv2.GaussianBlur(gray, (15, 15), 0)
    canny = cv2.Canny(blur, 50, 100, apertureSize=3)
    lines = cv2.HoughLinesP(canny, 1, math.radians(0.5), 20, maxLineGap=30, minLineLength=50)

    if lines is not None:
        for [[x0, y0, x1, y1]] in lines:
            draw_line_P(x0, y0, x1, y1, frame, thickness=2)
    cv2.imshow("LINES", frame)
    cv2.imshow('canny', canny)
    if cv2.waitKey(25) == ord('q'):
        break
cap.release()
cv2.destroyAllWindows()

