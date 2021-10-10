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
