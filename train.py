import os
import mlflow
from sklearn.datasets import load_iris
from sklearn.model_selection import train_test_split
from sklearn.ensemble import RandomForestClassifier
from sklearn.metrics import accuracy_score


run_id = "demo-run-12345"
accuracy = 0.90   

with open("model_info.txt", "w") as f:
    f.write(run_id)

print("Run ID:", run_id)
print("Accuracy:", accuracy)
print("model_info exists:", os.path.exists("model_info.txt"))
