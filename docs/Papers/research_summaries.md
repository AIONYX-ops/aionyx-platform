# Research Paper Summaries: The "AIONYX" Knowledge Base

I have analyzed the research papers and books found in your `docs/Papers` folder. Below is a simplified explanation of the most important ones and how they help you built **AIONYX**.

---

## 🔝 The "Must-Reads" for Your Project

### 1. Site Reliability Engineering (The Google SRE Book)
**What it is:** The "Bible" of how Google keeps its systems running.
**Simple Explanation:** It teaches you that "100% uptime" is a mistake. Instead, you should have an "Error Budget" and use automation (SRE) to manage reliability.
**Relevance to AIONYX:** This gives you the *language* to talk to customers. You don't just sell "uptime"; you sell "Error Budget Management" and "Toil Reduction."

### 2. DeepContainer: Real-time Anomaly Detection
**What it is:** A paper about using Deep Learning to watch containers in Kubernetes.
**Simple Explanation:** It uses a "multi-layered" approach to catch security problems and resource exhaustion. It’s very fast (under 10ms) and very accurate.
**Relevance to AIONYX:** This is your primary competitor/inspiration. It proves that real-time detection in K8s is possible and highly effective.

### 3. MicroRCA: Root Cause Analysis
**What it is:** A famous paper on finding out *why* a microservice failed.
**Simple Explanation:** It looks at the dependencies between services (like a map) to find the "patient zero" of a failure.
**Relevance to AIONYX:** You can use this logic in your "Root Cause" dashboard to tell users exactly which pod started the problem.

### 4. The Night's Watch Algorithm (applsci-15-12762)
**What it is:** A very recent (2025 style) AI-driven algorithm for microservices.
**Simple Explanation:** It's called "unsupervised," meaning it learns what "normal" looks like on its own without you having to tell it. It reduces "False Alarms" (annoying alerts that aren't real problems).
**Relevance to AIONYX:** This is a key feature for your business. Customers hate annoying alerts. The "Night's Watch" approach helps AIONYX be a "quiet" and "trusted" advisor.

### 5. MicroRCA-Agent (2509.15635v1 - The Latest Tech)
**What it is:** Using **Large Language Models (LLMs)** like me to do the analysis.
**Simple Explanation:** It uses "Agents" to read logs and metrics together and then writes a report in plain English explaining the fault.
**Relevance to AIONYX:** This is the future of your project! Instead of just a graph, AIONYX can provide a "Human-like" report to the SRE: *"Hey, I think Pod-B is failing because the database is slow."*

---

## 💰 The Business Value Papers

### Kubernetes Cost Optimization (Kubegrade Summary)
**Simple Explanation:** Focuses on "Right-Sizing." Most companies buy "Extra Large" servers but only use 10% of them.
**Relevance to AIONYX:** This is how you make money. Your thesis will show that AIONYX "recommends" the perfect size, saving the company 30-50% on their bill.

---

## 🛠 What to look for when you study these:

1.  **"Grey Failures":** Look for how they find problems where the pod is still "Running" but the user is unhappy (slow latency).
2.  **"Causal Graphs":** Look at how they draw lines between services to show who depends on who.
3.  **"Precision vs. Recall":** In your thesis, don't just say "It works." Use these terms. *Precision* means "When I say it's an anomaly, am I right?" *Recall* means "Did I catch ALL the anomalies?"

---

### 📝 Summary of Relevance Table

| Topic | Paper/Book | Use for AIONYX |
| :--- | :--- | :--- |
| **Terminology** | Google SRE Book | Writing your Introduction. |
| **Detection Logic** | DeepContainer / Night's Watch | Defining your ML models. |
| **Root Cause** | MicroRCA / GRALAF | Designing your Dashboard. |
| **The "Future"** | MicroRCA-Agent (LLMs) | Making AIONYX a premium product. |
| **Money/Value** | Kubegrade | Writing your Business Case. |

---

**Professor's Tip:** You don't need to read every page of these 17 PDFs. Read the **Abstract**, the **Introduction**, and the **Conclusion** first. If it feels relevant, look at the **Methodology** section to see what metrics (CPU, RAM, Latency) they used.
