#import numpy as np
import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.ensemble import RandomForestRegressor
# This program uses regression method of ML
# Using airfoil data from here : https://archive.ics.uci.edu/ml/datasets/Airfoil+Self-Noise

# load the data
df = pd.read_csv('https://archive.ics.uci.edu/ml/machine-learning-databases/00291/airfoil_self_noise.dat', sep='\t', header=None)

# split the data from the target values
data = df[[0,1,2,3,4]].values
target = df[5].values

# split up the testing and training data
X_train, X_test, y_train, y_test = train_test_split(data, target, test_size=0.33)

# train the model
model = RandomForestRegressor()
model.fit(X_train, y_train)

# score the model
train_score = model.score(X_train, y_train)
test_score = model.score(X_test, y_test)


print("R^2 score for training:", train_score)
print("R^2 score for testing:", test_score)

# Use the model to do a prediction
prediction = model.predict(X_test[[5]])

print('\n' + "Predcition of the first element - ")
print("Expected result:", prediction[0])
print("Model prediction:", y_test[5])