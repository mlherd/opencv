import cv2

# = 0: loads the image as a grayscale image
# < 0: loads the image as is
# > 0: loads the image in the BGR format

grayscale = cv2.imread('lenna.jpg',0)
colorBgr = cv2.imread('lenna.jpg',-1)

cv2.imshow('lenna_grayscale',grayscale)
cv2.imshow('lenna_color',colorBgr)

# print images before any changes happen
print ("")
print ("grayscale image matrix: " + str(grayscale))
print ("")
print ("grayscale first pixel: " + str(grayscale[0][0]))

print ("")
print ("colorBgr image matrix: " + str(colorBgr))
print ("")
print ("colorBgr first pixel: " + str(colorBgr[0][0]))

# change the color value of the first pixels
grayscale[0][0] = 0
print ("")
print ("first pixel new value: " + str(grayscale[0][0]))

colorBgr[0][0] = (0, 255, 0)
print ("")
print ("first pixel new value: " + str(colorBgr[0][0]))

#change the color value of first 100 pixels in row 10
for i in range (0,100):
    grayscale[10][i] = 0

for i in range (0,100):
    # (B, G, R)
    colorBgr [10,i] = (0, 255, 0)

# display the results     
cv2.imshow('lenna_grayscale',grayscale)
cv2.imshow('lenna_color',colorBgr)

cv2.waitKey(0)
cv2.destroyAllWindows()
