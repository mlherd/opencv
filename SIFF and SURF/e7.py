import numpy as np
import cv2
from matplotlib import pyplot as plt

#SIFT - FLANN Based - Shoe and Shoe_test1

img1 = cv2.imread('shoe.jpg',0) # Training Image
img2 = cv2.imread('shoe_test1.jpg',0) # Testing Image

e1 = cv2.getTickCount()

# Initiate SIFT detector
sift = cv2.xfeatures2d.SIFT_create()

# find the keypoints and descriptors with SIFT
kp1, des1 = sift.detectAndCompute(img1,None)
kp2, des2 = sift.detectAndCompute(img2,None)

print ("keypoints 1:" + str(len(kp1)))
print ("keypoints 2:" + str(len(kp2)))

# FLANN parameters
FLANN_INDEX_KDTREE = 0
index_params = dict(algorithm = FLANN_INDEX_KDTREE, trees = 5)
search_params = dict(checks=50)
flann = cv2.FlannBasedMatcher(index_params,search_params)

matches = flann.knnMatch(des1,des2,k=2)

# draw only good matches, so create a mask
matchesMask = [[0,0] for i in xrange(len(matches))]
print("number of matches: " + str(len(matches)))

counter = 0
# ratio test
for i,(m,n) in enumerate(matches):
    if m.distance < 0.5*n.distance:
        matchesMask[i]=[1,0]
        counter = counter + 0
        
print("number of good matches: " + str(counter))       

#cv2.drawMatchesKnn expects list of lists as matches.
draw_params = dict(matchColor = (0,255,0),
                   singlePointColor = (255,0,0),
                   matchesMask = matchesMask,
                   flags = 0)

img3 = cv2.drawMatchesKnn(img1,kp1,img2,kp2,matches,None,**draw_params)

e2 = cv2.getTickCount()
time = (e2 - e1)/ cv2.getTickFrequency()
print("time:" + str(time))

plt.imshow(img3),plt.show()

