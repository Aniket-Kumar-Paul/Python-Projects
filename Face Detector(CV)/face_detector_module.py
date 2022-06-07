import cv2
import mediapipe as mp
import time

class FaceDetector:
    def __init__(self, minDetectionCon=0.5):
        self.minDetectionCon = minDetectionCon
        self.mpFaceDetection = mp.solutions.face_detection
        self.mpDraw = mp.solutions.drawing_utils
        self.faceDetection = self.mpFaceDetection.FaceDetection(self.minDetectionCon)

    def findFaces(self, img, draw=True):
        imgRGB = cv2.cvtColor(img, cv2.COLOR_BGR2RGB)
        self.results = self.faceDetection.process(imgRGB)
        bboxs = []
        if self.results.detections:
            for id, detection in enumerate(self.results.detections):
                h, w, c = img.shape
                bboxC = detection.location_data.relative_bounding_box
                bbox = int(bboxC.xmin * w), int(bboxC.ymin * h), \
                    int(bboxC.width * w), int(bboxC.height * h)
                bboxs.append([id, bbox, detection.score])
                #cv2.rectangle(img, bbox, (255, 0, 255), 2)
                if draw:
                    img = self.fancyDraw(img, bbox)
                cv2.putText(img, f'{int(detection.score[0]*100)}%', (bbox[0], bbox[1]-20), cv2.FONT_HERSHEY_PLAIN, 2, (0,255,255), 1) 
        return img, bboxs

    def fancyDraw(self, img, bbox, l=30, t=3, rt=1):
        x, y, w, h = bbox
        x1, y1 = x+w, y+h

        cv2.rectangle(img, bbox, (255, 0, 255), rt)
        #Top Left
        cv2.line(img, (x,y), (x+l,y), (255,0,255), t)
        cv2.line(img, (x,y), (x,y+l), (255,0,255), t)
        #Top Right
        cv2.line(img, (x1,y), (x1-l,y), (255,0,255), t)
        cv2.line(img, (x1,y), (x1,y+l), (255,0,255), t)
        #Bottom Left
        cv2.line(img, (x,y1), (x+l,y1), (255,0,255), t)
        cv2.line(img, (x,y1), (x,y1-l), (255,0,255), t)
        #Bottom Right
        cv2.line(img, (x1,y1), (x1-l,y1), (255,0,255), t)
        cv2.line(img, (x1,y1), (x1,y1-l), (255,0,255), t)
        return img

def main():
    cap = cv2.VideoCapture(0)
    ptime = 0
    detector = FaceDetector()
    while True:
        success, img = cap.read()
        img, bboxs = detector.findFaces(img)
        print(bboxs)

        ctime = time.time()
        fps = 1/(ctime-ptime)
        ptime = ctime
        cv2.putText(img, f'FPS: {int(fps)}', (20, 70), cv2.FONT_HERSHEY_PLAIN, 3, (0,255,0), 2)

        cv2.imshow("Image", img)
        key=cv2.waitKey(1)
        if key==81 or key==113:
            break

if __name__=="__main__":
    main()