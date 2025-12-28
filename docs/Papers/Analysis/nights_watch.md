# Paper Analysis: The Night's Watch Algorithm
## *AI-Driven Anomaly Detection in Cloud-Native Microservices*

### 1. Simple Summary
Named after the watchers in "Game of Thrones," this algorithm is designed to stay awake and watch your microservices 24/7. Its main job is to solve "Alert Fatigue"—the problem where engineers get so many fake alerts that they start ignoring the real ones.

### 2. Core Technical Concepts
- **Unsupervised Learning:** It doesn't need a human to tell it "this is a crash." It learns what "Wednesday afternoon traffic" looks like vs "Saturday night traffic" automatically.
- **Temporal Coherence:** It looks at the *order* of events. If A normally happens before B, and suddenly B happens before A, it knows something is wrong.
- **Multi-Source Data:** It combines logs (text) + metrics (numbers) + alarms to get a full picture.

### 3. Relevance to AIONYX
- **The "Truth" Filter:** We will use the Night's Watch philosophy to ensure AIONYX doesn't "cry wolf." This is our #1 selling point for the business: **Trusted Alerts.**
- **Feature Engineering:** The way they combine logs and metrics is exactly how we should design our Dagster processing assets.

### 4. Key Takeaway for Your Thesis
This paper is perfect for your "Methodology" chapter. You can explain how AIONYX uses temporal coherence to detect subtle anomalies that simple thresholds (like "CPU > 80%") would miss.
