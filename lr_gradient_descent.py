import numpy as np
import matplotlib.pyplot as plt

N = 10
D = 3

# Generate dummy data
X = np.zeros((N, D))
X[:,0] = 1 # bias term
X[:5,1] = 1
X[5:,2] = 1
Y = np.array([0]*5 + [1]*5)

costs = []
w = np.random.randn(D) / np.sqrt(D) # randomly initialize w
learning_rate = 0.001
for t in range(1000):
  Yhat = X.dot(w)
  delta = Yhat - Y
  # weight update
  w = w - learning_rate*X.T.dot(delta)
  
