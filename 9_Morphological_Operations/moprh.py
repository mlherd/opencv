import cv2
import numpy as np

img1 = cv2.imread('sample1.png',0)
cv2.imshow("sample1", img1)

img2 = cv2.imread('sample2.png',0)
cv2.imshow("sample2", img2)

img3 = cv2.imread('sample3.png',0)
cv2.imshow("sample3", img3)

img4 = cv2.imread('sample4.png',0)
cv2.imshow("sample4", img4)

#5x5 structuring elemnent all ones
kernel = np.ones((5,5),np.uint8)

#dilation
dilation = cv2.dilate(img1,kernel,iterations = 1)
cv2.imshow("dilation", dilation)

#erosion
erosion = cv2.erode(img2,kernel,iterations = 1)
cv2.imshow("erosion", erosion)

#opening
opening = cv2.morphologyEx(img3, cv2.MORPH_OPEN, kernel)
cv2.imshow("opening", opening)

#closing
closing = cv2.morphologyEx(img4, cv2.MORPH_CLOSE, kernel)
cv2.imshow("closing", closing)

cv2.waitKey(0)
cv2.destroyAllWindows()

