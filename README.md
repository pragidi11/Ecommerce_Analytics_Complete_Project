# E-Commerce Sales ELT Pipeline with dbt + PostgreSQL + Power BI

A complete end-to-end data engineering portfolio project that demonstrates how raw e-commerce data can be ingested, validated, transformed into a dimensional warehouse, and exposed as analytics-ready marts for Power BI.

## Project Overview

An e-commerce company receives transactional data from multiple operational files:

- Customers
- Products
- Orders
- Order Items
- Payments

The raw data is loaded into PostgreSQL, transformed using dbt, tested for quality, and modeled into a star schema optimized for analytics.

The final marts are designed for Power BI reporting.

## Architecture

```text
CSV / JSON Source Files
        |
        v
Python Ingestion + Validation
        |
        v
PostgreSQL Raw Schema
        |
        v
dbt Staging Models
        |
        v
dbt Intermediate Models
        |
        v
Dimensional Warehouse
        |
        +----------------------------+
        |                            |
        v                            v
Dimension Tables                Fact Tables
dim_customer                    fact_orders
dim_product                     fact_order_items
dim_date                        fact_payments
dim_geography
        |
        v
Analytics Marts
        |
        +-----------------------------+
        |             |               |
        v             v               v
Sales Summary   Customer Analysis   Product Performance
        |
        v
Power BI
```

## Tech Stack

- Python
- PostgreSQL
- SQL
- dbt Core
- Pandas
- Docker
- Pytest
- GitHub Actions
- Power BI

## Repository Structure

```text
ecommerce-sales-elt-pipeline/
├── data/
│   ├── raw/
│   └── processed/
├── dbt/
│   └── ecommerce_warehouse/
│       ├── models/
│       │   ├── staging/
│       │   ├── intermediate/
│       │   └── marts/
│       ├── dbt_project.yml
│       └── profiles.yml
├── docs/
│   ├── architecture.md
│   ├── data_dictionary.md
│   ├── interview_guide.md
│   └── powerbi_dashboard_guide.md
├── scripts/
│   ├── generate_data.py
│   ├── run_local_pipeline.py
│   └── export_powerbi_marts.py
├── sql/
│   ├── 001_create_schemas.sql
│   └── analytics_queries.sql
├── src/
│   ├── config.py
│   ├── database.py
│   ├── ingest.py
│   ├── quality.py
│   └── transformations.py
├── tests/
│   ├── test_quality.py
│   └── test_transformations.py
├── .github/workflows/ci.yml
├── docker-compose.yml
├── requirements.txt
└── README.md
```

## Business Questions

The project supports questions such as:

- What is total revenue?
- What is average order value?
- Which products generate the most revenue?
- Which categories sell the most units?
- Which states generate the most sales?
- How many customers are repeat buyers?
- Which customers have the highest lifetime value?
- What are monthly revenue trends?
- Which payment methods are used most?
- What is the order cancellation rate?

## Data Model

### Dimensions

- `dim_customer`
- `dim_product`
- `dim_date`
- `dim_geography`

### Facts

- `fact_orders`
- `fact_order_items`
- `fact_payments`

### Analytics Marts

- `mart_sales_summary`
- `mart_customer_analysis`
- `mart_product_performance`
- `mart_monthly_revenue`

## Quick Start

### 1. Create Python environment

```bash
python -m venv .venv
```

Windows:

```bash
.venv\Scripts\activate
```

macOS/Linux:

```bash
source .venv/bin/activate
```

### 2. Install dependencies

```bash
pip install -r requirements.txt
```

### 3. Run the local pipeline

```bash
python scripts/run_local_pipeline.py
```

This creates a complete local demo and writes Power BI-ready CSV outputs to:

```text
data/processed/
```

## PostgreSQL Setup

```bash
docker compose up -d postgres
python scripts/generate_data.py
python -m src.ingest
```

## dbt Setup

```bash
cd dbt/ecommerce_warehouse
dbt debug --profiles-dir .
dbt run --profiles-dir .
dbt test --profiles-dir .
```

## Power BI

Import the CSV marts from:

```text
data/processed/
```

Recommended files:

- `mart_sales_summary.csv`
- `mart_customer_analysis.csv`
- `mart_product_performance.csv`
- `mart_monthly_revenue.csv`

See:

`docs/powerbi_dashboard_guide.md`

## Data Quality Checks

The project validates:

- unique customer IDs
- unique product IDs
- unique order IDs
- non-null primary keys
- valid order status values
- positive quantities
- non-negative prices
- valid payment amounts
- valid timestamps
- referential integrity
- duplicate records

## Sample Resume Bullets

**E-Commerce Sales ELT Pipeline | Python, PostgreSQL, dbt, Power BI**

- Built an end-to-end ELT pipeline for 50,000+ e-commerce order-item records using Python, PostgreSQL, and dbt, transforming raw customer, product, order, and payment data into analytics-ready dimensional models.
- Designed a star-schema warehouse with customer, product, geography, and date dimensions plus order, order-item, and payment fact tables to support scalable BI reporting.
- Developed dbt staging, intermediate, and mart layers with automated data-quality tests for uniqueness, null values, referential integrity, and business-rule validation.
- Created Power BI-ready analytics marts for revenue trends, customer lifetime value, repeat purchases, product performance, and geographic sales analysis.

## Interview Summary

> I built an end-to-end e-commerce ELT pipeline using Python, PostgreSQL, dbt, and Power BI. I created realistic source data for customers, products, orders, order items, and payments. Python handles ingestion and validation, PostgreSQL stores the raw layer, and dbt transforms the data through staging and intermediate models into a star schema. I also built analytics marts for sales, customer value, product performance, and monthly revenue. The final outputs are designed to connect directly to Power BI.

## Future Enhancements

- Apache Airflow orchestration
- Kafka event ingestion
- S3 raw data lake
- Snowflake or Redshift
- Spark transformations
- dbt snapshots for SCD Type 2
- Terraform
- Great Expectations
- DataHub or OpenMetadata
- CI/CD deployment
