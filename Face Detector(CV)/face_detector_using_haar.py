import cv2
from random import randrange

# Load pre-trained data on frontal face from opencv's github (using haar cascade algorithm)
trained_face_data = cv2.CascadeClassifier('haarcascade_frontalface_default.xml')

# Read an image
# img = cv2.imread('faces.jpg')

# Capture video (0->default webcam, or give 'file name')
webcam = cv2.VideoCapture(0)

# Iterate forever over frames
while True:
    # Read current frame(image)
    successfull_frame_read, frame = webcam.read()

    if successfull_frame_read:
        # Must convert to grayscale
        grayscaled_frame = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
    else:
        break
    
    # Detect Faces
    face_coordinates = trained_face_data.detectMultiScale(grayscaled_frame)
    print(face_coordinates) 

    # Draw rectangles around all the faces
    # cv2.rectangle(image, (top left coordinates), (bottom right coordinates), (b,g,r - rectangle color), thickness)
    for (x, y, w, h) in face_coordinates:
        cv2.rectangle(frame, (x,y), (x+w, y+h), (randrange(256), randrange(256), randrange(256)), 4)

    # Show the image with the message and rectangles over faces
    cv2.imshow('Lets see the faces..', frame)

    # cv2.waitKey() -> Wait/Don't exit until a key is pressed

    # Listen for a key press for 1ms, then move on
    key = cv2.waitKey(1)

    # Stop if Q or q key is pressed
    if key==81 or key==113:
        break

# Release the VideoCapture object
webcam.release()

print("\nCode Completed")