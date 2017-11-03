import numpy as np
import cv2

flag = 1
# Create a VideoCapture object and read from input file
cap = cv2.VideoCapture('Seahawks.avi')

# Read until video is completed
while(cap.isOpened()):
    # Capture frame-by-frame
    ret, frame = cap.read()
    # Display the resulting frame
    gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)

    # Show only the 1st frame
    if flag == 1:
         cv2.imshow('first_frame',gray)
         flag = 0

    # Display the resulting frame
    cv2.imshow('grayscale',gray)
         
    # Press Q on keyboard to  exit
    if cv2.waitKey(25) & 0xFF == ord('q'):
        break

cap.release()
cv2.destroyAllWindows()
