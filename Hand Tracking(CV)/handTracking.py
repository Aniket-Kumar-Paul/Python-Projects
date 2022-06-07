import cv2
import mediapipe as mp
import time

cap = cv2.VideoCapture(0)

mpHands = mp.solutions.hands
# .Hands(static_image_mode=False, max_num_hands=2, complexity=1, min_detection_confidence=0.5, min_tracking_confidence=0.5)
# Initializes a mediapipe hand object
# static_image_mode=False => both tracking and detection(if confidence of tracking is below min. then do detection), True=> only detection
hands = mpHands.Hands()
mpDraw = mp.solutions.drawing_utils #to draw the lines between the points

prevTime = 0
currTime = 0

while True:
    success, img = cap.read()
    imgRGB = cv2.cvtColor(img, cv2.COLOR_BGR2RGB)
    results = hands.process(imgRGB)
    # prints x,y,z coordinates if hand detected else returns none
    #print(results.multi_hand_landmarks)
    
    if results.multi_hand_landmarks:
        for handLms in results.multi_hand_landmarks: #can be multiple hands, draw for each hand
            for id, lm in enumerate(handLms.landmark):
                # id-> 0 to 20(21 points in the hand) , lm-> x,y,z location in decimals(positions of the points)
                height, width, channels = img.shape
                cx, cy = int(lm.x * width), int(lm.y * height) #getting the positions as pixels
                print(id, cx, cy)
                if id==0: #the bottom most point
                    cv2.circle(img, (cx, cy), 25, (255, 0, 255), cv2.FILLED)

            mpDraw.draw_landmarks(img, handLms, mpHands.HAND_CONNECTIONS) 
    
    currTime = time.time() 
    fps = 1/(currTime-prevTime)
    prevTime = currTime

    cv2.putText(img, str(int(fps)), (10,70), cv2.FONT_HERSHEY_PLAIN, 3, (255,0,255), 3)

    cv2.imshow("Image", img)
    key=cv2.waitKey(1)
    if key==81 or key==113:
        break