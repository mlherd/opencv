import cv2
import numpy as np

def nothing(x):
    pass

# Create a black image and a window
img = np.zeros((300,512,3), np.uint8)
cv2.namedWindow('ui')

#resize and move the window
cv2.moveWindow('ui', 0, 0)
cv2.resizeWindow('ui', 512, 512)

# create trackbars for color change
cv2.createTrackbar('Red','ui',0,255,nothing)
cv2.createTrackbar('Green','ui',0,255,nothing)
cv2.createTrackbar('Blue','ui',0,255,nothing)

# set trackbar values
cv2.setTrackbarPos('Red','ui', 123)
cv2.setTrackbarPos('Green','ui', 123)
cv2.setTrackbarPos('Blue','ui', 123)

# create a switch for ON/OFF functionality
switch = '0 : OFF \n1 : ON'
cv2.createTrackbar(switch, 'ui',0,1,nothing)

while(1):
    cv2.imshow('ui',img)
    k = cv2.waitKey(1) & 0xFF

    # Esc key to break
    if k == 27:
        break

    # get current positions of four trackbars
    r = cv2.getTrackbarPos('Red','ui')
    g = cv2.getTrackbarPos('Green','ui')
    b = cv2.getTrackbarPos('Blue','ui')
    s = cv2.getTrackbarPos(switch,'ui')

    if s == 0:
        img[:] = 0
    else:
        img[:] = [b,g,r]

cv2.destroyAllWindows()
