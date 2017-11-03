import numpy as np
import cv2

# Create a black image
img = np.zeros((900,1024,3), np.uint8)

# Draw a diagonal blue line with thickness of 5 px
cv2.line(img,(0,0),(511,511),(255,0,0),5)

# Draw a green rectangle with thickness of 3 px
cv2.rectangle(img,(384,0),(510,128),(0,255,0),3)

# Draw a circle
cv2.circle(img,(200,400), 63, (0,0,255), -1)

# Draw a polygon
pts = np.array([[300,550],[400,800],[900,700],[700,600]], np.int32)

# Reshape gives a new shape to an array without changing its data.
pts = pts.reshape((-1,1,2))
cv2.polylines(img,[pts],True,(0,255,255))

# Add a text
font = cv2.FONT_HERSHEY_SIMPLEX
cv2.putText(img,'Portland State University',(600,500), font, 1,(0,255,0),2,cv2.LINE_AA)

cv2.imshow("result", img)

cv2.waitKey(0)
cv2.destroyAllWindows()
