import pandas as pd
from pathlib import Path

BASE = Path(__file__).parent

CATEGORIES = pd.DataFrame({
    "product": ["Laptop", "Monitor", "Keyboard", "Mouse", "Headset", "Webcam"],
    "category": ["Computer", "Computer", "Accessory", "Accessory", "Accessory", "Accessory"],
})

MAX_QUANTITY = 100

def load_orders(path):
    return pd.read_csv(path)

def problem_counts(df):
    rows = len(df)
    missing = int(df.isna().sum().sum())
    duplicates = int(df.duplicated().sum())
    return {"rows": rows, "missing": missing, "duplicates": duplicates}

def clean_text(df):
    out = df.copy()
    for col in ["city", "customer", "product"]:
        out[col] = out[col].str.strip().str.title()
    return out

def convert_types(df):
    out = df.copy()
    out["quantity"] = pd.to_numeric(out["quantity"], errors="coerce")
    out["price"] = pd.to_numeric(out["price"], errors="coerce")
    out["order_date"] = pd.to_datetime(out["order_date"], errors="coerce")
    return out

def drop_duplicate_orders(df):
    return df.drop_duplicates()

def drop_missing(df):
    return df.dropna(subset=["quantity","price","order_date"])

def drop_bad_quantity(df):
    return df[df["quantity"] > 0]

def add_revenue(df):
    out = df.copy()
    out["revenue"] = out["quantity"] * out["price"]
    return out

def remove_outliers(df, max_quantity=MAX_QUANTITY):
    return df[df["quantity"] <= max_quantity]

def revenue_by_city(df):
    return (df.groupby("city").agg(orders=("order_id", "count"), 
                                   revenue=("revenue", "sum"))
                                   .sort_values("revenue", ascending=False).reset_index())


def revenue_by_product(df):
    return (df.groupby("product").agg(orders=("order_id", "count"), 
                                      units=("quantity", "sum"), revenue=("revenue", "sum"))
                                      .sort_values("revenue",ascending=False).reset_index())

def add_category(df, categories):
    new = df.merge(categories, on="product", how="left")
    return new

def revenue_by_category(df):
    return (df.groupby("category")["revenue"].sum()
            .sort_values(ascending=False).reset_index())

def clean_orders(raw):
    log = [("loaded", len(raw))]
    df = raw
    steps = [
        ("clean text", clean_text),
        ("convert types", convert_types),
        ("drop duplicates", drop_duplicate_orders),
        ("drop missing", drop_missing),
        ("drop quantity <= 0", drop_bad_quantity),
        ("add revenue", add_revenue),
        ("drop outliers", remove_outliers),
    ]
    for name, func in steps:
        df = func(df)
        log.append((name, len(df)))
    return df.reset_index(drop=True), log


def build_report(clean, log, by_city, by_product, by_category):
    lines = ["=== ORDERS CLEANING REPORT ==="]
    lines.append("")
    lines.append("--- Cleaning log ---")
    prev = None
    for name, n in log:
        if prev is None:
            lines.append(f"{name}: {n} rows")
        else:
            lines.append(f"{name}: {n} rows (removed {prev - n})")
        prev = n
    lines.append("")
    lines.append(f"Clean orders: {len(clean)} | Unique customers: {clean['customer'].nunique()}")
    lines.append(f"Total revenue: {clean['revenue'].sum():.2f}")
    lines.append(f"Date range: {clean['order_date'].min().date()} to {clean['order_date'].max().date()}")
    lines.append("")
    lines.append("--- Revenue by city ---")
    for city, n, rev in zip(by_city["city"], by_city["orders"], by_city["revenue"]):
        lines.append(f"{city}: {rev:.2f} (orders: {n})")
    lines.append("")
    lines.append("--- Revenue by product ---")
    for p, u, rev in zip(by_product["product"], by_product["units"], by_product["revenue"]):
        lines.append(f"{p}: {rev:.2f} (units: {u:.0f})")
    lines.append("")
    lines.append("--- Revenue by category ---")
    for c, rev in zip(by_category["category"], by_category["revenue"]):
        lines.append(f"{c}: {rev:.2f}")
    return lines


def save_report(lines, path):
    with open(path, "w") as f:
        f.write("\n".join(lines) + "\n")

if __name__ == "__main__":
    raw = load_orders(BASE / "orders_raw.csv")
    clean, log = clean_orders(raw)
    by_city = revenue_by_city(clean)
    by_product = revenue_by_product(clean)
    with_cat = add_category(clean, CATEGORIES)
    by_category = revenue_by_category(with_cat)

    lines = build_report(clean, log, by_city, by_product, by_category)
    print("\n".join(lines))

    save_report(lines, BASE / "report.txt")
    clean.to_csv(BASE / "orders_clean.csv", index=False)
    print("Saved report.txt and orders_clean.csv")