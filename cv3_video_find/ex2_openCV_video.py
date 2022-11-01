import cv2
import numpy as np

Path="C:\\Users\\Katya\\Desktop\\course2022\\test_video_forEx3.mp4"
vid = cv2.VideoCapture(Path)

while True:
 
    _, frame = vid.read()
 
    cv2.imshow("frame", frame)

    b = frame[:, :, 0]
    g = frame[:, :, 1]
    r = frame[:, :, 2]
 
    # computing the mean
    b_mean = np.mean(b)
    g_mean = np.mean(g)
    r_mean = np.mean(r)
 
    if (b_mean > g_mean and b_mean > r_mean):
        print("Blue")
    if (g_mean > r_mean and g_mean > b_mean):
        print("Green")
    else:
        print("Red")

    if cv2.waitKey(1) == 27:
        break

vid.release()
cv2.destroyAllWindows