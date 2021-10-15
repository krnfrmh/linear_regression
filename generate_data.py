import numpy as np
import pandas as pd

def gen_1d_data(N):
  X = np.random.uniform(low=0, high=100, size=N)
  Y = 2*X + 1 + np.random.normal(scale=5, size=N)
  df = pd.DataFrame({'X': X, 'Y': Y})
  df.to_csv('data_1d.csv', index = False, header = False)
  
def gen_2d_data(N):
  w = np.array([2, 3])
  X = np.random.uniform(low=0, high=100, size=(N,2))
  Y = np.dot(X, w) + 1 + np.random.normal(scale=5, size=N)
  df = pd.DataFrame({'feat_0': X[0], 'feat_1': X[1], 'Y': Y})
  df.to_csv('data_2d.csv', index = False, header = False)
  
if __name__ == '__main__':
  gen_1d_data(100)
#   gen_2d_data(100)
