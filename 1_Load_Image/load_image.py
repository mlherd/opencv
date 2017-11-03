import cv2

# = 0: loads the image as a grayscale image
# < 0: loads the image as is
# > 0: loads the image in the BGR format

grayscale = cv2.imread('lenna.jpg',0)
asItis = cv2.imread('lenna.jpg',1)
colorBgr = cv2.imread('lenna.jpg',-1)

cv2.imshow('lenna_grayscale',grayscale)
cv2.imshow('lenna_asItis',asItis)
cv2.imshow('lenna_color',colorBgr)

cv2.waitKey(0)
cv2.destroyAllWindows()
