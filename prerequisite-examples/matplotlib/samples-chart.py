import numpy as np
import matplotlib.pyplot as plt


### Standard Time Series Line Chart ##

# Create a 1D array with 1000 evenly spaced points between 0 and 20
x = np.linspace(0 , 20, 1000) 
y = np.sin(x) + 0.2 * x

plt.plot(x,y)
plt.xlabel('input')
plt.ylabel('output')
plt.title('my plot')
plt.show()

## Scatter Plot ##
# 100 datapoints with dimensionality of 2
x = np.random.randn(100, 2) 
plt.scatter(x[:,0], x[:,1])
plt.show()

# Do some classification
x = np.random.randn(200, 2)
# Since randr draws from the standard normal, they all tend to be near zero. Center some of the datapoints at 3 instead.
x[:50] += 3 
 # Create and array of zeros for labels
y = np.zeros(200)
# Set first half of the values to 1; some will be centered at zero, and others will be at 1
y[:50] = 1 
plt.scatter(x[:,0], x[:,1], c=y)
plt.show()


## Histogram ##
# Create 10,000 random numbers
x = np.random.randn(10000)
plt.hist(x)
plt.show()

plt.hist(x, bins=50) # create more bars to help view
plt.show()

# uses the “continuous uniform” distribution instead
x = np.random.random(10000) 
plt.hist(x, bins=50)
plt.show()