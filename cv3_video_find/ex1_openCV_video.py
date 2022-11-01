
import cv2
Path="C:\\Users\\Katya\\Desktop\\course2022\\test_video_cut.mp4"
cap = cv2.VideoCapture(Path)
i = 0
 
while(cap.isOpened()):
    ret, frame = cap.read()

    if ret == False:
        break
    
    cv2.imwrite('Frame'+str(i)+'.jpg', frame)
    i += 1

cap.release()
cv2.destroyAllWindows()