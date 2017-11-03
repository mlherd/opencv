# -*- coding: cp1252 -*-
import cv2
import numpy as np

img = cv2.imread('portland.jpg', 0)
cv2.imshow("original", img)

#interpolation methods:

#INTER_NEAREST - a nearest-neighbor interpolation
#INTER_LINEAR - a bilinear interpolation (used by default)
#INTER_AREA - resampling using pixel area relation. A preferred method for image decimation, as it gives moire’-free results.
#INTER_CUBIC - a bicubic interpolation over 4x4 pixel neighborhood
#INTER_LANCZOS4 - a Lanczos interpolation over 8x8 pixel neighborhood

#scale down
res = cv2.resize(img,None,fx=0.5, fy=0.5, interpolation = cv2.INTER_AREA)
cv2.imshow("half", res)

#scale up
height, width = img.shape[:2]
res = cv2.resize(img,(300, 150), interpolation = cv2.INTER_CUBIC)
cv2.imshow("300x150", res)

#translation
rows,cols = img.shape
x =5000
y =200
translation_matrix = np.float32([[1,0,100],[0,1,50]])
translation = cv2.warpAffine(img,translation_matrix,(cols,rows))
cv2.imshow('translation',translation)

#rotation
rows,cols = img.shape
M = cv2.getRotationMatrix2D((cols/2,rows/2),90,1)
rotation = cv2.warpAffine(img,M,(cols,rows))
cv2.imshow('rotation',rotation)

cv2.waitKey(0)
cv2.destroyAllWindows()
