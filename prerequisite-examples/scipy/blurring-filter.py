# Use Convolution to apply a blurring filter on an image
# The gaussian filter is basically a 2D spherical gaussian, with some constants we ignore.
import numpy as np
import matplotlib.pyplot as plt
from scipy.stats import norm
from scipy.signal import convolve2d
from PIL import Image

# Import image
im = Image.open('Lenna.png')

# Convert image to grayscale, use only two dimensions of color
gray = np.mean(im, axis =2) 

# Return evenly spaced numbers over a specified interval
x = np.linspace(-6,6,50) 

# Generate the Probability Density Function
fx = norm.pdf(x, loc=0, scale=1) 

# Create filter
filt = np.outer(fx, fx) 

# Apply  function
out = convolve2d(gray, filt) 

# Plot original image, and new blur image side-by-side
# Two plots, thing in first position
plt.subplot(1,2,1)
plt.imshow(gray, cmap='gray')

# Two plots, thing in second position
plt.subplot(1,2,2)
plt.imshow(out, cmap='gray')

plt.show()