import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

df = pd.read_csv('twitter_2022midterm_us_governors.csv', index_col=[0])
print(df.head())