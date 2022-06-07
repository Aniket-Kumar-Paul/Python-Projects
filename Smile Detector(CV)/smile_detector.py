import cv2

face_detector = cv2.CascadeClassifier('haarcascade_frontalface_default.xml')
smile_detector = cv2.CascadeClassifier('haarcascade_smile.xml')

webcam = cv2.VideoCapture(0)

# Detect Smiles inside the faces and use optimizations
while True:
    successfull_frame_read, frame = webcam.read()
    if not successfull_frame_read:
        break
    frame_grayscale = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)

    faces = face_detector.detectMultiScale(frame_grayscale)
    
    # Find all faces
    for (x,y,w,h) in faces:
        cv2.rectangle(frame, (x,y), (x+w,y+h), (0,255,0), 4)
        
        # Just get the sub image of the face from the whole frame using slicing
        # openCV uses numpy, so we can slice as shown below
        the_face = frame[y:y+h, x:x+w]
        face_grayscale = cv2.cvtColor(the_face, cv2.COLOR_BGR2GRAY)

        # Optimizations :-
        # scaleFactor -> How much to blur the image (Another optimization on top of the grayscaling of image)
        # minNeighbors -> =20 => there must be atleast 20 rectangles in an area to actually count it as a smile
        smiles = smile_detector.detectMultiScale(face_grayscale, scaleFactor=1.7, minNeighbors=20)

        # Find all smiles in the face
        #for (x_,y_,w_,h_) in smiles:
        #    cv2.rectangle(the_face, (x_,y_), (x_+w_,y_+h_), (0,255,255), 4)
    
        # Labelling face as smiling instead of drawing rectangles
        if len(smiles) > 0:
            cv2.putText(frame, 'smiling :)', (x, y+h+40), fontScale=3,
            fontFace=cv2.FONT_HERSHEY_PLAIN, color=(255,255,255))
        else:
            cv2.putText(frame, 'why serious :(', (x, y+h+40), fontScale=3,
            fontFace=cv2.FONT_HERSHEY_PLAIN, color=(255,255,255)) 
            
    cv2.imshow('Detecting Smiles..', frame)

    key = cv2.waitKey(1)
    if key==81 or key==113:
        break

# Cleanup
webcam.release()
cv2.destroyAllWindows()

print('Code Completed')