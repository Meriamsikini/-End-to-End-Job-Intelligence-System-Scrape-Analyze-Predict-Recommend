# Job Market Intelligence System

This data-driven project aims to assist students and job seekers by analyzing job trends in the IT and Finance sectors, using data scraped from national and international job boards.

## 📌 Problem Statement

The number of job titles and specialties in the labor market increases every day. Fresh graduates and students seeking internships or employment often face difficulty identifying the right jobs that align with their education and skills.

## ✅ Proposed Solution

Our recommendation system tackles this issue by:
- **Scraping** real-time job data from 4 platforms (emploi.ma, jobboom, marocannonces, remoteok).
- **Cleaning and storing** the data in an **Oracle Database**.
- **Visualizing** top jobs and in-demand skills using **PyQt5** dashboards.
- **Predicting** future job and skill trends using **XGBoost** and **Scikit-learn**.
- **Recommending** job roles based on users' resumes using PDF parsing (`pdfminer.high_level`).

## ⚙️ Technologies

- 🐍 Python
- 📊 Pandas, Matplotlib, Seaborn
- 💻 Oracle Database (SQL)
- 🤖 XGBoost, Scikit-learn (ML)
- 🕸️ Selenium, BeautifulSoup (Web scraping)
- 🖼️ PyQt5 , Matplotlib (Visualization)
- 📄 pdfminer (CV parsing)

## 📈 Features

### 🔎 Data Scraping
- Extract job offers from 4 job websites.
- Clean region, date, and skill fields.
- Normalize and store in Oracle DB.

### 📊 Data Visualization
- Top 5 jobs and skills by domain (IT / Finance).
- Interactive dashboards built with PyQt5.

### 🔮 Prediction Engine
- Forecast top 3 specialties and 5 skills for the next 6 months.
- Uses pipelines with `StandardScaler` and `XGBRegressor`.

### 🎯 Resume Matching
- Upload a PDF resume.
- Automatically extract keywords and match them with predicted job offers.
