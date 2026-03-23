

THRESHOLD = 0.85
accuracy = 0.70

with open("model_info.txt", "r") as f:
    run_id = f.read().strip()

print("Run ID:", run_id)
print("Accuracy:", accuracy)

if accuracy < THRESHOLD:
    print("Accuracy below threshold. Failing pipeline.")
    sys.exit(1)

print("Accuracy passed threshold.")
