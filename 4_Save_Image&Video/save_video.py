import cv2

cap = cv2.VideoCapture(0)

# Define the codec and create VideoWriter object
# fourcc: 4-character code of codec
fourcc = cv2.VideoWriter_fourcc(*'XVID')
out = cv2.VideoWriter('output.avi',fourcc, 20.0, (640,480))

while(cap.isOpened()):
    ret, frame = cap.read()
    if ret==True:

        # write the frame
        out.write(frame)

        cv2.imshow('my_video',frame)
        
        if cv2.waitKey(1) & 0xFF == ord('q'):
            break
    else:
        break

# Release everything if job is finished
cap.release()
out.release()
cv2.destroyAllWindows()
