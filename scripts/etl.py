import pandas as pd
import sqlite3
import os

SRC = "data/retail_sales.csv"
DB = "data/retail.db"

def load_csv(path):
    print("Loading:", path)
    df = pd.read_csv(path, parse_dates=["OrderDate"], infer_datetime_format=True)
    print("Loaded rows:", len(df))
    return df

def clean(df):
    print("Starting cleaning...")
    before = len(df)
    # drop exact duplicate rows
    df = df.drop_duplicates()
    # drop rows missing customer id
    df = df[df["CustomerID"].notna()]
    # ensure numeric types
    df["UnitPrice"] = pd.to_numeric(df["UnitPrice"], errors="coerce")
    df["Quantity"] = pd.to_numeric(df["Quantity"], errors="coerce")
    # drop rows with invalid unit price
    df = df[df["UnitPrice"].notna() & (df["UnitPrice"] > 0)]
    # fix Revenue if it looks wrong
    df["Revenue"] = pd.to_numeric(df["Revenue"], errors="coerce")
    df["Revenue"] = df["Revenue"].fillna(df["UnitPrice"] * df["Quantity"])
    # add derived columns
    df["OrderMonth"] = df["OrderDate"].dt.to_period("M").dt.to_timestamp()
    df["OrderDateOnly"] = df["OrderDate"].dt.date
    # remove absurd values
    df = df[(df["Quantity"].abs() <= 5000)]
    after = len(df)
    print(f"Cleaned: before={before} after={after} dropped={before-after}")
    return df

def save_to_sqlite(df, db_path):
    if os.path.exists(db_path):
        os.remove(db_path)  # overwrite for fresh run
    conn = sqlite3.connect(db_path)
    df.to_sql("transactions", conn, index=False)
    conn.close()
    print("Saved cleaned data to", db_path)

def basic_checks(df):
    print("--- Basic checks ---")
    print("rows:", len(df))
    print("unique_invoices:", df["InvoiceNo"].nunique())
    print("unique_customers:", df["CustomerID"].nunique())
    print("total_revenue:", round(df["Revenue"].sum(), 2))
    print("total_returns (qty<0):", (df["Quantity"] < 0).sum())

def main():
    df = load_csv(SRC)
    df = clean(df)
    basic_checks(df)
    save_to_sqlite(df, DB)

if __name__ == "__main__":
    main()
