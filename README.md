# 📈 Company Revenue Prediction Pipeline

An end-to-end, production-ready Machine Learning workflow that predicts corporate revenue based on financial metrics and geographical data. 

Instead of treating preprocessing and modeling as disconnected, fragile scripts, this project utilizes a highly modular architecture built with Scikit-Learn **Pipelines** and **ColumnTransformers**. This professional setup guarantees clean data transformation, isolates the training scope to prevent data leakage, and ensures smooth deployment.

---

## ✨ Features

* **Unified Data Pipeline**: Automatically bundles numerical feature standardization (`StandardScaler`) and categorical encoding (`OneHotEncoder`) into a single, cohesive execution graph.
* **Production-Grade Guardrails**: Configures `handle_unknown='ignore'` within the encoder to safely bypass unexpected region queries during live inference without crashing.
* **Modernized Performance Metrics**: Tracks regression performance using future-proof scikit-learn APIs, outputting Mean Absolute Error (MAE), Root Mean Squared Error (RMSE), and R² Score.
* **Interactive CLI Prompt Loop**: Features a terminal interface that allows users to type in manual company parameters with live input-type constraints and exception validations.

---

## 📂 File Structure

```text
revenue-prediction-pipeline/
├── data.csv             # Training and testing historical financial dataset
├── main.py              # Core script (Pipeline architecture & interactive CLI)
└── README.md            # Comprehensive project documentation
```

---

## ⚙️ Installation & Setup

This project requires **Python 3.8+**. Follow these quick steps to get the environment ready:

1. **Clone the repository:**
   ```bash
   git clone https://github.com
   cd revenue-prediction-pipeline
   ```

2. **Install dependencies:**
   ```bash
   pip install pandas numpy scikit-learn
   ```

3. **Provide historical data:**
   Ensure your local repository folder contains a `data.csv` file with the following column headers: `Marketing_Spend`, `R&D_Spend`, `Administration_Costs`, `Number_of_Employees`, `Region`, and `Revenue`.

---

## 🚀 How to Run

Launch the entire pipeline directly from your terminal or command prompt:

```bash
python main.py
```

### **What happens next?**
1. **Model Automation**: The code loads your CSV, creates an 80/20 train-test split, fits the preprocessing transformer configurations, and trains a Linear Regression model.
2. **Metrics Summary**: Performance benchmarks print automatically onto your screen.
3. **Interactive Predictor**: The program enters a live loop prompting you to input coordinates to project predictive revenue data in real-time:

```text
=== Model Evaluation Metrics ===
MAE: 6648.39973
RMSE: 8363.05825
R2:   0.93301
================================

Enter company region (North America/Europe/Asia or exit to stop): North America
Marketing_Spend: 150000
R&D_Spend: 95000
Administration_Costs: 30000
Number_of_Employees: 120

Predicted Revenue: $185,420.50
```

---

## 🛠️ Pipeline Architecture

The end-to-end framework abstracts away complex feature splits by routing inputs cleanly through parallel transformers before running predictive calculations:

```text
Raw Tabular Row (Dict/DataFrame)
       │
       ├──► [Numerical Columns]  ──► StandardScaler() ──┐
       │                                                ├──► Linear Regression ──► Predicted Revenue
       └──► [Categorical Columns] ──► OneHotEncoder()  ──┘
```

---

## 🤝 Contributing
Feel free to fork this project, open issues, or submit pull requests. Future architectural upgrades could include scaling this template to support **Regularized Linear Models** (Ridge/Lasso) or deploying it as a microservice using a lightweight **FastAPI** application layer.
