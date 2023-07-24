import cv2
import time 
import numpy as np

fourcc = cv2.VideoWriter_fourcc(*"XVID")
output_file = cv2.VideoWriter('output_avi.avi', fourcc, 20.0, (640, 480))

cap = cv2.VideoCapture(0)

time.sleep(2)
bg = 0 

for i in range(60):
    ret, bg = cap.read()
    bg = np.flip(bg, axis=1)

while cap.isOpened():
    ret, img = cap.read()
    if not ret:
        break

    img = np.flip(img, axis=1)

    hsv = cv2.cvtColor(img, cv2.COLOR_BGR2HSV)

    lower_red = np.array([0, 120, 50])
    upper_red = np.array([10, 255, 255])
    mask_1 = cv2.inRange(hsv, lower_red, upper_red)

    mask_1 = mask_1 + 1 - mask_1

    img[np.where(mask_1 == 1)] = bg[np.where(mask_1 == 1)]

    output_file.write(img)

    cv2.imshow("Magic", img)
    if cv2.waitKey(1) & 0xFF == 27: 
        break

cap.release()
output_file.release()
cv2.destroyAllWindows()
