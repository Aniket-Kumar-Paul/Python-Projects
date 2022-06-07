import cv2
import numpy as np
import time
import poseEstimationModule as pm

cap = cv2.VideoCapture("video.mp4")
prevTime = 0
detector = pm.poseDetector()
count = 0
dir = 0

while True:
    success, img = cap.read()
    #img = cv2.resize(img, (1280,720))
    img = detector.findPose(img)
    lmList = detector.findPosition(img, False)
    if len(lmList) != 0:
        # Right Arm
        angleR = detector.findAngle(img, 12,14,16)
        # Left Arm
        #detector.findAngle(img, 11,13,15)
        per = np.interp(angleR,(24,160),(0,100))

        # Check for the dumbell curls
        if per == 100:
            if dir == 0:
                count += 0.5
                dir = 1
        if per == 0:
            if dir == 1:
                count += 0.5
                dir = 0
        cv2.putText(img, str(int(count)), (50,100), cv2.FONT_HERSHEY_PLAIN, 5, (255,0,0), 5)
    currTime = time.time() 
    fps = 1/(currTime-prevTime)
    prevTime = currTime
    
    #cv2.putText(img, str(int(fps)), (10,70), cv2.FONT_HERSHEY_PLAIN, 3, (255,0,255), 3)
    cv2.imshow('Video', img)
    key=cv2.waitKey(1)
    if key==81 or key==113:
        break