# Finance Data Warehouse (Bolt-like Simulation)

## 📌 Overview

This project simulates a Finance Data Warehouse for a ride-hailing platform (similar to Bolt/Uber).
It demonstrates how raw operational data is transformed into business-ready financial metrics and dashboards.

---

## 🧱 Architecture

**Data Flow:**

Raw Data (CSV) → PostgreSQL (Docker) → dbt Models → Analytics Tables → Dashboard

---

## ⚙️ Tech Stack

* Python (data generation)
* PostgreSQL (data warehouse)
* dbt (transformations & modeling)
* Docker (infrastructure)
* Looker Studio (dashboard)

---

## 📊 Data Model

### Raw Layer

* rides
* payments

### Staging Layer (dbt)

* stg_rides
* stg_payments

### Mart Layer (dbt)

* fact_rides
* fact_financials

---

## 💰 Key Metrics

* Gross Booking Value (GBV)
* Platform Revenue
* Driver Payout
* Take Rate

---

## 📈 Dashboard

Includes:

* Revenue trends over time
* Revenue by city
* KPI summary (Revenue, GBV, Payouts)
* Take rate analysis

---

## 🚀 How to Run

### 1. Start database

docker compose up -d

### 2. Generate data

python scripts/generate_data.py

### 3. Load data into Postgres

### 4. Run dbt

cd dbt_project/finance_dbt
dbt run
dbt test

---

## 📌 Key Learnings

* Designed OLAP data models (fact tables)
* Built finance metrics from raw transactions
* Implemented dbt transformation pipelines
* Created business-facing dashboard

---

## 📎 Future Improvements

* Add refund & currency conversion logic
* Orchestrate pipelines using Airflow
* Deploy on cloud (AWS/GCP)

---
