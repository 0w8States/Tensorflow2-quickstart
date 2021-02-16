# This program generates random data and then plots them/categorizes based on an XOR gate

import numpy as np
import matplotlib.pyplot as plt

# Generate a 2D array with floating point values between 1 and -1
A = np.random.uniform(-1,1, size=(10000,10000))

# Generate a new 2D array of just 0's and 1's using the previous random 2D array. 
# If the random value is previous 2D array is Positive then store 1
# if the random value is negative then store 0
B = np.where(A[:,:]<0, 0,1)

#Perform the XOR check for each of the elements by checking whether column 0 and column 1 of the new 2D array is not equal and store a 1 in y when not equal
C = np.where(B[:,0] != B[:,1],1,0)

# Create the scatter plot
plt.scatter(A[:,0],A[:,1], c=C)
plt.show()