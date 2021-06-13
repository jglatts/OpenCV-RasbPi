"""
    Simple OpenCV-Python script to verify camera access
    author: JDG
"""
import imutils
import cv2

def obscure_frame(frame):
    frame = cv2.resize(frame, (200, 200))
    frame = cv2.cvtColor(frame, cv2.COLOR_RGB2GRAY)
    cv2.blur(frame, (30, 30)) 
    return frame

def cam_capture():
    vid = cv2.VideoCapture(0)
    while(1):
        ret, frame = vid.read()
        frame = obscure_frame(frame)
        cv2.imshow('JDG OpenCV-Python', frame)
        if cv2.waitKey(1) & 0xFF == ord('q'): break
    vid.release()
    cv2.destroyAllWindows()

if __name__ == "__main__":
    cam_capture()
