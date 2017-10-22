import cv2
import numpy as np

#Load original image
original = cv2.imread('c_2.jpg')
cv2.imshow('original_image',original)

#convert image to grayscale
gray = cv2.cvtColor(original, cv2.COLOR_BGR2GRAY)
cv2.imshow('grayscale image',gray)
cv2.imwrite("grayscale_image.jpg",gray)

#run canny edge detection
edges = cv2.Canny(gray,30,90)
cv2.imshow("Edges", edges)
cv2.imwrite("edges.jpg",edges)

#find contours and draw contours
im2, contours, hierarchy= cv2.findContours(edges,cv2.RETR_TREE,cv2.CHAIN_APPROX_SIMPLE)
cv2.drawContours(original,contours,-1,(0,255,0),2)
cv2.imshow('contour',original)
cv2.imwrite("contour.jpg",original)

#draw a bounding rectangle around the object
cnt = contours[0]
x,y,w,h = cv2.boundingRect(cnt)
img = cv2.rectangle(original,(x,y),(x+w,y+h),(0,0,255),3)
cv2.imshow('boundingRect',original)
cv2.imwrite("boundingRect.jpg",original)

cv2.waitKey(0)
cv2.destroyAllWindows()
