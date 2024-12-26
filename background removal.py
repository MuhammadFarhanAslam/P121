import cv2
import numpy as np

camera = cv2.VideoCapture(0)
camera.set(3, 640)
camera.set(4, 480)

mountain = cv2.imread('mount everest.jpg')
mountain = cv2.resize(mountain, (640, 480))

while True:
    status, frame = camera.read()
    if status:
        frame = cv2.flip(frame, 1)
        frame_rgb = cv2.cvtColor(frame, cv2.COLOR_BGR2RGB)
        hsv = cv2.cvtColor(frame, cv2.COLOR_BGR2HSV)
        lower_bound = np.array([100, 100, 100])
        upper_bound = np.array([255, 255, 255])
        img = cv2.inRange(hsv, lower_bound, upper_bound)
        img1 = img
        img2 = mountain
        final_image = np.where(img1 == 0, img1, img2)
        cv2.imshow('frame', frame)
        code = cv2.waitKey(1)
        if code == 32:
            break

camera.release()
cv2.destroyAllWindows()
