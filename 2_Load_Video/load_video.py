import cv2
 
# Create a VideoCapture object and read from input file
cap = cv2.VideoCapture('Seahawks.avi')
 
# Read until video is completed
while(cap.isOpened()):
  # Capture frame-by-frame
  ret, frame = cap.read()
  if ret == True:
 
    # Display the resulting frame
    cv2.imshow('Color Video',frame)
 
    # Press Q on keyboard to  exit
    if cv2.waitKey(50) & 0xFF == ord('q'):
      break
 
  # Break the loop
  else: 
    break
 
# When everything done, release the video capture object
cap.release()
 
# Closes all the frames
cv2.destroyAllWindows()

