import os
import sys
import mlflow

THRESHOLD = 0.85

def main():
    tracking_uri = os.environ.get("MLFLOW_TRACKING_URI")
    if not tracking_uri:
        print("MLFLOW_TRACKING_URI is not set.")
        sys.exit(1)

    mlflow.set_tracking_uri(tracking_uri)

    if not os.path.exists("model_info.txt"):
        print("model_info.txt not found.")
        sys.exit(1)

    with open("model_info.txt", "r") as f:
        run_id = f.read().strip()

    if not run_id:
        print("Run ID is empty.")
        sys.exit(1)

    run = mlflow.get_run(run_id)
    metrics = run.data.metrics

    accuracy = metrics.get("accuracy")
    if accuracy is None:
        print(f"No 'accuracy' metric found for run {run_id}.")
        sys.exit(1)

    print(f"Run ID: {run_id}")
    print(f"Accuracy: {accuracy:.4f}")
    print(f"Threshold: {THRESHOLD:.2f}")

    if accuracy < THRESHOLD:
        print("Accuracy is below threshold. Failing deployment.")
        sys.exit(1)

    print("Accuracy passed threshold. Proceeding to deployment.")

if __name__ == "__main__":
    main()
