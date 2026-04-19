# 🚗 Finance Data Warehouse For Ride Hailing Platform

## 📌 Overview

This project simulates a **Finance Data Warehouse** for a ride-hailing platform (similar to Bolt or Uber).
It demonstrates how raw operational data is transformed into **business-ready financial metrics** and exposed through a dashboard.

The project covers the full analytics engineering workflow:

* Data generation
* Data warehousing
* Data modeling (dbt)
* Pipeline orchestration (Airflow)
* Business intelligence (dashboard)

---

## 🧱 Architecture

**End-to-end data flow:**

```
Raw Data (Python)
        ↓
PostgreSQL (Docker)
        ↓
dbt (Staging → Marts)
        ↓
Analytics Tables
        ↓
Dashboard (Looker Studio)
```

---

## ⚙️ Tech Stack

* **Python** → data generation
* **PostgreSQL** → data warehouse
* **dbt (Data Build Tool)** → data transformation & modeling
* **Docker** → containerized infrastructure
* **Apache Airflow** → pipeline orchestration
* **Looker Studio** → dashboard & visualization

---

## 📊 Data Model

### 🔹 Raw Layer

* `rides` → trip-level data
* `payments` → transaction data

### 🔹 Staging Layer (dbt)

* `stg_rides`
* `stg_payments`

### 🔹 Mart Layer (dbt)

* `fact_rides` → joined operational dataset
* `fact_financials` → finance-ready metrics

---

## 💰 Key Metrics

* **Gross Booking Value (GBV)**
* **Platform Revenue** (20% take rate)
* **Driver Payout** (80%)
* **Take Rate** = Revenue / GBV

---

## ⚙️ Pipeline Orchestration (Airflow)

The pipeline is orchestrated using Apache Airflow:

* Generate synthetic data
* Run dbt transformations
* Build analytics tables

**DAG Flow:**

```
generate_data → run_dbt
```

## 🚀 How to Run

### 1. Start infrastructure

```bash
docker compose up -d
```

### 2. Generate data

```bash
python scripts/generate_data.py
```

### 3. Run dbt transformations

```bash
cd dbt_project/finance_dbt
dbt run
dbt test
```

### 4. Run Airflow (optional)

Open:

```
http://localhost:8080
```

---

## 🧠 Key Learnings

* Designed OLAP data models (fact tables)
* Built financial metrics from raw transactional data
* Implemented modular transformations using dbt
* Orchestrated pipelines with Airflow
* Delivered business insights through dashboards

---

## 📎 Future Improvements

* Add refund & adjustment logic
* Integrate real data sources (APIs)
* Deploy on cloud (AWS / GCP)
* Replace BashOperator with production-grade operators
* Add data quality monitoring & alerts

---
