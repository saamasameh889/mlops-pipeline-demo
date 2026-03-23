

run_id = "demo-run-12345"
accuracy = 0.70

with open("model_info.txt", "w") as f:
    f.write(run_id)

print("Run ID:", run_id)
print("Accuracy:", accuracy)
print("Created model_info.txt")
