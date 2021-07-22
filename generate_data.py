import numpy as np
import pandas as pd

def generate_1d_data(N):
  X = np.random.uniform(low=0, high=100, size=N)
  Y = 2*X + 1 + np.random.normal(scale=5, size=N)
  df = pd.DataFrame({'X': X, 'Y': Y})
  df.to_csv('data_1d.csv', index = False, header = False)
  
if __name__ == '__main__':
  generate_1d_data(100)
