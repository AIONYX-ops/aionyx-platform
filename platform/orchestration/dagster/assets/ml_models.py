from dagster import asset
import pandas as pd

@asset(deps=["anomaly_labels"], group_name="ml")
def trained_anomaly_model(anomaly_labels: pd.DataFrame):
    """
    Mock asset representing the training of an ML model.
    In production, this would use scikit-learn/PyTorch and save to model_registry.
    """
    # Simulate training logic
    model_info = {
        "model_type": "IsolationForest",
        "precision": 0.85,
        "recall": 0.72,
        "features_used": ["cpu_usage", "rolling_mean"]
    }
    return model_info
