# Literature Review: AIOps, Predictive Reliability, and Kubernetes

This document serves as the academic foundation for the **AIONYX** thesis. It outlines current research trends, key terminology, and a guide for further study.

## 1. Key Research Areas (What to Study)

To write a high-scoring thesis at Malmö University, you must demonstrate a deep understanding of these four pillars:

### A. AIOps (Artificial Intelligence for IT Operations)
Focus on the transition from "Monitoring" (knowing what happened) to "AIOps" (predicting what will happen).
- **Core Concept:** Multi-source data ingestion (metrics, logs, events) + ML for automated remediation.
- **Key Terms:** MTTR (Mean Time To Recovery), MTBF (Mean Time Between Failures), Noise Reduction, Alert Correlation.

### B. Time-Series Anomaly Detection
Since Kubernetes telemetry is time-sequential, you must study how to detect "out-of-pattern" behavior.
- **Algorithms:** LSTMs (Long Short-Term Memory), Isolation Forests, Autoencoders, and Prophet (by Meta).
- **Sub-topic:** "Grey Failures"—failures that don't trigger a binary health check but degrade performance.

### C. Predictive Infrastructure Scaling
This links your project to **Cost Optimization**.
- **Research focus:** Horizontal Pod Autoscaler (HPA) vs. Predictive Scaling (using ML to scale *before* a spike).
- **Concept:** Trade-offs between "Resource Under-utilization" (waste) and "Service Level Agreement (SLA) Violations" (risk).

### D. Reproducible MLOps in SRE
This is where **Dagster** fits into the research.
- **Focus:** How "Software-Defined Assets" improve the reliability of ML models in production infrastructure.
- **Key Term:** Data Provenance (knowing exactly where your training data came from).

---

## 2. Recommended Search Strategies (Where to Look)

Use these platforms for peer-reviewed, high-impact papers:

1.  **IEEE Xplore / ACM Digital Library:** Search for *"Anomalous behavior detection in Kubernetes"* or *"Deep learning for microservices reliability."*
2.  **Google Scholar:** Use specific queries like: `"AIOps" + "Kubernetes" + "Predictive maintenance"`.
3.  **ArXiv.org (Computer Science section):** For the most cutting-edge (but sometimes unreviewed) papers on AI and Systems.
4.  **Malmö University Library (LibSearch):** Specifically look for previous theses in **Data Science** or **Computer Science** related to "Cloud Computing" or "Monitoring."

---

## 3. High-Value Papers to Find (Search Keywords)

Look for these specific topics to build your bibliography:
- *"MicroRCA: Root Cause Analysis of Microservices in Clusters"* (Very famous paper).
- *"Cloud-native system anomaly detection using deep learning."*
- *"Cost-aware resource management in containerized environments."*
- *The "Google SRE Book"* (Specifically the chapters on Monitoring and Alerting—this is the "Bible" of DevOps).

---

## 4. How to Read for the Thesis

When reading, don't just summarize. **Compare.**
- "Paper A uses LSTMs, but Paper B argues that Isolation Forests are faster for real-time K8s metrics. **AIONYX** will test both to find the best balance for small-scale startups."

> [!TIP]
> Use a tool like **Zotero** or **Mendeley** (both free) to save your papers and automatically generate citations. This will save you weeks of work during the writing phase.
