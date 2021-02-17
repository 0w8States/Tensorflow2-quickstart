# Same example as classification.py, except using a deep learning neural network
# In this example, we train a model to do classification on breast cancer datasets
import numpy as np

# import the built-in dataset for breast cancer classification
from sklearn.datasets import load_breast_cancer

# load the data
data = load_breast_cancer()

# We typically split the data into training and test sets
# Make sure the data you test on is different from the data you train on
# It could simply be that the model has memorized the data you've used in the past, and that would end with a lookup table
# The goal is to predict things you have not seen, not just repeat past things

from sklearn.model_selection import train_test_split
# split up the dataset
X_train, X_test, y_train, y_test = train_test_split(data.data, data.target, test_size=0.33)


from sklearn.neural_network import MLPClassifier
from sklearn.preprocessing import StandardScaler

# Scale the inputs
scaler = StandardScaler()
# fit function, and transform function
X_train2 = scaler.fit_transform(X_train)
X_test2 = scaler.transform(X_test)

# If you get "hadn't converged" warning, make it train longer with max_iter
model = MLPClassifier(max_iter=500) 
model.fit(X_train2, y_train)

# Evaluate the success
train_score = model.score(X_train2, y_train)
test_score = model.score(X_test2, y_test)


# Print the results
print("Training accuracy:", train_score)
print("Testing accuracy:", test_score)