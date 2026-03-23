import os
import mlflow
from sklearn.datasets import load_iris
from sklearn.model_selection import train_test_split
from sklearn.ensemble import RandomForestClassifier
from sklearn.metrics import accuracy_score

mlflow.set_tracking_uri(os.environ["MLFLOW_TRACKING_URI"])

X, y = load_iris(return_X_y=True)
X_train, X_test, y_train, y_test = train_test_split(
    X, y, test_size=0.2, random_state=42
)

with mlflow.start_run():
    clf = RandomForestClassifier(n_estimators=10, random_state=42)
    clf.fit(X_train, y_train)

    preds = clf.predict(X_test)
    accuracy = accuracy_score(y_test, preds)

    mlflow.log_param("model_type", "RandomForestClassifier")
    mlflow.log_metric("accuracy", accuracy)

    print(f"Accuracy: {accuracy:.4f}")
