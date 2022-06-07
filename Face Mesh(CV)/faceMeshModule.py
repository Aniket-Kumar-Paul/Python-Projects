import cv2
import mediapipe as mp
import time

class FaceMeshDetector:
    def __init__(self, mode=False, maxFace=2, rflm=False, detCon=0.5, tracCon=0.5):
        self.mode = mode
        self.maxFace = maxFace
        self.rflm = rflm
        self.detCon = detCon
        self.tracCon = tracCon

        self.mpFaceMesh = mp.solutions.face_mesh
        self.mpDraw = mp.solutions.drawing_utils
        self.faceMesh = self.mpFaceMesh.FaceMesh(self.mode,self.maxFace,self.rflm,self.detCon,self.tracCon)
        self.drawSpec = self.mpDraw.DrawingSpec(thickness=1, circle_radius=1, color=(255, 0, 255))

    def findFaceMesh(self, img, draw=True):
        self.imgRGB = cv2.cvtColor(img, cv2.COLOR_BGR2RGB)
        self.results = self.faceMesh.process(self.imgRGB)
        faces=[] 
        if self.results.multi_face_landmarks:
            for faceLms in self.results.multi_face_landmarks:
                if draw:
                    self.mpDraw.draw_landmarks(img, faceLms, self.mpFaceMesh.FACEMESH_CONTOURS, self.drawSpec, self.drawSpec)
                face=[]
                for id,lm in enumerate(faceLms.landmark):
                    h, w, c = img.shape
                    x, y = int(lm.x*w), int(lm.y*h)
                    cv2.putText(img, str(id), (x, y), cv2.FONT_HERSHEY_PLAIN, 0.5, (0,255,0), 1)
                    face.append([id, x, y])
                faces.append(face)
        return img, faces
        
def main():
    cap = cv2.VideoCapture(0)
    ptime = 0
    detector = FaceMeshDetector()
    while True:
        success, img = cap.read()
        img, faces = detector.findFaceMesh(img)
        if(len(faces)!=0):
            print(len(faces))
        ctime = time.time()
        fps = 1/(ctime-ptime)
        ptime = ctime
        cv2.putText(img, f'FPS: {int(fps)}', (20, 70), cv2.FONT_HERSHEY_PLAIN, 3, (0,255,0), 2)

        cv2.imshow("Image", img)
        key=cv2.waitKey(1)
        if key==81 or key==113:
            break

if __name__ == "__main__":
    main()