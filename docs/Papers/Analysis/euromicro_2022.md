# Paper Analysis: Euromicro SEAA 2022
## *Anomaly Detection in Cloud-Native Systems*

### 1. Simple Summary
This paper specifically tests **8 different AI algorithms** to see which one is best at catching problems in cloud systems (like Kafka and Zookeeper). It found that AI can be incredibly accurate (over 95%) and very fast to train.

### 2. Core Technical Concepts
- **KPI Dependency:** It studied how 5 major "Key Performance Indicators" depend on 168 smaller metrics. 
- **Algorithm Performance:** It tested 8 models and found that training took only 8-17 minutes—proving that you don't need a supercomputer to run AIOps.
- **Accuracy:** Accomplished a 95% AUC (Area Under Curve), which is a very high score for real-world production data.

### 3. Relevance to AIONYX
- **Metric Selection:** The paper lists **168 metrics**. We can use this list to decide exactly which Postgres columns and Dagster assets to prioritize.
- **Algorithm Choice:** Since they found that training is fast, it justifies why AIONYX can run its ML models directly on a small Kubernetes node rather than needing a massive expensive server.

### 4. Key Takeaway for Your Thesis
Cite this in your "Data Science" chapter to justify your choice of metrics. It provides the "Scientific Approval" for using standard infrastructure metrics (CPU, Memory, Latency) as the primary inputs for your AI.
