import cv2
import mediapipe as mp
import time

cap = cv2.VideoCapture('WALK.mp4')
mpPose = mp.solutions.pose
mpDraw = mp.solutions.drawing_utils
# .Pose(static_image_mode=False, model_complexity=1, smooth_landmarks=True, enable_segmentation=False, smooth_segmentation=False, min_detection_confidence=0.5, max_tracking_confidence=0.5)
pose = mpPose.Pose()

prevTime = 0
currTime = 0

while True:
    success, img = cap.read()
    imgRGB = cv2.cvtColor(img, cv2.COLOR_BGR2RGB)
    results = pose.process(imgRGB)
    if results.pose_landmarks:
        mpDraw.draw_landmarks(img, results.pose_landmarks, mpPose.POSE_CONNECTIONS)
        for id, lm in enumerate(results.pose_landmarks.landmark):
            h, w, c = img.shape
            cx, cy = int(lm.x * w), int(lm.y * h)
            cv2.circle(img, (cx, cy), 3, (255,0,0), cv2.FILLED)

    currTime = time.time() 
    fps = 1/(currTime-prevTime)
    prevTime = currTime
    
    cv2.putText(img, str(int(fps)), (10,70), cv2.FONT_HERSHEY_PLAIN, 3, (255,0,255), 3)
    cv2.imshow('Video', img)
    key=cv2.waitKey(1)
    if key==81 or key==113:
        break