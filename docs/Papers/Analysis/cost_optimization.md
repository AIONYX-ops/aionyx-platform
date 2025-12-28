# Paper Analysis: Kubernetes Cost Optimization
## *Strategies and Best Practices (Kubegrade Summary)*

### 1. Simple Summary
Cloud bills are the #1 nightmare for CFOs. This document explains the "Three Pillars" of saving money on Kubernetes: Right-Sizing, Autoscaling, and Spot Instances.

### 2. Core Technical Concepts
- **Right-Sizing:** Most pods are assigned 2GB of RAM but only use 200MB. Reducing this "Requested" resource is the fastest way to save money.
- **Autoscaling (HPA, VPA, Cluster):** Using the three types of K8s autoscalers together ensure you only pay for what you use *at that exact second*.
- **FinOps:** Bringing Finance and Engineering teams together to look at the same data.

### 3. Relevance to AIONYX
- **The "Business Goal":** One of AIONYX's core modules will be a "Cost Predictor." We will use these strategies to give users recommendations like: *"Your API pod is over-provisioned; you could save $200/month by reducing it."*
- **The "Winning Metric":** In your thesis, don't just measure "Accuracy." Measure **"Dollars Saved."** That is what gets you hired and gets you investors.

### 4. Key Takeaway for Your Thesis
Use this for your "Business Context" or "Cost Evaluation" section. It gives you the "Industry Standard" benchmark (70-80% utilization) to compare your AIONYX results against.
