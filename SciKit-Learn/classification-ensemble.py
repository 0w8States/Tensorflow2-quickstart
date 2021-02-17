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


# pick a model, here we use the RandomForestClassifier
from sklearn.ensemble import RandomForestClassifier
# RandomForestClassifier is an object, not a function, so lets instantiate it
model = RandomForestClassifier()
# train the model
model.fit(X_train, y_train)

# evalutae it's performance
train_score = model.score(X_train, y_train)
test_score = model.score(X_test, y_test)

# How to make predicitions?
# Here we use X_test again, but you can use any data you want to see a prediction
predicitions = model.predict(X_test)

# You can also manually check the accuacy like this
N = len(y_test)
predict_score = np.sum(predicitions == y_test) / N


# Print the results
print("Training accuracy:", train_score)
print("Testing accuracy:", test_score)
print("Prediction result", predict_score)