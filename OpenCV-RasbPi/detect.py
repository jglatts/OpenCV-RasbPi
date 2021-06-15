"""
    Simple OpenCV-Python script for face detection
    author: JDG
"""
import cv2

def detect_face():
    face_cascade = cv2.CascadeClassifier(cv2.data.haarcascades + 'haarcascade_frontalface_default.xml')
    cam = cv2.VideoCapture(0)
    while True:
        ret, img = cam.read()
        if ret is None: break 
        gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
        faces = face_cascade.detectMultiScale(gray, 1.1, 4)
        for (x, y, w, h) in faces:
            cv2.rectangle(img, (x, y), (x+w, y+h), (255, 0, 0), 2)
        cv2.imshow('Face Detect', img)
        if  cv2.waitKey(1) & 0xff == ord('q'): break
    cam.release()


if __name__ == "__main__":
    detect_face()
