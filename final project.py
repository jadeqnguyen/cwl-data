import pandas as pd

dataset_1 = pd.read_csv('vgsales.csv')
dataset_2 = pd.read_csv('vgsales-12-4-2019-short.csv')
dataset_3 = pd.read_csv('vgsales-12-4-2019.csv')

# print(dataset_1.columns)
# print(dataset_2.columns)
print(dataset_3.columns)