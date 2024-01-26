import matplotlib.pyplot as plt
import pandas as pd
import numpy as np

file_path = "/Users/jakobsmac/Public/git/physics_simulations/heart+disease/processed.switzerland.data"

df = pd.read_csv(file_path, header = None)

plt.scatter(df[0], df[7])
plt.xlabel('age')
plt.ylabel('max heart rate')
plt.title('Heartare data from a test in switzerland')
plt.show()