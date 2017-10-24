import numpy as np
import cv2
from matplotlib import pyplot as plt

#SURF - BFMatcher - Bear and Bear_test1

print("SURF - BFMatcher - Bear and Bear_test1")

img1 = cv2.imread('bear.jpg',0) # queryImage
img2 = cv2.imread('bear_test1.jpg',0) # trainImage

e1 = cv2.getTickCount()

# Initiate SURF detector
surf = cv2.xfeatures2d.SURF_create()

# find the keypoints and descriptors with SURF
kp1, des1 = surf.detectAndCompute(img1,None)
kp2, des2 = surf.detectAndCompute(img2,None)

print ("keypoints 1:" + str(len(kp1)))
print ("keypoints 2:" + str(len(kp2)))

# BFMatcher with default params
bf = cv2.BFMatcher()
matches = bf.knnMatch(des1,des2, k=2)
print("number of matches: " + str(len(matches)))

# draw only good matches, so create a mask
matchesMask = [[0,0] for i in xrange(len(matches))]

counter = 0
# ratio test
for i,(m,n) in enumerate(matches):
    if m.distance < 0.5*n.distance:
        matchesMask[i]=[1,0]
        counter = counter + 1
        
print("number of good matches: " + str(counter))

draw_params = dict(matchColor = (0,255,0),
                   singlePointColor = (255,0,0),
                   matchesMask = matchesMask,
                   flags = 0)

# cv2.drawMatchesKnn expects list of lists as matches.
img3 = cv2.drawMatchesKnn(img1,kp1,img2,kp2,matches,None,**draw_params)

e2 = cv2.getTickCount()
time = (e2 - e1)/ cv2.getTickFrequency()
print("time:" + str(time))

plt.imshow(img3),plt.show()

