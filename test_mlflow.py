import mlflow

# Connect to MLflow server
mlflow.set_tracking_uri("http://127.0.0.1:5000")

# Set experiment
mlflow.set_experiment("warehouse_robot_v1")

# Start a run and log
with mlflow.start_run(run_name="quick_test"):
    mlflow.log_param("test", 123)
    mlflow.log_metric("score", 0.99)
    
print("✓ Run logged successfully!")
print("✓ Check browser at: http://127.0.0.1:5000")