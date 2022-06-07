import cv2

car_tracker = cv2.CascadeClassifier('cars.xml')
pedestrian_tracker = cv2.CascadeClassifier('haarcascade_fullbody.xml')
video = cv2.VideoCapture('video.mp4')

while True:
    successfull_frame_read, frame = video.read()

    if successfull_frame_read:
        grayscaled_frame = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
    else:
        break
    
    cars = car_tracker.detectMultiScale(grayscaled_frame)
    pedestrians = pedestrian_tracker.detectMultiScale(grayscaled_frame)
    
    for (x, y, w, h) in cars:
        cv2.rectangle(frame, (x, y), (x+w, y+h), (0, 0, 255), 2)
    
    for (x, y, w, h) in pedestrians:
        cv2.rectangle(frame, (x, y), (x+w, y+h), (255, 0, 0), 2)

    cv2.imshow('Detecting Cars(Red) and Pedestrians(Blue)..', frame)

    key = cv2.waitKey(1)

    if key==81 or key==113:
        break

# Release the VideoCapture object
video.release()

print("Code Completed")