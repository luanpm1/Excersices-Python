import pandas as pd



df = pd.read_csv("diabetes.csv")
print(df.to_string)

stats = df.describe()
