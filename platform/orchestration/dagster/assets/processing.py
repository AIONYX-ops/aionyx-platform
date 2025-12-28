from dagster import asset
import pandas as pd

@asset(deps=["raw_kubernetes_metrics"], group_name="processing")
def feature_cpu_usage(raw_kubernetes_metrics: pd.DataFrame) -> pd.DataFrame:
    """
    Transform raw metrics into features. 
    In a real scenario, this would compute rolling averages, 
    detect spikes, or perform normalization.
    """
    df = raw_kubernetes_metrics[raw_kubernetes_metrics["metric_name"] == "cpu_usage"].copy()
    # Mock feature engineering: normalized value and rolling mean
    df["rolling_mean"] = df["value"].rolling(window=2, min_periods=1).mean()
    return df

@asset(deps=["feature_cpu_usage"], group_name="processing")
def anomaly_labels(feature_cpu_usage: pd.DataFrame) -> pd.DataFrame:
    """
    Simulate manual or automated labeling for supervised learning.
    """
    df = feature_cpu_usage.copy()
    df["label"] = df["value"].apply(lambda x: "anomaly" if x > 0.9 else "healthy")
    return df
