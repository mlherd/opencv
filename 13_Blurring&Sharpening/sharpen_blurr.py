import cv2
import numpy as np
from matplotlib import pyplot as plt

#image for blurring
img1 = cv2.imread('input1.png')

#image for sharpening
img2 = cv2.imread('input2.jpg')

#Create a kernel
kernel = np.ones((5,5),np.float32)/25

#Apply custom-made filter to theimage
custom = cv2.filter2D(img1,-1,kernel)

# Use blur function
blur = cv2.blur(img1,(3,3))

# Use Gaussian Blur function
gaussianblur = cv2.GaussianBlur(img1,(5,5),0)

# Use Median Blur
median = cv2.medianBlur(img1,5)

# Use Sharpening
kernel = np.array([[-1,-1,-1], [-1,9,-1], [-1,-1,-1]])
sharp = cv2.filter2D(img2, -1, kernel)

# Unsharp Masking
mask = cv2.GaussianBlur(img2,(0, 0), 3);
unsharp = cv2.addWeighted(mask, 4, img2, -3, 0);

cv2.imshow('Original_1', img1)
cv2.imshow('Original_2', img2)
cv2.imshow('Averaging', custom)
cv2.imshow('Blur_Function', blur)
cv2.imshow('Baussian Blur', gaussianblur)
cv2.imshow('Median Blur', median)
cv2.imshow('Sharpening', sharp)
cv2.imshow('UnsharpMask', unsharp)


cv2.waitKey(0)
cv2.destroyAllWindows()
