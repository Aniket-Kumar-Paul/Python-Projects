import cv2
import numpy as np
import handTrackingmodule as htm
import time
import autopy

wCam, hCam = 640, 480
frameR = 100 # Frame Reduction
smoothening = 7

cap = cv2.VideoCapture(0)
cap.set(3, wCam)
cap.set(3, hCam)
wScr, hScr = autopy.screen.size()

prevTime = 0
plocX, plocY = 0, 0
clocX, clocY = 0, 0

detector = htm.handDetector(maxHands=1)
while True:
    # Find hand landmarks
    success, img = cap.read()
    img = detector.findHands(img)
    lmList, bbox = detector.findPosition(img,draw=False)
   
    # Get tip of index and middle fingers
    if len(lmList) != 0 :
        x1, y1 = lmList[8][1:]
        x2, y2 = lmList[12][1:]
        
        # check which fingers are up
        fingers = detector.fingersUp()
        
        cv2.rectangle(img, (frameR, frameR), (wCam-frameR, hCam-frameR), (255,0,255), 2)
            
        # only index finger : moving mode
        if fingers[1] and fingers[2]==0:
            # Convert coordinates
            x3 = np.interp(x1, (frameR,wCam-frameR), (0,wScr))
            y3 = np.interp(y1, (frameR,hCam-frameR), (0,hScr))
            
            # smoothen values
            clocX = plocX + (x3-plocX)/smoothening
            clocY = plocY + (y3-plocY)/smoothening

            # Move Mouse
            autopy.mouse.move(wScr-x3,y3)
            cv2.circle(img, (x1, y1), 15, (255, 0, 255), cv2.FILLED)
            plocX, plocY = clocX, clocY

    # Both Index and middle fingers are up : Clicking mode
    if fingers[1] and fingers[2]:
        # Find distance between fingers
        length, img, lineInfo = detector.findDistance(8, 12, img)
        if length<40:
            cv2.circle(img, (lineInfo[4], lineInfo[5]), 15, (255, 0, 255), cv2.FILLED)
             # click mouse if distance short
            autopy.mouse.click()

    # fps
    currTime = time.time() 
    fps = 1/(currTime-prevTime)
    prevTime = currTime
    cv2.putText(img, str(int(fps)), (10,70), cv2.FONT_HERSHEY_PLAIN, 3, (255,0,255), 3)
    
    cv2.imshow("Image", img)
    cv2.waitKey(1)