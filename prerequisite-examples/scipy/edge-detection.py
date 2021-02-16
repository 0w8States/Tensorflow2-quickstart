# In this example we do a few things to detect the edge
# 1. We define two filers (aka sobel filters) called Hx, Hy
# 2. We perform a convolution on Hx and Hy to get Gx, Gy
# 3. From there we calculate the edge detection output and solve for G


import numpy as np
import matplotlib.pyplot as plt
from PIL import Image
from scipy.signal import convolve2d


# Import the image
im = Image.open('Lenna.png')


Hx = np.array([[1,0,-1],[2,0,-2],[1,0,-1]]) # Filter 1
Hy = np.array([[1,2,1],[0,0,0],[-1,-2,-1]]) # Filter 2

 # Convert image to grayscale, use only two dimensions of color
gray = np.mean(im, axis =2)

# Apply convolution function
Gx = convolve2d(gray, Hx) 
Gy = convolve2d(gray, Hy)

# Solve for G
G = np.sqrt((Gx**2)+(Gy**2))

# Plot original image, and new blur image side-by-side
# Two plots, thing in first position
plt.subplot(1,2,1)
plt.imshow(im)

# Two plots, thing in second position
plt.subplot(1,2,2)
plt.imshow(G, cmap='gray')
plt.show()