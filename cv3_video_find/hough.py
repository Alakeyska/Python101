import cv2
import math

# IMAGE = "/Users/jetbrains/Desktop/opencv/line2.png"

# рисование линий HoughLinesP
def draw_line_P(x0, y0, x1, y1, img, color=(0, 0, 255),thickness=1, lineType=cv2.LINE_AA):
    cv2.line(img, (x0, y0), (x1, y1),color, thickness, lineType)

IMAGE = "/Users/jetbrains/Desktop/opencv/line5.png"
img = cv2.imread(IMAGE, cv2.IMREAD_COLOR) 
img_g = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
_, img_g = cv2.threshold(img_g, 127, 255, cv2.THRESH_BINARY_INV)
cv2.imshow("GRAYSCALE", img_g)

lines = cv2.HoughLinesP(img_g, 1, math.pi/2, 400)
print(lines)
print("lines:", len(lines))

for [[x0, y0, x1, y1]] in lines:
    draw_line_P(x0, y0, x1, y1, img, thickness=2)

cv2.imshow("LINES", img)

cv2.waitKey(0)

IMAGE = "/Users/jetbrains/Desktop/opencv/circle6.png"

# вывод на экран изображения
def show(name, img):
    cv2.namedWindow(name)
    cv2.imshow(name, img)

img = cv2.imread(IMAGE, cv2.IMREAD_COLOR)
A = img.shape[0]
img_g = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
img_g = cv2.GaussianBlur(img_g, (11, 11), 0)
# param1 - верхняя граница Кенни
# pamam2 - порог аккумулятора
circles = cv2.HoughCircles(img_g, cv2.HOUGH_GRADIENT, 1, minDist=(A//16 + A//8), param1=100, param2=A//16, minRadius=A//4)
print("\n", circles)
if circles is not None:
    for circle in circles[0]:
        print(circle)
        cv2.circle(img, (int(circle[0]), int(circle[1])), int(circle[2]), color=(0, 0, 255), thickness=3)

cv2.imshow("SOURCE", img)

show("SOURCE", img)

while cv2.waitKey(0) != 27:
    pass
