## Speed Comparison ##

# This program is to show the advantage of using numpy arrays for matrix functions
# and how they compare to lists. Increase the x/y values to make the matrix larger.
# numpy is much faster.

# Results depend on the system, but here is some rough numbers based on mine
# Eg. 200x200 matrix = ~1115 times faster
# Eg. 2000x2000 matrix = ~

import numpy as np
# import cupy as np # Used for cuda support
from datetime import datetime

# matrix size
x = 2000
y = 2000

# create an x*y matrix 
A = np.random.choice(10, size=(x,y))
# create an x*y matrix  
B = np.random.choice(10, size=(x,y))
# create an x*y matrix for the results
result= np.zeros((x,y))


# take timestamp
t0 = datetime.now()
# Slow calculation
for i in range(len(A)):   
  # iterating by coloum by B  
  for j in range(len(B[0])): 
      # iterating by rows of B 
      for k in range(len(B)): 
          result[i][j] += A[i][k] * B[k][j]
# read duration
dt1 = datetime.now() - t0

t0 = datetime.now()
#Fast calculation
result = A @ B # can also be done with np.dot(A,B) or matmul
dt2 = datetime.now() - t0

print("Time for slow method:", dt1.total_seconds())
print("Time for fast method:", dt2.total_seconds())
print("(slow / fast) Factor:", dt1.total_seconds() / dt2.total_seconds())