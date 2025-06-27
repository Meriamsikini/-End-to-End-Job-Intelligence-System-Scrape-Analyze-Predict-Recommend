# Job Market Intelligence System

This project is designed to help students and job seekers navigate the complex job market by leveraging scraped data from various job platforms, storing it in a structured Oracle database, and delivering visual analytics and predictive insights using machine learning.

## 👉 Problem Statement

With the continuous emergence of new professions and specialties, identifying the right job becomes a challenge for fresh graduates and individuals entering the workforce. Navigating thousands of offers and understanding market demands is overwhelming.

## 🛠️ Solution Overview

Our system addresses this challenge by:

* **Scraping** job data from four national and international websites.
* **Cleaning** and storing job data in an **Oracle Database**.
* **Visualizing** top jobs and skills per domain using PyQt5 and matplotlib.
* **Predicting** future in-demand jobs and skills using **Scikit-learn** and **XGBoost**.
* **Recommending** relevant jobs based on uploaded resumes (CVs) using **PDF parsing** (pdfminer).

## 📊 Key Features

### ✅ Data Collection

* Source platforms: emploi.ma, jobboom, marocannonces, remoteok
* Stored as CSV in the `SCRAPING/` folder
* Unified and preprocessed before database insertion

### ✉️ Database Management

* Oracle DB schema in `database/jobs_database.sql`
* Connection and insertion logic in `database/csv_connection.py` and `db_connection.py`

### 📊 Visualizations

* Dashboards built using **PyQt5**
* Files: `dashboard_page.py`, `competence_dashboard.py`

### 🤖 Prediction Engine

* `prediction_page.py`, `competence_prediction.py`
* ML pipeline: `StandardScaler()` + `XGBRegressor()`
* Forecasts job/skill trends (next 6 months)

### 💼 CV Recommendation

* Users upload PDF resumes
* System extracts skills and matches with job offers
* Logic in `job_matcher.py` and `recommandation_page.py`

## 📂 Project Directory Structure

```
project_root/
|
├── database/
│   ├── jobs_database.sql         # SQL schema
│   └── csv_connection.py         # Load CSVs to Oracle DB
│
├── SCRAPING/
│   ├── jobboom.py
│   ├── emplois_ma.py
│   └── ...
│
├── competence_dashboard.py       # Visualize skill data
├── competence_prediction.py      # Predict skills
├── dashboard_page.py             # Visualize job offers
├── data_loader.py                # Load data for visual/ML
├── db_connection.py              # Oracle DB helper
├── job_matcher.py                # Match CVs with jobs
├── prediction_page.py            # Predict jobs
├── recommandation_page.py        # Recommendation logic
├── main.py                       # Main PyQt5 interface
└── README.md
```

## 🔧 Technologies Used

* **Python** (PyQt5, Pandas, Numpy)
* **Oracle Database** (SQL)
* **Machine Learning**: Scikit-learn, XGBoost
* **Visualization**: Matplotlib, PyQt5
* **Web Scraping**: BeautifulSoup,Requests, Selenium
* **PDF Parsing**: pdfminer.high\_level

## 💡 How It Works

💡 How It Works

1-Data Ingestion: Run all scraping scripts manually to collect job offers.

2-Database Sync: Insert CSVs into Oracle using CSV_TO_DATABASE.py.

3-run "main.py" to Launch PyQt5 interface

## 🚀 Quick Start

```bash
# Install Python dependencies
pip install -r requirements.txt

# Run the main interface
python main.py
```

## 👤 Author

Meriam SIKINI

---

For any queries or issues, feel free to open an issue or contact the maintainer.
