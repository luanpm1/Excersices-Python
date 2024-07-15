import pandas as pd



df = pd.read_csv("diabetes.csv")
stats = df.describe()
