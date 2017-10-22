import cv2
import numpy as np

img = cv2.imread('image.jpg')
cv2.imshow('original image',img)

# get the size of the original image
shape=img.shape
w=shape[1]
h=shape[0]

# create a base 3 chanale image - 20 pixel larger from the sides 
base_size=h+20,w+20,3
base=np.zeros(base_size,dtype=np.uint8)

#create a black rectange and put it in the base image
cv2.rectangle(base,(0,0),(w+20,h+20),(0,0,0),0)#black rectangle
cv2.imshow("black_image",base)

#put the original image on the base image - move it 10 pixel right and down to create borders around the original image
base[10:h+10,10:w+10]=img
cv2.imshow("border_reflection",base)
cv2.imwrite("border_reflection.jpg",base)

# get size of the new image with its new boarders
h,w = base.shape[:2]

#downscale the image
img1 = cv2.pyrDown(base,dstsize = (w/2,h/2))
cv2.imshow("Gaussian Level 1",img1)
cv2.imwrite("Gaussian_Level_1.jpg",img1)

#get the size of the downscaled image
h,w = img1.shape[:2]

#downscale the image
img2 = cv2.pyrDown(img1,dstsize = (w/2,h/2))
cv2.imshow("Gauissian Level 2",img2)
cv2.imwrite("Gauissian_Level_2.jpg",img2)

#get the size of the downscaled image
h,w = img2.shape[:2]

#upscale the image
img3 = cv2.pyrUp(img2,dstsize = (2*w,2*h))
cv2.imshow("Upscaled image 1",img3)
cv2.imwrite("Upscaled_image_1.jpg",img3)

#get the size of the upscaled image
h,w = img3.shape[:2]

#upscale the image
img4 = cv2.pyrUp(img3,dstsize = (2*w,2*h))
cv2.imshow("Upscaled image 2",img4)
cv2.imwrite("Upscaled_image_2.jpg",img4)

#first level of the laplacian pyramid
lap1 = cv2.subtract(base,img4)
cv2.imshow("Laplacian Level 1",lap1)
cv2.imwrite("Laplacian_Level_1.jpg",lap1)

#second level of the laplacian pyramid
lap2 = cv2.subtract(img1,img3)
cv2.imshow("Laplacian Level 2",lap2)
cv2.imwrite("Laplacian_Level_2.jpg",lap2)

#refactoring the original image
#factor gaussian image with laplacian image
factor1 = cv2.add(lap2, img3)
cv2.imshow("Reconstruction first step",factor1)
cv2.imwrite("Reconstruction_first_step.jpg",factor1)

# expand the refactored image
h,w = factor1.shape[:2]
expanded = cv2.pyrUp(factor1,dstsize = (2*w,2*h))

#factor refactored image with laplacian image
factor2 = cv2.add(expanded, lap1)
cv2.imshow("Reconstruction Original image",factor2)
cv2.imwrite("Reconstructed_Original_image.jpg",factor2)

cv2.waitKey(0)
cv2.destroyAllWindows()

