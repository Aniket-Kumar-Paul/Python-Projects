import cv2
import mediapipe as mp
import time

cap = cv2.VideoCapture(0)
ptime = 0

mpFaceDetection = mp.solutions.face_detection
mpDraw = mp.solutions.drawing_utils
faceDetection = mpFaceDetection.FaceDetection(min_detection_confidence=0.75) #default is 0.5

while True:
    success, img = cap.read()
    imgRGB = cv2.cvtColor(img, cv2.COLOR_BGR2RGB)
    results = faceDetection.process(imgRGB)

    if results.detections:
        for id, detection in enumerate(results.detections): #multiple faces iteration, id 0 => face 1 and so on..
            #mpDraw.draw_detection(img, detection) -> will draw rectangle as well as eye, nose etc points 
            #print(id, detection)
            #print(detection.score) -> accuracy of detection
            #print(detection.location_data.relative_bounding_box) -> xmin, ymin, width, height
            h, w, c = img.shape
            bboxC = detection.location_data.relative_bounding_box
            bbox = int(bboxC.xmin * w), int(bboxC.ymin * h), \
                int(bboxC.width * w), int(bboxC.height * h)
            cv2.rectangle(img, bbox, (255, 0, 255), 2)
            cv2.putText(img, f'{int(detection.score[0]*100)}%', (bbox[0], bbox[1]-20), cv2.FONT_HERSHEY_PLAIN, 2, (0,255,255), 1)

    ctime = time.time()
    fps = 1/(ctime-ptime)
    ptime = ctime
    cv2.putText(img, f'FPS: {int(fps)}', (20, 70), cv2.FONT_HERSHEY_PLAIN, 3, (0,255,0), 2)

    cv2.imshow("Image", img)
    key=cv2.waitKey(1)
    if key==81 or key==113:
        break