import cv2

# use camera as a source
# if you have more than 1 camera change the number 0, 1, 2 etc.
capBack = cv2.VideoCapture(0)
capFront = cv2.VideoCapture(1)

# counter for the image name
counter = 0

while(True):
    # Capture frame-by-frame from the back and the front camera
    ret, frameBack = capBack.read()
    ret, frameFront = capFront.read()

    # Our operations on the frame come here
    # Make the frame grayscale
    gray = cv2.cvtColor(frameBack, cv2.COLOR_BGR2GRAY)

    #Display the original frame from the front camera
    cv2.imshow('color image frame',frameFront)
    
    # Display the resulting frame
    cv2.imshow('grayscale frame',gray)

    # if c is presssed, save the image. Name the image image_<counter>.jpg.
    if cv2.waitKey(1) & 0xFF == ord('c'):
        name = "image_" + str(counter) + ".jpg"
        cv2.imwrite(name, frameBack)
        counter = counter + 1
        
    # break the while loop if q is pressed
    elif cv2.waitKey(1) & 0xFF == ord('q'):
            break

# When everything done, release the capture
capBack.release()
capFront.release()
cv2.destroyAllWindows()
