# This program does the following to create a Donut Dataset, A.k.a concentric circles dataset
# Generate and array with x1 and x2 datapoints
# Completes the quadratic feature expansion

import numpy as np
import pandas as pd
import matplotlib.pyplot as plot

# Function to generate datapoints
def create_donut(radius, size):
    # assume that arr is in polar coordinates
    arr = np.array([np.linspace(0, 2 * np.pi, size), np.random.randn(size)]).T + radius
    cartesian_arr = np.array([arr[:, 1] * np.cos(arr[:, 0]), arr[:, 1] * np.sin(arr[:, 0])]).T
    return cartesian_arr

# Function to square values
def square_x1(row):
  return float(row['x1']**2) # select only the year, 0th element in this case

def square_x2(row):
  return float(row['x2']**2) # select only the year, 0th element in this case

# Function to multiply values
def multiply_x1x2(row):
  return float(row['x1'] * row['x2']) # select only the year, 0th element in this case

# Generate numpy arrays
outerCircle = create_donut(10, 5000)
innerCircle = create_donut(5, 5000)

# Outer donut dataframe
dfo = pd.DataFrame(outerCircle, columns=["x1", "x2"])
dfo["y"] = 1

# Inner donut dataframe
dfi = pd.DataFrame(innerCircle, columns=["x1", "x2"])
dfi["y"] = 0

# Generate DataFrame for result csv
df = pd.concat([dfi, dfo], ignore_index=True)

# Apply quadratic feature expansion
df["x1^2"] = df.apply(square_x1, axis=1)
df["x2^2"] = df.apply(square_x2, axis=1)
df["x1*x2"] = df.apply(multiply_x1x2, axis=1)



# Rearrange columns
df = df[["x1", "x2", "x1^2", "x2^2", "x1*x2", "y"]]

# (Optional) Shuffle to mix up "y" values
# df = df.sample(frac=1.0)

# Export to CSV
df.to_csv("result.csv", header=True, index=False)

# Plot
ax = dfo.plot(x=0, y=1, kind="scatter", color="blue")
dfi.plot(x=0, y=1, kind="scatter", color="red", ax=ax, figsize=(15, 15), legend=False)
plot.show()
