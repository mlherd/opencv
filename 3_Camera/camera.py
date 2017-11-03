import cv2

# use camera as a source
# if you have more than 1 camera change the number 0, 1, 2 etc.
cap = cv2.VideoCapture(0)

while(True):
    # Capture frame-by-frame
    ret, frame = cap.read()

    # Our operations on the frame come here
    # Make the frame grayscale
    gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)

    #Display the original frame
    cv2.imshow('color image frame',frame)
    
    # Display the resulting frame
    cv2.imshow('grayscale frame',gray)
    if cv2.waitKey(1) & 0xFF == ord('q'):
        break

# When everything done, release the capture
cap.release()
cv2.destroyAllWindows()
