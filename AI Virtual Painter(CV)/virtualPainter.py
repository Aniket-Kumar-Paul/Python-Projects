import cv2
import numpy as np
import time
import os
import handTrackingmodule as htm

folderPath = "header"
myList = os.listdir(folderPath)
overlayList = []
for imPath in myList:
    image = cv2.imread(f'{folderPath}/{imPath}')
    overlayList.append(image)
header = overlayList[0]
drawColor = (255,255,255)
brushThickness = 10
eraserThickness = 100

cap = cv2.VideoCapture(0)
cap.set(3,1280)
cap.set(4,720)

prevTime = 0
detector = htm.handDetector(detectionCon=0.8)
xp, yp = 0, 0
imgCanvas = np.zeros((720, 1280, 3), np.uint8)

while True:
    success, img = cap.read()
    img = cv2.flip(img, 1)
    img[0:125, 0:1280] = header
    img = detector.findHands(img)
    lmList = detector.findPosition(img,draw=False)
    
    if len(lmList) != 0:
        x1,y1 = lmList[8][1:]  #tip of index finger
        x2,y2 = lmList[12][1:] #tip of middle finger

        fingers = detector.fingersUp()
        
        if fingers[1] and fingers[2]: #Select
            xp, yp = 0, 0
            if y1<125: #Header region
                if 320<x1<480:
                    header = overlayList[0]
                    drawColor = (255,255,255)
                elif 485<x1<640:
                    header = overlayList[1]
                    drawColor = (0,0,255)
                elif 645<x1<800:
                    header = overlayList[2]
                    drawColor = (0,255,0)
                elif 805<x1<960:
                    header = overlayList[3]
                    drawColor = (255,0,0)
                elif 965<x1<1120:
                    header = overlayList[4]
                    drawColor = (0,0,0)
            cv2.rectangle(img, (x1-5,y1-25),(x2+5,y2+25),drawColor,cv2.FILLED)
            
        if fingers[1] and fingers[2]==False: #Draw
            cv2.circle(img,(x1,y1),10,drawColor,cv2.FILLED)
            if xp==0 and yp==0:
                xp, yp = x1, y1
            
            if drawColor==(0,0,0):
                cv2.line(img, (xp,yp), (x1,y1), drawColor, eraserThickness)
                cv2.line(imgCanvas, (xp,yp), (x1,y1), drawColor, eraserThickness)
            else:
                cv2.line(img, (xp,yp), (x1,y1), drawColor, brushThickness)
                cv2.line(imgCanvas, (xp,yp), (x1,y1), drawColor, brushThickness)
            xp, yp = x1, y1

    imgGray = cv2.cvtColor(imgCanvas, cv2.COLOR_BGR2GRAY)
    _, imgInv = cv2.threshold(imgGray, 58, 255, cv2.THRESH_BINARY_INV)
    imgInv = cv2.cvtColor(imgInv, cv2.COLOR_GRAY2BGR)
    img = cv2.bitwise_and(img, imgInv)
    img = cv2.bitwise_or(img, imgCanvas)

    currTime = time.time() 
    fps = 1/(currTime-prevTime)
    prevTime = currTime
    cv2.putText(img, str(int(fps)), (10,70), cv2.FONT_HERSHEY_PLAIN, 3, (255,0,255), 3)
    #cv2.addWeighted(img,0.5,imgCanvas,0.5,0)
    cv2.imshow("Image", img)
    #cv2.imshow("Canvas", imgCanvas)
    key = cv2.waitKey(1)
    if key==81 or key==113:
        break