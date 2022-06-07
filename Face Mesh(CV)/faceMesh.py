import cv2
import mediapipe as mp
import time

cap = cv2.VideoCapture(0)
ptime = 0

mpFaceMesh = mp.solutions.face_mesh
mpDraw = mp.solutions.drawing_utils
# .FaceMesh(static_image_mode=False, max_num_face=1, refine_landmarks=False, min_detection_confidence=0.5, min_tracking_confidence=0.5)
faceMesh = mpFaceMesh.FaceMesh(max_num_faces=2)
drawSpec = mpDraw.DrawingSpec(thickness=1, circle_radius=1, color=(255, 0, 255))

while True:
    success, img = cap.read()
    imgRGB = cv2.cvtColor(img, cv2.COLOR_BGR2RGB)
    results = faceMesh.process(imgRGB)

    if results.multi_face_landmarks:
        for faceLms in results.multi_face_landmarks:
            mpDraw.draw_landmarks(img, faceLms, mpFaceMesh.FACEMESH_CONTOURS, drawSpec, drawSpec)
            for id,lm in enumerate(faceLms.landmark):
                h, w, c = img.shape
                x, y = int(lm.x*w), int(lm.y*h)

    ctime = time.time()
    fps = 1/(ctime-ptime)
    ptime = ctime
    cv2.putText(img, f'FPS: {int(fps)}', (20, 70), cv2.FONT_HERSHEY_PLAIN, 3, (0,255,0), 2)

    cv2.imshow("Image", img)
    key=cv2.waitKey(1)
    if key==81 or key==113:
        break