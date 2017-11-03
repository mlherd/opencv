import cv2
import numpy as np

x = np.array([1, 0, 1])
print ("x: ", x)
y = np.array([1, 0, 0])
print ("y: ", y)
z1 = cv2.bitwise_and(x,y)
print ("x and y: ")
print(z1)
z2 = cv2.bitwise_or(x,y)
print ("x or y: ")
print(z2)
z3 = cv2.bitwise_xor(x, y)
print ("x xor: ")
print(z3)

cv2.waitKey(0)
cv2.destroyAllWindows()

