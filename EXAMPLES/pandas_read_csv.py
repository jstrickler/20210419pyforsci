import pandas as pd

df = pd.read_csv('../DATA/sales_records.csv')  # <.>

print(df.head())  # <.>

print(df.describe())  # <.>
print()

print(df.info())  # <.>
print()


print(df['Unit Price'])
