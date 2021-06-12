"""
    Simple OpenCV-Python Script to verify install
    author: JDG
"""
import imutils
import cv2

def opencv_test():
    img = cv2.imread("kush.png")
    (h, w, d) = img.shape
    print("width={}, height={}, depth={}".format(w, h, d))
    resize_and_rotate(img)

def resize_and_rotate(img):   
    img = cv2.resize(img, (200, 200))
    while (1):
        angle = 30
        while (angle <= 360):
            print("Angle = {}\n".format(angle))
            img_copy = imutils.rotate_bound(img, angle)
            cv2.resize(img_copy, (200, 200))
            cv2.blur(img_copy, (35, 35))
            cv2.imshow("CV JDG", img_copy)
            cv2.waitKey(50)
            angle += 30

if __name__ == "__main__":
    opencv_test()
