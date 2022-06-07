import cv2
import time
import mediapipe as mp
import handTrackingmodule as htm

cap = cv2.VideoCapture(0)
prevTime = 0
currTime = 0
detector = htm.handDetector()
while True:
    success, img = cap.read()
    img = detector.findHands(img)
    lmList = detector.findPosition(img)
    if len(lmList) != 0 :
        print(lmList[4]) #4->thumb
    currTime = time.time() 
    fps = 1/(currTime-prevTime)
    prevTime = currTime

    cv2.putText(img, str(int(fps)), (10,70), cv2.FONT_HERSHEY_PLAIN, 3, (255,0,255), 3)

    cv2.imshow("Image", img)
    key = cv2.waitKey(1)
    if key==81 or key==113:
        break