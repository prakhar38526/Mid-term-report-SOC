# Mid-term-report-SOC

# Corporate Compliance & Risk Analytics (SOC Project)

## Overview

This repository contains my work completed during the first four weeks of the Summer of Code (SOC) project on **Corporate Compliance & Risk Analytics**.

The overall objective of this project is to understand how data analytics and machine learning can be used in corporate compliance systems to identify suspicious financial activities, procurement fraud, and operational risks in the global metallurgical supply chain.

Instead of directly using machine learning libraries, the project focuses on understanding the mathematics, compliance concepts, data collection process, and logic behind risk detection systems.

Throughout these weeks, I learnt about financial APIs, international trade databases, fraud detection concepts, transaction risk analysis, and the mathematical foundation of linear regression.

---

# Project Objectives

The project aims to build a compliance analytics pipeline that can:

- Collect financial and trade data from different sources.
- Understand international trade behaviour.
- Detect suspicious transactions using logical rules.
- Learn the mathematics behind regression models.
- Build the foundation for anomaly detection in future weeks.

---

# Repository Structure

```
.
├── README.md
├── requirements.txt

Week 1
├── yahoo_finance_api.py
├── un_comtrade_api.py
├── yahoo_finance_data.csv

Week 2
├── world_bank_api.py
├── world_bank_data.csv

Week 3
├── suspicious_transaction_analysis.py
├── analysed_transactions.xlsx

Week 4
├── least_squares_regression.py
├── regression_predictions.csv
```

---

# Week 1

## Topic

Understanding APIs and collecting financial/trade data.

### Concepts Studied

### What is an API?

API stands for **Application Programming Interface**.

An API allows two software applications to communicate with each other.

Instead of manually opening websites and copying information, Python programs can automatically request data from servers.

Most APIs return data in **JSON (JavaScript Object Notation)** format.

Example:

```json
{
  "country": "India",
  "tradeValue": 500000
}
```

JSON stores information in key-value pairs which can easily be converted into Python dictionaries or pandas DataFrames.

---

## Yahoo Finance API

Yahoo Finance provides financial market data including:

- Stock prices
- Commodity prices
- Currency exchange rates
- Cryptocurrency data
- Historical market prices
- Company financial information

Although Yahoo discontinued its official API in 2017, libraries such as **yfinance** and **yahoo_fin** still allow easy access to the available data.

### Why is it useful?

For this project, commodity prices act as a benchmark.

Example:

If the international market price of copper is around **$9000 per ton**, but procurement records show purchases at **$15000 per ton**, it could indicate:

- Over-invoicing
- Procurement fraud
- Suspicious transactions

Yahoo Finance data helps establish the expected market price.

---

### Data Downloaded

Using the **yfinance** library, I downloaded historical Copper Futures prices and saved the data into a CSV file.

Output file:

```
yahoo_finance_data.csv
```

---

## UN Comtrade API

UN Comtrade is one of the world's largest international trade databases.

It contains import-export information reported by countries around the world.

Some important fields include:

- Import/Export
- Trade Value
- Quantity
- Commodity Code (HS Code)
- Reporter Country
- Partner Country

### Why is it important?

Trade data is one of the most important sources for detecting Trade-Based Money Laundering (TBML).

Large differences between market prices and declared trade values may indicate:

- Over-invoicing
- Under-invoicing
- False invoicing
- Procurement fraud

I also explored how UN Comtrade data can later be combined with Yahoo Finance data for compliance analysis.

---

## AML Concepts

I also studied the basics of Anti-Money Laundering (AML).

Money laundering generally consists of three stages:

1. Placement
2. Layering
3. Integration

In international trade, commodities such as metals can also be used for laundering money through manipulated invoices.

---

## Files

- yahoo_finance_api.py
- un_comtrade_api.py

---

# Week 2

## Topic

Economic Indicators, Fraud Detection Concepts and World Bank API.

---

## World Bank API

The World Bank API provides publicly available economic indicators for countries across the world.

Examples include:

- GDP
- Inflation
- Population
- Unemployment
- Trade statistics

These indicators help provide economic context while analysing financial transactions.

For this week, I wrote a Python program to download India's GDP data from the World Bank API.

The downloaded data was stored in:

```
world_bank_data.csv
```

---

## Shipment Delay

I studied the concept of shipment delay.

In international trade, there is usually a time gap between:

- Finalising a deal
- Shipment of goods

Very unusual shipment delays can sometimes indicate:

- Fake transactions
- Documentation fraud
- Compliance issues
- Supply chain risks

---

## Smurfing

Smurfing is an Anti-Money Laundering technique.

Instead of transferring one large amount, criminals divide money into many smaller transactions to avoid regulatory reporting limits.

Example:

Instead of transferring ₹1 Crore once,

they transfer

₹5 lakh

20 different times.

Each transaction appears normal individually but together they represent suspicious behaviour.

---

## Benford's Law

Benford's Law states that in naturally occurring datasets, smaller leading digits appear more frequently than larger digits.

Expected distribution:

| Digit | Approx. Frequency |
|-------|------------------|
|1|30%|
|2|17%|
|3|12%|
|...|...|
|9|5%|

Large deviations from this distribution may indicate manipulated financial records.

Benford's Law is widely used in:

- Fraud Detection
- Accounting Audits
- Compliance Analytics

---

## Files

- world_bank_api.py

---

# Week 3

## Topic

Transaction Risk Analysis

---

## OFAC Sanctions

I studied OFAC (Office of Foreign Assets Control) sanctions.

OFAC maintains lists of individuals, companies and countries with whom financial transactions are restricted.

Businesses screen transactions against these sanction lists to ensure regulatory compliance.

---

## Suspicious Transaction Detection

Using logical rules, I developed a simple risk scoring system.

Different criteria were created to identify potentially suspicious transactions.

Examples include:

- Large transaction amount
- High-risk country
- Suspicious vendor behaviour
- Unusual transaction frequency

Each criterion was stored as a separate column.

A risk score was calculated by combining these conditions.

Transactions were finally classified into:

- Low Risk
- Medium Risk
- High Risk

The analysed dataset was exported to:

```
analysed_transactions.xlsx
```

---

## Files

- suspicious_transaction_analysis.py

---

# Week 4

## Topic

Least Squares Regression

---

Instead of directly using machine learning libraries like Scikit-Learn, I learnt the mathematical foundation of linear regression.

The objective was to understand how the best fitting line is calculated.

The regression model follows the equation:

```
y = mx + c
```

where

- m = slope
- c = intercept

The Least Squares Method finds the values of m and c that minimise the total squared error between actual and predicted values.

I implemented this algorithm manually in Python.

The program calculates:

- Slope
- Intercept
- Predictions

The predicted values were saved as:

```
regression_predictions.csv
```

---

## Files

- least_squares_regression.py

---

# Libraries Used

- Python
- Pandas
- NumPy
- Requests
- yfinance

---

# Key Learnings

During these four weeks, I learnt:

- How APIs work
- Working with JSON data
- Downloading financial datasets using APIs
- International trade datasets
- Basics of Anti-Money Laundering (AML)
- Trade-Based Money Laundering (TBML)
- OFAC sanctions
- Smurfing
- Benford's Law
- Transaction risk scoring
- Basic compliance analytics
- Least Squares Regression
- Data preprocessing using pandas

---

# Future Work

The concepts learnt in these weeks will be used in the upcoming phases of the project where the focus will shift towards:

- Building regression models from scratch
- Vendor behaviour profiling
- Anomaly detection
- Mahalanobis Distance
- Risk scoring models
- Machine Learning for compliance analytics

---

## Mentor

**Amit Jaiswal**

Summer of Code (SOC)

Corporate Compliance & Risk Analytics
