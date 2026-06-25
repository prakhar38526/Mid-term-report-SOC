"""
-------------------------------------------------------------
SOC Week 3

Transaction Risk Analysis

Objective:
Mark each transaction as suspicious or non-suspicious
based on predefined compliance criteria.
-------------------------------------------------------------
"""

import pandas as pd

# ---------------------------------------------------
# Read Excel File
# ---------------------------------------------------

df = pd.read_excel("metallurgical_ledgers.xlsx")

# ---------------------------------------------------
# OFAC High-Risk Countries (Example List)
# ---------------------------------------------------

high_risk_countries = [
    "Iran",
    "North Korea",
    "Syria",
    "Russia",
    "Cuba"
]

# ---------------------------------------------------
# Criterion 1
# High Value Transaction
# ---------------------------------------------------

df["High_Value"] = df["Total_Value_USD"] > 500000

# ---------------------------------------------------
# Criterion 2
# High Risk Country
# ---------------------------------------------------

df["High_Risk_Country"] = df["Vendor_Country"].isin(high_risk_countries)

# ---------------------------------------------------
# Criterion 3
# Large Price Difference
# Compare Unit Price with Market Price
# ---------------------------------------------------

price_difference = abs(
    df["Unit_Price_USD"] - df["Market_Spot_Price"]
)

df["Price_Anomaly"] = (
    price_difference >
    (0.20 * df["Market_Spot_Price"])
)

# ---------------------------------------------------
# Criterion 4
# Cash Payments
# ---------------------------------------------------

df["Cash_Payment"] = (
    df["Payment_Method"]
    .str.lower()
    .eq("cash")
)

# ---------------------------------------------------
# Risk Score
# ---------------------------------------------------

criteria = [
    "High_Value",
    "High_Risk_Country",
    "Price_Anomaly",
    "Cash_Payment"
]

df["Risk_Score"] = df[criteria].sum(axis=1)

# ---------------------------------------------------
# Final Classification
# ---------------------------------------------------

def classify(score):
    if score >= 3:
        return "High Risk"
    elif score >= 1:
        return "Medium Risk"
    else:
        return "Low Risk"

df["Transaction_Status"] = df["Risk_Score"].apply(classify)

# ---------------------------------------------------
# Save Output
# ---------------------------------------------------

output_file = "analysed_transactions.xlsx"

df.to_excel(output_file, index=False)

print("=" * 60)
print("Transaction Analysis Complete")
print("=" * 60)

print(df.head())
print("\nRisk Level Summary:\n")
print(df["Transaction_Status"].value_counts())

print(f"\nOutput saved as: {output_file}")