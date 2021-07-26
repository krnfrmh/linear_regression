import numpy as np
import pandas as pd
import matplotlib.pyplot as plt

# load the data
df = pd.read_csv('data_1d.csv', header = None)
X = df[0].values
Y = df[1].values

# plot the data
plt.scatter(X, Y)
plt.show()

# apply the equations we learned to calculate a and b
# Numpy representation of Mathematic equations derived
# denominator is common so computing once
denominator = X.dot(X) - X.mean() * X.sum()
a = ( X.dot(Y) - Y.mean() * X.sum() ) / denominator
b = ( Y.mean() * X.dot(X) - X.mean() * X.dot(Y) ) / denominator

# calculate the predicted Y
Yhat = a * X + b

# plot everything together to make sure it worked
plt.scatter(X, Y)
plt.plot(X, Yhat)
plt.show()
