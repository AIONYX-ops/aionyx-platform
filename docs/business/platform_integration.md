# AIONYX: Integration Guide (GitHub & Hugging Face)

To build a professional identity for AIONYX, you need to sync your **Code (GitHub)** with your **Models (Hugging Face)**. Here is how to do it efficiently without creating unnecessary accounts.

## 1. Do you need a new Hugging Face Account?
**No.** You do not need a new personal login.
- **The Strategy:** Much like GitHub, Hugging Face has **Organizations**.
- **Action:** Keep your personal account, but create a new **Organization** named `aionyx` or `aionyx-ai`.
- **Benefit:** You can be the "Owner" of the AIONYX organization using your existing account. This keeps your personal profile and your professional work separate but managed from one login.

### Which Organization Type to choose?
When creating the organization on Hugging Face, you will see several options. Here is the best choice for your situation:

| Type | Choice | Why? |
| :--- | :---: | :--- |
| **Company** | **Recommended** | This is the most professional option. It signals to investors and customers that AIONYX is a serious venture. You don't need a registered legal entity yet to select this. |
| **Community** | No | Good for general open-source groups, but less "startup-ready." |
| **University** | No | AIONYX is your personal project, not an official university department. |
| **Non-Profit** | No | Only if you don't plan to ever make money from it. |

> [!TIP]
> Choose **Company**. It allows you to build a brand now that you can legally register later without changing your Hugging Face identity.
There are two ways to connect them, depending on your workflow:

### A. The "Syncing" Method (Recommended)
You can set up your Hugging Face space or model repository to automatically "mirror" a GitHub repository.
1.  **Create a Repository** in your GitHub Organization (e.g., `aionyx-hq/anomaly-detection`).
2.  **Create a Model/Space** in your Hugging Face Organization.
3.  **Link them:** In Hugging Face settings, go to "Connected Accounts" or use the "GitHub Sync" feature to automatically pull code from GitHub whenever you push.

### B. The "CI/CD" Method (Advanced)
Use **GitHub Actions** to automatically upload models to Hugging Face after a successful training run in Dagster.
1.  Generate a **Hugging Face Access Token** (Write permission).
2.  Add it as a **Secret** in your GitHub Organization.
3.  Add a step in your `.github/workflows/deploy.yml` to push the model artifact to Hugging Face.

## 3. Step-by-Step Setup Checklist

1.  **On GitHub:**
    - Create a GitHub Organization: [github.com/organizations/plan](https://github.com/organizations/plan).
    - Invite your personal account as the "Owner."

2.  **On Hugging Face:**
    - Create an Organization: [huggingface.co/organizations/new](https://huggingface.co/organizations/new).
    - Invite your personal account as the "Admin."

3.  **Link the Two:**
    - **Step 1:** Create your Space or Model repository on Hugging Face first (as a "Static" space).
    - **Step 2:** Once created, click on the **"Settings"** tab at the top of that specific Space/Model page.
    - **Step 3:** Scroll down to the **"GitHub Mirroring"** or **"Repository Mirroring"** section.
    - **Step 4:** Follow the instructions there to add your GitHub repository URL and a "Mirroring Token" from GitHub.
    - **Method 2 (The Pro Way):** Use **GitHub Actions**. This is what most startups do. It pushes your code from GitHub to Hugging Face automatically whenever you save. We will set this up together in the "CI/CD" phase.

## 4. Why this matters for the Thesis & Business
- **For the Thesis:** It shows you understand **Data Provenance**. You have the code on GitHub and the resulting model on Hugging Face, linked together.
- **For the Business:** It creates a "Hugging Face Portfolio." When someone searches for "AIOps" on Hugging Face, they will find your organization and your high-quality, documented models.
