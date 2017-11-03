import cv2
import numpy as np

drawing = False # true if mouse is pressed
mode = True # if True, draw rectangle. Press 'm' to toggle to curve
ix,iy = -1,-1

# mouse callback function
def draw_circle(event,x,y,flags,param):
    global ix,iy,drawing,mode

    # if left button is clicked enable drawing
    if event == cv2.EVENT_LBUTTONDOWN:
        drawing = True
        ix,iy = x,y
        
    # if left button is clicked disable drawing
    if event == cv2.EVENT_RBUTTONDOWN:
        drawing = False
        ix,iy = x,y

    # if drawing is enabled draw black circles
    if event == cv2.EVENT_MOUSEMOVE:
        if drawing == True:
            cv2.circle(img,(x,y),2,(0,0,0),-1)

#create a black image
img = np.zeros((512,512,3), np.uint8)
#make it white
img[:,0:512] = (255,255,255) 

cv2.namedWindow('whiteboard')
cv2.setMouseCallback('whiteboard',draw_circle)

while(1):
    cv2.imshow('whiteboard',img)
    k = cv2.waitKey(1) & 0xFF
    if k == ord('m'):
        mode = not mode
    elif k == 27:
        break

cv2.destroyAllWindows()
