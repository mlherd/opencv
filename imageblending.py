import cv2
import numpy as np
# load the original images
g1= cv2.imread('gray_1.jpg')
cv2.imshow('original_image_g1',g1)
g2= cv2.imread('gray_2.jpg')
cv2.imshow('original_image_g2',g2)

# convert them to gray scale
gray1 = cv2.cvtColor(g1, cv2.COLOR_BGR2GRAY)
cv2.imshow('grayscale_image_1',gray1)
cv2.imwrite("grayscale_image_1.jpg",gray1)
gray2 = cv2.cvtColor(g2, cv2.COLOR_BGR2GRAY)
cv2.imshow('grayscale_image_2',gray2)
cv2.imwrite("grayscale_image_2.jpg",gray2)

# calculate the absulute difference of the images
result = cv2.absdiff(gray1, gray2)
cv2.imshow('absdiff',result)
cv2.imwrite("absdiff.jpg",result)

#trashold the image
ret,thresh = cv2.threshold(result,65,255,0)
cv2.imshow("thresh", thresh)
cv2.imwrite("thresh.jpg",thresh)

#open and close the image to get rid of noise
kernel = np.ones((5,5),np.uint8)
opening = cv2.morphologyEx(thresh, cv2.MORPH_OPEN, kernel)
cv2.imshow("opening", opening)
cv2.imwrite("opening.jpg",opening)
closing = cv2.morphologyEx(opening, cv2.MORPH_CLOSE, kernel)
cv2.imshow("closing", closing)
cv2.imwrite("closing.jpg",closing)

#flood fill the white area with the value 100
h,w = closing.shape[:2]
flooded =closing
for i in range(0, h):
        for j in range(0, w):
            if flooded[i][j] == 255:
                flooded[i][j] = 100
cv2.imshow("floodfill", flooded)
cv2.imwrite("floodfill.jpg",flooded)

# add the cup in the original image without the cup
inv = cv2.bitwise_not(flooded)
cv2.imshow("inv", inv)
cv2.imwrite("inv.jpg",inv)
r1 = cv2.bitwise_and(gray2, flooded)
cv2.imshow("r1", r1)
cv2.imwrite("r1.jpg",r1)
r2 = cv2.bitwise_and(inv,gray1)
cv2.imshow("r2", r2)
cv2.imwrite("r2.jpg",r2)
r3 = cv2.bitwise_or(r1,r2)
cv2.imshow("r3", r3)
cv2.imwrite("r3.jpg",r3)

cv2.waitKey(0)
cv2.destroyAllWindows()
for i in range (1,5):
    cv2.waitKey(1)
