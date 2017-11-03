import numpy as np

#create an 3x5 array with values between 0-15
a = np.arange(15).reshape(3, 5)

#Print the array
print ("Example array: ")
print (a)

#The dimensions of the array.
#This is a tuple of integers indicating the size of the array in each dimension. 
print("")
print("The dimensions of the array: "+ str(a.shape))

#The number of axes (dimensions) of the array.
print("")
print("Dimentions: " + str(a.ndim))

#An object describing the type of the elements in the array.
print("")
print("Element type: " + str(a.dtype.name))

# The size in bytes of each element of the array.
print("")
print("Element size in byte: "+ str(a.itemsize))

# The actual elements of the array.
print("")
print("Total number of elements of the array: "+ str(a.size))

# Create an 1x3 array
b = np.array([6, 7, 8])
print("")
print(b)

# Creare an array full zeros
zero = np.zeros((3,4))
print("")
print("An array full zeros: ")
print(zero)

# Create an array full ones
one = np.ones((2,3,4), dtype=np.int16)
print("")
print("An array full ones: ")
print(one)

# Create an uninitialized array - result may vary
empty = np.empty((2,3))
print("")
print("Uninitialized array: ")
print(empty)

# Create an array of squences of numbers
squence = np.arange(10, 30, 5)
print("")
print("Squence array: " + str(squence))
