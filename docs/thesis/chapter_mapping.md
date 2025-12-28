# AIONYX Thesis Alignment Roadmap

As your professor, here is how the repository structure and toolset map directly to your **Master's Thesis chapters** at Malmö University.

| Thesis Chapter | Repository Section | Tool/Tech Focus |
| :--- | :--- | :--- |
| **1. Introduction** | `docs/thesis/proposal.md` | Problem statement, research questions. |
| **2. Background** | `docs/architecture/` | Kubernetes (K8s), AIOps state-of-the-art. |
| **3. Methodology** | `platform/orchestration/` | **Dagster** for reproducible data pipelines. |
| **4. System Design** | `infra/` + `platform/storage/` | **Terraform**, **K8s**, **Postgres** schema. |
| **5. Implementation** | `platform/ml/` | **Python**, **Scikit-learn/PyTorch**. |
| **6. Experiments** | `experiments/notebooks/` | Jupyter, Dataset analysis, Model evaluation. |
| **7. Evaluation** | `docs/thesis/results.md` | Metrics (Precision, Recall, Cost savings). |
| **8. Conclusion** | `docs/business/roadmap.md` | Future outlook (Thesis to Startup transition). |

## Academic Contribution Checklist

- [ ] **Reproducibility**: Guaranteed by the `Dagster` asset definitions and `Terraform` manifests.
- [ ] **Data Quality**: Managed through `Dagster` software-defined assets and type checking.
- [ ] **Novelty**: Applying ML particularly for *proactive* failure detection rather than reactive monitoring.
- [ ] **Validity**: Experimental results backed by the `model_registry` in Postgres.

## Professor's Tip for the Viva (Defense)
When asked about your choice of **Dagster**, explain:
> "I chose Dagster instead of simple scripts because it provides a self-documenting, software-defined asset graph. This ensures that the data used for the thesis results is traceable, reproducible, and verifiable—standard requirements for high-quality scientific research."
