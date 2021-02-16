## Speed Comparison ##

# This test is to compare how much faster numpy is compared to python lists, in terms of the dot product
# calculated the dot product using both methods 100,000 times, and then prints the ratio of time
import numpy as np
from datetime import datetime

# note: you can also use %timeit

a = np.random.randn(100)
b = np.random.randn(100)
T = 100000

def slow_dot_product(a, b):
  result = 0
  for e, f in zip(a, b):
    result += e*f
  return result

t0 = datetime.now()
for t in range(T):
  slow_dot_product(a, b)
dt1 = datetime.now() - t0

t0 = datetime.now()
for t in range(T):
  a.dot(b)
dt2 = datetime.now() - t0


print("Time for slow method:", dt1.total_seconds())
print("Time for fast method:", dt2.total_seconds())
print("(slow / fast) Factor:", dt1.total_seconds() / dt2.total_seconds())