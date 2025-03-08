# AIEngineerCICD

## Simple ML Project with Iris Classification to Work with CI/CD Pipelines

This is a simple Machine Learning project in Python using the Iris dataset. The project covers data loading, processing, splitting, training, hyperparameter tuning, and evaluation. It provides a foundation for working with CI/CD pipelines and includes tasks related to adding tests and automating them using GitHub Actions.

## Project Overview

The project uses `scikit-learn` for the entire ML pipeline, which includes:

1. **Data Loading and Processing** (`data_loading.py`)
2. **Model Training and Evaluation** (`model_training.py`)
3. **Hyperparameter Tuning** (`hyperparameter_tuning.py`)
4. **Evaluation** (`evaluation.py`)

You will be tasked with integrating this project into a CI/CD pipeline, writing tests, and automating the entire process using GitHub Actions.

---

### **Project Structure:**

```plaintext
your_project/
├── data_loading.py             # Handles data loading and preprocessing
├── model_training.py           # Handles model training and evaluation
├── hyperparameter_tuning.py    # Performs hyperparameter tuning
├── evaluation.py               # Final model evaluation script
├── tests/                      # Directory containing unit tests
│   ├── test_data_loading.py    # Unit tests for data_loading.py
├── requirements.txt            # Dependencies for the project
└── README.md                   # Project overview and instructions
```


## How to Run the Project Locally

### Clone the Repository:

<pre><code class="bash">
git clone https://github.com/your-username/your-repo.git
cd your-repo
</code></pre>

### Install Dependencies:

<pre><code class="bash">
pip install -r requirements.txt
</code></pre>

### Run the Data Loading and Model Training:

<pre><code class="bash">
python evaluation.py
</code></pre>

### Run Unit Tests:

<pre><code class="bash">
pytest /tests
</code></pre>

## Conclusion

This project offers an introduction to setting up a CI/CD pipeline for a simple machine learning project. 
By completing the tasks, you'll gain experience in automating tests, hyperparameter tuning, and linting 
as part of a continuous integration workflow.

<pre><code class="yaml">
# Example YAML for CI/CD pipeline:
name: ML CI Pipeline

on:
  push:
    branches:
      - main

jobs:
  build:
    runs-on: ubuntu-latest

    steps:
      - uses: actions/checkout@v2
      - name: Set up Python
        uses: actions/setup-python@v2
        with:
          python-version: '3.x'
      - name: Install dependencies
        run: |
          pip install -r requirements.txt
      - name: Run data loading and model training
        run: |
          python data_loading.py
          python model_training.py
</code></pre>
