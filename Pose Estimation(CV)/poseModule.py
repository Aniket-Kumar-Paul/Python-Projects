import cv2
import mediapipe as mp
import time

class poseDetector:
    def __init__(self, mode=False, complexity=1, smooth_lm=True, enSegment=False, smSegment=True, detCon=0.5, TraCon=0.5):
        self.mode = mode
        self.complexity = complexity
        self.smooth_lm = smooth_lm
        self.enSegment = enSegment
        self.smSegment = smSegment
        self.detCon = detCon
        self.TraCon = TraCon

        self.mpPose = mp.solutions.pose
        self.mpDraw = mp.solutions.drawing_utils
        self.pose = self.mpPose.Pose(self.mode, self.complexity, self.smooth_lm, self.enSegment, self.smSegment, self.detCon, self.TraCon)

    def findPose(self, img, draw=True):
        imgRGB = cv2.cvtColor(img, cv2.COLOR_BGR2RGB)
        self.results = self.pose.process(imgRGB)
        if self.results.pose_landmarks:
            if draw:
                self.mpDraw.draw_landmarks(img, self.results.pose_landmarks, self.mpPose.POSE_CONNECTIONS)
        return img
    
    def findPosition(self, img, draw=True):
        lmList = []
        if self.results.pose_landmarks:
            for (id, lm) in enumerate(self.results.pose_landmarks.landmark):
                h, w, c = img.shape
                cx, cy = int(lm.x * w), int(lm.y * h)
                lmList.append([id, cx, cy])
                if draw:
                    cv2.circle(img, (cx, cy), 3, (255,0,0), cv2.FILLED)
        return lmList

def main():
    cap = cv2.VideoCapture('WALK.mp4')
    prevTime = 0
    detector = poseDetector()
    while True:
        success, img = cap.read()
        img = detector.findPose(img)
        lmList = detector.findPosition(img)
        # Tracking right elbow
        if len(lmList) != 0:
            print(lmList[14])
            cv2.circle(img, (lmList[14][1], lmList[14][2]), 10, (0, 0, 255), cv2.FILLED)

        currTime = time.time() 
        fps = 1/(currTime-prevTime)
        prevTime = currTime
    
        cv2.putText(img, str(int(fps)), (10,70), cv2.FONT_HERSHEY_PLAIN, 3, (255,0,255), 3)
        cv2.imshow('Video', img)
        key=cv2.waitKey(1)
        if key==81 or key==113:
            break

if __name__ == "__main__":
    main()