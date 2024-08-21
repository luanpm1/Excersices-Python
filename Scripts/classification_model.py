import pandas as pd
from ydata_profiling import ProfileReport
from sklearn.model_selection import train_test_split
from sklearn.preprocessing import StandardScaler
from sklearn.ensemble import RandomForestClassifier
from sklearn.metrics import classification_report
from sklearn.linear_model import LogisticRegression
from sklearn.model_selection import GridSearchCV
from lazypredict.Supervised import LazyClassifier

target = "Outcome"
data = pd.read_csv("diabetes.csv")
x = data.drop(target, axis=1)
y = data[target]

# profile = ProfileReport(data, title="Diabetes Report")
# profile.to_file("report.html")

x_train, x_test, y_train, y_test = train_test_split(x, y, test_size=0.2, random_state=42, stratify=y)
# print(y_train.value_counts())
# print(y_test.value_counts())
scaler = StandardScaler()
x_train = scaler.fit_transform(x_train)
x_test = scaler.transform(x_test)

clf = LazyClassifier(verbose=0, ignore_warnings=True, custom_metric=None)
models, predictions = clf.fit(x_train, x_test, y_train, y_test)

# params = {
#     "n_estimators": [50, 100, 200],
#     "criterion": ["gini", "entropy", "log_loss"],
#     "max_depth": [None, 2, 5, 10]
# }
#
# model = GridSearchCV(
#     estimator=LogisticRegression(random_state=2024),
#     param_grid=params,
#     scoring="recall",
#     cv=6,
#     verbose=2,
#     n_jobs=-1
# )
# model.fit(x_train, y_train)
# print(model.best_estimator_)
# print(model.best_score_)
# print(model.best_params_)
# y_predict = model.predict(x_test)
# print(classification_report(y_test, y_predict))
