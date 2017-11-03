import cv2
import numpy as np

# Load and display original images
img1 = cv2.imread('psu.png')
img2 = cv2.imread('opencv.jpg')
cv2.imshow('psu_logo',img1)
cv2.imshow('opencv_logo',img2)

# add and absdiff operations
result1 = cv2.addWeighted(img1,0.7,img2,0.3,0)
result2 = cv2.absdiff(img1,img2)

#show results
cv2.imshow('addWeighted',result1)
cv2.imshow('absdiff',result2)

cv2.waitKey(0)
cv2.destroyAllWindows()

