import numpy as np
import pandas as pd
import matplotlib.pyplot as plt

df = pd.read_csv('data_1d.csv', header = None)
X = df[0].values
Y = df[1].values

plt.scatter(X, Y)
plt.show()
