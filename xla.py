import cv2
import numpy as np

img = cv2.imread('line.jpg')

cv2.imshow('image', img)

for i in range(200): # loop to 200
    for j in range(200): # loop to 200
        if img[i,j,0] > 30:  # if the first of property is greater than 30
            img[i, j] = 1 # force color to 1

cv2.imwrite('anh2.jpg', img)