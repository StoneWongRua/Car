import cv2
from skimage import exposure

face = cv2.CascadeClassifier('haarcascade_frontalface_default.xml')
face.load(r'C:\Users\15845\.ipython\cv2\data\haarcascade_frontalface_default.xml')
cap = cv2.VideoCapture(0)
while 1:
    ret, frame = cap.read()
    frame = exposure.adjust_gamma(frame, 0.5)
    grayframe = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
    faces = face.detectMultiScale(grayframe, 1.3, 5)
    for (x, y, w, h) in faces:
        cv2.rectangle(frame, (x, y), (x + w, y + h), (255, 0, 0), 2)
    cv2.imshow('img', frame)
    k = cv2.waitKey(10)
    if k == 27:
        break
cv2.destroyAllWindows()