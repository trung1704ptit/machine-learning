import numpy as np
import cv2

img = cv2.imread("dantruong.jpg")
cv2.line(img,(0,0), (400, 300), (255, 3, 134), 5);
cv2.imwrite('line.jpg', img)