import pandas as pd

df = pd.read_csv('DATA/titanic3.csv')

print(df.head())

print(df.info())

print(df.fare.value_counts())

print(df.sex.value_counts())

print(df.embarked.value_counts())
