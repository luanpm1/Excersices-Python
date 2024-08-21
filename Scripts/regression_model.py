import pandas as pd
from sklearn.model_selection import train_test_split
from ydata_profiling import ProfileReport
from sklearn.pipeline import Pipeline
from sklearn.impute import SimpleImputer
from sklearn.preprocessing import StandardScaler, OrdinalEncoder, OneHotEncoder

data = pd.read_csv("StudentScore.xls")
# profile = ProfileReport(data, title="StudentScore Report")
# profile.to_file("StudentScore.html")
target = "math score"
x = data.drop(target, axis=1)
y = data[target]

x_train, x_test, y_train, y_test = train_test_split(x, y, test_size=0.2,  random_state=42)

num_transformer = Pipeline(steps=[
    ("imputer", SimpleImputer(strategy="median")),
    ("scaler", StandardScaler())
])

education_levels = ["some high school", "high school", "some college", "associate's degree", "bachelor's degree",
                    "master's degree"]
ord_transformer = Pipeline(steps=[
    ("imputer", SimpleImputer(strategy="most_frequent")),
    ("encoder", OrdinalEncoder(categories=[education_levels]))
])

nom_transformer = Pipeline(steps=[
    ("imputer", SimpleImputer(strategy="most_frequent")),
    ("encoder", OneHotEncoder(sparse_output=False))
])


result = nom_transformer.fit_transform(x_train[["race/ethnicity"]])
for i, j in zip(x_train[["race/ethnicity"]].values, result):
    print("Before: {}. After: {}".format(i, j))