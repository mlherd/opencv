import cv2
import numpy as np

# global variables
img = None
ret = None
threshold = None
se_square = None
se_cross = None
se_diamond = None
se_x = None

# load the image and conver it to a binary image
def load_images():
    global img, ret, threshold
    img = cv2.imread('corner_binary.jpg')
    cv2.imshow('original image',img)
    ret, threshold = cv2.threshold(img, 127, 255, cv2.THRESH_BINARY)

# create structing elements for the morphological operations
def create_structuring_elements():
    global se_square, se_cross, se_diamond, se_x
    
    se_square= np.matrix([[1, 1, 1, 1, 1], [1, 1, 1, 1, 1], [1, 1, 1, 1, 1], [1, 1, 1, 1, 1], [1, 1, 1, 1, 1]])
    print "se_square"
    print se_square

    se_cross= np.matrix([[0, 0, 1, 0, 0], [0, 0, 1, 0, 0], [1, 1, 1, 1, 1], [0, 0, 1, 0, 0], [0, 0, 1, 0, 0]])
    print "se_cross"
    print se_cross

    se_diamond= np.matrix([[0, 0, 1, 0, 0], [0, 1, 1, 1, 0], [1, 1, 1, 1, 1], [0, 1, 1, 1, 0], [0, 0, 1, 0, 0]])
    print "se_diamond"
    print se_diamond
    
    se_x= np.matrix([[1, 0, 0, 0 ,1], [0, 1, 0, 1, 0], [0, 0, 1, 0, 0], [0, 1, 0, 1, 0], [1, 0, 0, 0, 1]])
    print "se_x"
    print se_x

# detect corners by morphological operations
def corner_detection():
    #global ret, threshold

    result1 = cv2.dilate(threshold,se_cross,iterations = 1)
    cv2.imshow('dilation',result1)

    result1 = cv2.erode(result1,se_diamond,iterations = 1)
    cv2.imshow('erode',result1)

    result2 = cv2.dilate(threshold,se_x,iterations = 1)
    cv2.imshow('dilation2', result2)

    result2 = cv2.erode(result2,se_square,iterations = 1)
    cv2.imshow('erode2',result2)

    diff = cv2.absdiff(result1,result2);
    cv2.imshow('diff',diff)
    cv2.imwrite("q3-original.jpg", threshold)
    cv2.imwrite("q3-result2.jpg", diff)
    
    
load_images()
create_structuring_elements()
corner_detection()

cv2.waitKey(0)
cv2.destroyAllWindows()

