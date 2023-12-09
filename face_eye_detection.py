import cv2

face_cascade = cv2.CascadeClassifier(r'cascades\haarcascade_frontalface_alt.xml')

eye_cascade = cv2.CascadeClassifier(r'cascades\haarcascade_eye.xml')

cap = cv2.VideoCapture(0)

while True:
    ret, frame = cap.read()

    faces = face_cascade.detectMultiScale(frame, 1.1, 5, minSize=(10, 10))

    for (x, y, w, h) in faces:
        cv2.rectangle(frame, (x, y), (x+w, y+h), (200, 0, 0), 2)
        
        roi = frame[y:y+h, x:x+w]
        eyes = eye_cascade.detectMultiScale(roi, 1.1, 20, minSize=(2, 2))
        for (ex, ey, ew, eh) in eyes:
            radius = int((ew+eh)/4)
            
            cv2.circle(roi, (int(ex+ew/2), int(ey+eh/2)), radius, (0, 0, 255), 2, cv2.LINE_AA)
            radius = 0
            frame[y:y+h, x:x+w] = roi
           
    cv2.imshow('cam', frame)
    
    if cv2.waitKey(1) & 0xFF == ord(' '):
        break

cv2.destroyAllWindows()
cap.release()