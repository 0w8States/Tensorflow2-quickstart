# Demo of how to import and plot a standard image
import numpy as np
import matplotlib.pyplot as plt
from PIL import Image

# Import the famous Lenna image
im = Image.open('Lenna.png')


# Convert the image to numpy array
arr = np.array(im) 

# Plot the image
plt.imshow(arr)
plt.show()

# Convert to grayscale by taking the mean accross the array

# These are not actually colors stored within the image, they are just numbers from 0 to 255
# What we've actually created here is an image heatmap
# 
# The number generated depend on numpy, or whatever other program you are using
gray = arr.mean(axis=2)
plt.imshow(gray) 
plt.show()

 # Finish the grayscale conversion - Apply a Colormap
plt.imshow(gray, cmap='gray')
plt.show()
