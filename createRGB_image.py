import cv2
import numpy as np

# image variables
height = 200
width = 200
blank_image = None

# creates an white image
def create_RGBimage():
    global blank_image
    blank_image = np.zeros((height, width, 3), np.uint8)
    blank_image[0:200, 0:200] = (255, 255, 255)
    cv2.imshow("blank image", blank_image)

def draw_circle():
    global blank_image
    cv2.circle(blank_image,(100,100), 20, (255,0,0), -1)
    cv2.imshow("circle", blank_image)

def draw_rectangle():
    global blank_image
    for i in range(60,100):
        for j in range(30,100):
            bgr = blank_image [i,j]
            # only update the green channel by comparing the original values
            if bgr[0] == 255 and bgr[1] == 255 and bgr[2] == 255:
                blank_image [i,j] = (0, 255, 0)
            else:
                blank_image [i,j] = (bgr[0], 255, bgr[2])
            
create_RGBimage()
draw_circle()
draw_rectangle()
cv2.imshow("result", blank_image)
cv2.imwrite("q4-result.jpg", blank_image)
cv2.waitKey(0)
cv2.destroyAllWindows()

