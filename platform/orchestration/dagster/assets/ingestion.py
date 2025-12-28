from dagster import asset, ResourceParam
import pandas as pd
from datetime import datetime

@asset(group_name="ingestion", compute_kind="python")
def raw_kubernetes_metrics() -> pd.DataFrame:
    """
    Mock asset representing raw metrics pulled from Prometheus/Kubernetes.
    In production, this would use a Prometheus API client.
    """
    # Simulate some data for now
    data = {
        "timestamp": [datetime.now() for _ in range(5)],
        "node_name": ["node-1", "node-2", "node-1", "node-3", "node-2"],
        "metric_name": ["cpu_usage", "memory_usage", "cpu_usage", "cpu_usage", "memory_usage"],
        "value": [0.45, 0.78, 0.42, 0.91, 0.82]
    }
    return pd.DataFrame(data)

@asset(group_name="ingestion", compute_kind="python")
def raw_kubernetes_logs() -> pd.DataFrame:
    """
    Mock asset representing logs pulled from Kubernetes API or ELK.
    """
    data = {
        "timestamp": [datetime.now() for _ in range(3)],
        "pod_name": ["api-pod", "db-pod", "auth-pod"],
        "log_level": ["INFO", "ERROR", "INFO"],
        "message": ["Server started", "Connection failed", "User logged in"]
    }
    return pd.DataFrame(data)
