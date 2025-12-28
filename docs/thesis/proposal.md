# AIONYX: Project Proposal (Thesis + Business)

## 1. Executive Summary
**AIONYX** is a data-driven AIOps platform designed to provide predictive reliability and cost efficiency for Kubernetes environments. It bridges the gap between infrastructure automation and machine learning, offering a system that moves beyond reactive monitoring into proactive operations.

## 2. The Vision: "Lean & Mean" AIOps
As a one-person project on a student budget, AIONYX focuses on a **Zero-Cost, High-Impact** stack. We use the best open-source tools to build a system that rivals expensive commercial alternatives (Datadog, Dynatrace).

### Core Research Question (Thesis)
*How can a software-defined ingestion pipeline (Dagster) and machine learning models (AIOps) be used to predict Kubernetes node failures 30 minutes before they occur?*

## 3. Implementation Strategy (The "Solo" Plan)
To succeed as a single developer, the project is scoped around a single "Killer Feature": **Predictive Anomaly Detection**.

### Phase 1: Local Foundation (Month 1-2)
- **Environment**: Use `Kind` or `Minikube` (Free) instead of expensive cloud clusters.
- **Ingestion**: Dagster assets pulling `container_cpu_usage_seconds_total` and `container_memory_working_set_bytes`.
- **Storage**: Postgres (Standard) or TimescaleDB (vial Docker - Free).

### Phase 2: Data & ML (Month 3-4)
- **Feature Engineering**: Transform raw metrics into time-series features (Rolling mean, Std dev, Rate of change).
- **Model**: Start with **Isolation Forest** (Unsupervised) to detect outliers, then move to **LSTMs** if time permits.
- **Labels**: Use your internship experience to "inject" failures (Stress tests) to create a labeled dataset for free.

### Phase 3: Business MVP (Month 5-6)
- **Alerting**: Simple Slack/Discord integration (Free).
- **Dashboard**: Use Dagster's built-in UI (Dagit) as your first "product" interface—no custom frontend needed yet.

## 4. Zero-Cost Market Standard Stack
| Function | Tool | Commercial Equivalent | Cost |
| :--- | :--- | :--- | :--- |
| **Orchestration** | Dagster | Airflow/Prefect | $0 |
| **Database** | Postgres | Snowflake/Databricks | $0 |
| **Compute** | Local K8s (Kind) | EKS/GKE | $0 |
| **CI/CD** | GitHub Actions | Jenkins/CircleCI | $0 ($2k free mins) |
| **Infrastructure** | Terraform | Manual Config | $0 |
| **ML Framework** | Scikit-learn/PyTorch| SageMaker | $0 |

## 5. Business Path: From Thesis to Startup
1. **Open Source (The "Lead Magnet")**: Release the core Dagster assets as a public repo. This builds your brand name in the DevOps community.
2. **Productize**: Offer a "Cloud Agent" that small startups can drop into their clusters to get instant ML insights without setting up Dagster themselves.
3. **Target Market**: Startups with < 50 nodes who cannot afford $5,000/month Datadog bills.

## 6. Milestones & Deliverables
- **M1**: Reproducible local K8s + Dagster + Postgres environment (Infrastructure).
- **M2**: Automated data ingestion and "Feature Store" populated with simulated failures.
- **M3**: Trained ML model with > 80% precision on failure prediction.
- **M4**: Final Thesis at Malmö University + Open Source MVP launch.

---
**Prepared by**: [User Name]
**Academic Advisor**: Your AI Professor
**Date**: December 2025
