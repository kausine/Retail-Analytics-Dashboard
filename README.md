# 🛒 Retail Analytics Dashboard  

## 📌 Project Overview  
This project demonstrates a complete **retail analytics pipeline** using **Python, SQL, and Power BI**. It covers everything from **ETL (Extract, Transform, Load)** to **exploratory data analysis, customer segmentation (RFM), and interactive dashboards**.  

The goal is to provide actionable insights into **sales trends, top-performing products, and customer behavior**, enabling data-driven decision-making for retail businesses.  

---

## ⚙️ Tech Stack  
- **Python** → ETL, data cleaning, RFM segmentation, cohort analysis  
- **Pandas, Matplotlib, Seaborn** → Exploratory Data Analysis (EDA) & visualization  
- **SQLite (SQL)** → Schema design, queries, and data storage  
- **Power BI** → Interactive dashboards (Revenue trends, Top Products, RFM Segments)  
- **Jupyter Notebooks** → Analysis and experimentation  

---

## 📂 Project Structure  
retail-project/
├─ data/                # Raw & processed data
│  ├─ retail_sales.csv
│  ├─ retail.db
│  ├─ rfm_segments.csv
├─ notebooks/           # Jupyter notebooks (ETL, EDA, Modeling)
│  ├─ 01_sql_queries_and_eda.ipynb
│  └─ 02_modeling_forecast_recs.ipynb
├─ scripts/             # Python scripts for automation
│  ├─ etl.py
│  └─ run_forecast.py
├─ dashboards/          # Power BI dashboards
│  ├─ dashboard.pbix      (Revenue Trends & Top Products)
│  └─ dashboard2.pbix     (RFM Segments)
├─ sql/                 # SQL schema & queries
│  ├─ schema.sql
│  └─ queries.sql
├─ README.md            # Project documentation
├─ requirements.txt     # Python dependencies
└─ .gitignore

---

## 📊 Dashboards  

### 1️⃣ Revenue Trends & Top Products  
- **Line chart** → Monthly revenue trends (seasonality, peaks & dips)  
- **Bar chart** → Top 10 products by revenue  

### 2️⃣ Customer Segmentation (RFM)  
- **Pie chart** → Customer distribution across segments (Champions, Potential, At Risk, etc.)  
- **Bar chart** → Revenue contribution by each segment  

📂 Files:  
- `dashboard.pbix` → Revenue & Product analysis  
- `dashboard2.pbix` → RFM Segmentation  

---

## 🔑 Key Features  
✔️ **ETL Pipeline** → Automated data cleaning and loading into SQLite  
✔️ **SQL Queries** → Revenue summaries, top products, customer counts  
✔️ **EDA** → Monthly sales trends, customer cohorts  
✔️ **RFM Segmentation** → Classified ~8,000 customers into segments for targeted marketing  
✔️ **Power BI Dashboards** → Interactive visualizations for decision-making  

---

## 🚀 How to Run Locally  

### 1. Clone the Repository  
```bash
git clone https://github.com/kausine/Retail-Analytics-Dashboard.git
cd Retail-Analytics-Dashboard
