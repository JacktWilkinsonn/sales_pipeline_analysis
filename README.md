# 📊 Sales Pipeline Analysis

## Overview

This project analyzes a B2B sales pipeline using Python, Pandas, and data visualization libraries to evaluate sales performance, pipeline health, revenue concentration, forecasting accuracy, and opportunity management.

The analysis recreates the functionality of an executive sales dashboard using a fully reproducible analytics workflow.

---

## Business Problem

Sales leaders need visibility into:

- Pipeline health
- Revenue forecasting
- Opportunity progression
- Sales representative performance
- Partner influence
- Customer acquisition trends

Without consistent reporting, it becomes difficult to identify stalled opportunities, forecast future revenue, and allocate resources effectively.

---

## Project Objectives

This analysis answers the following business questions:

### Pipeline Management

- Which stages contain the largest number of opportunities?
- Where do opportunities stall in the sales funnel?
- How old are current opportunities?

### Revenue Analysis

- Which deals contribute the most pipeline value?
- Is revenue concentrated among a small number of opportunities?

### Sales Performance

- Which sales representatives generate the most revenue?
- Which reps close the most opportunities?

### Partner Impact

- How much business is influenced by partners?
- Are partner-assisted opportunities more valuable?

### Customer Analysis

- What is the split between new and existing customers?
- Which segment contributes the most revenue?

### Forecasting

- How much revenue is expected by month?
- Are future bookings concentrated in specific periods?

---

# Dataset

The repository contains a simulated CRM dataset modeled after an enterprise sales pipeline dashboard.

## Raw Dataset

Location:

```text
data/raw/sales_pipeline_raw.csv
```

## Processed Dataset

Location:

```text
data/processed/sales_pipeline_clean.csv
```

---

## Dataset Fields

| Column | Description |
|----------|-------------|
| opportunity_id | Unique opportunity identifier |
| opportunity_name | Opportunity name |
| stage | Sales stage |
| deal_value | Opportunity value |
| sales_rep | Assigned sales representative |
| account_type | New or Existing account |
| partner_involved | Partner involvement indicator |
| product_category | Software or Electronics |
| competitor | Competitor involved |
| created_date | Opportunity creation date |
| last_interaction_date | Most recent activity |
| expected_close_date | Forecast close date |
| next_step_defined | Whether next step exists |

---

# Data Cleaning

The following cleaning steps were performed:

- Removed duplicate records
- Standardized date fields
- Converted dates to datetime format
- Created opportunity age metrics
- Calculated engagement metrics
- Generated revenue size buckets

---

# Feature Engineering

Additional fields were created:

## Pipeline Age

```python
pipeline_age_days
```

Measures the number of days since opportunity creation.

---

## Days Since Last Interaction

```python
days_since_last_interaction
```

Measures engagement recency.

---

## Opportunity Size Bucket

```python
size_bucket
```

Categories:

- 0–10K
- 10K–500K
- 500K–1M
- 1M–5M
- 5M–100M
- 100M+

---

## Forecast Month

```python
forecast_month
```

Used for revenue forecasting.

---

## Stale Opportunity Flag

```python
stale_opportunity
```

Flags opportunities with no recent activity.

---

# Technologies Used

## Programming

- Python 3

## Data Analysis

- Pandas
- NumPy

## Visualization

- Matplotlib
- Seaborn

## Development Environment

- Jupyter Notebook
- VS Code

---

# Repository Structure

```text
sales-pipeline-analysis/
│
├── data/
│   ├── raw/
│   │   └── sales_pipeline_raw.csv
│   │
│   └── processed/
│       └── sales_pipeline_clean.csv
│
├── notebooks/
│   └── sales_pipeline_analysis.ipynb
│
├── src/
│   ├── data_cleaning.py
│   ├── feature_engineering.py
│   ├── kpi_analysis.py
│   ├── forecasting.py
│   └── visualization.py
│
├── visualizations/
│   ├── pipeline_by_stage.png
│   ├── opportunity_size_distribution.png
│   ├── sales_rep_performance.png
│   ├── partner_involvement.png
│   ├── account_breakdown.png
│   ├── product_category_analysis.png
│   ├── revenue_forecast.png
│   └── next_step_status.png
│
├── reports/
│   └── final_report.pdf
│
├── requirements.txt
├── .gitignore
└── README.md
```

---

# Analysis Performed

## 1. Pipeline Stage Analysis

Evaluated:

- Opportunity count by stage
- Revenue by stage
- Funnel distribution

Visualization:

```text
pipeline_by_stage.png
```

---

## 2. Opportunity Size Analysis

Evaluated:

- Revenue concentration
- Deal size distribution
- Large opportunity dependence

Visualization:

```text
opportunity_size_distribution.png
```

---

## 3. Sales Representative Performance

Metrics:

- Total revenue
- Opportunity count
- Average deal size

Visualization:

```text
sales_rep_performance.png
```

---

## 4. Partner Impact Analysis

Metrics:

- Revenue influenced by partners
- Opportunity count
- Contribution percentage

Visualization:

```text
partner_involvement.png
```

---

## 5. Customer Analysis

Metrics:

- New vs Existing opportunities
- Revenue contribution by customer type

Visualization:

```text
account_breakdown.png
```

---

## 6. Product Category Analysis

Compared:

- Software
- Electronics

Metrics:

- Revenue
- Opportunity count

Visualization:

```text
product_category_analysis.png
```

---

## 7. Revenue Forecasting

Forecasted future revenue using expected close dates.

Visualization:

```text
revenue_forecast.png
```

---

# Key Insights

### Revenue Concentration

A significant portion of pipeline value is concentrated among a small number of large opportunities.

### Partner Influence

Partner-assisted opportunities account for a large share of total pipeline value.

### Pipeline Health

Several opportunities show signs of inactivity and require follow-up.

### Sales Performance

Performance varies substantially across representatives, highlighting opportunities for coaching and resource allocation.

---

# Future Enhancements

### Dashboard Development

- Streamlit Dashboard
- Plotly Interactive Visualizations

### Data Engineering

- SQL Database Integration
- Automated ETL Pipeline

### Machine Learning

- Win Probability Prediction
- Opportunity Risk Scoring
- Revenue Forecast Modeling

---

# Author
Jack Wilkinson
Built with Python, Pandas, and Data Visualization tools.
