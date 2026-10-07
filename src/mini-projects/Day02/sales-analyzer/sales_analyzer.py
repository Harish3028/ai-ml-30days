import numpy as np
from pathlib import Path

BASE = Path(__file__).parent

products = np.array(["Pen", "Notebook", "Backpack", "Lamp", "Mouse", "Headset"])
months = np.array(["Jan", "Feb", "Mar", "Apr", "May", "Jun"])

units = np.array([
    [320, 300, 350, 410, 380, 450],
    [150, 170, 160, 200, 210, 190],
    [ 40,  35,  60,  55,  70,  90],
    [ 25,  30,  20,  45,  40,  38],
    [ 60,  55,  80,  75,  95, 110],
    [ 12,  18,  15,  22,  30,  28],
])
prices = np.array([1.5, 4.0, 25.0, 18.0, 12.5, 40.0])

def product_totals(units):
    return (units.sum(axis=1))

def month_totals(units):
    return (units.sum(axis=0))

def best_product(units, products):
    totals = product_totals(units)
    i = totals.argmax()
    return products[i], totals[i]

def best_month(units, months):
    totals = month_totals(units)
    i = totals.argmax()
    return months[i], totals[i]

def revenue_matrix(units, prices):
    col = prices.reshape(-1, 1)
    return ((units * col))

def revenue_by_product(revenue):
    return revenue.sum(axis=1)

def revenue_by_month(revenue):
    return revenue.sum(axis=0)

def top_products_by_revenue(revenue, products, n=3):
    top_products = revenue_by_product(revenue)
    position = np.argsort(top_products)[::-1][:n]
    return products[position]

def revenue_share(revenue):
    rev_share = product_totals(revenue)
    return rev_share / rev_share.sum() * 100

def low_cell_count(units, limit=50):
    low = units < limit
    return int(low.sum())

def products_with_low_month(units, products, limit=50):
    low = units < limit
    return products[low.any(axis=1)]


def steady_sellers(units, products, floor=100):
    steady = units >= floor
    return products[steady.all(axis=1)]


def months_above_average(revenue, months):
    per_month = revenue.sum(axis=0)
    rev_month = per_month > per_month.mean()
    return months[rev_month]


def product_tiers(revenue):
    totals = revenue.sum(axis=1)
    return np.where(totals >= 6000, "Star",
            np.where(totals >= 4000, "Core", "Niche"))

def growth_percent(units):
    jan = units[:, 0]
    jun = units[:, -1]
    return (jun - jan) / jan * 100

def fastest_and_slowest(units, products):
    g = growth_percent(units)
    fast = g.argmax()
    slow = g.argmin()
    return products[fast], float(g[fast]), products[slow], float(g[slow])

def biggest_total_jump(units, months):
    totals = month_totals(units)
    jump = np.diff(totals)
    i = jump.argmax()
    return months[i + 1], int(jump[i])

def peak_months(units, months):
    return months[units.argmax(axis=1)]

def min_max_scale(units):
    mn = units.min(axis=1, keepdims=True)
    mx = units.max(axis=1, keepdims=True)
    return (units - mn) / (mx - mn)

def running_month_totals(units):
    return np.cumsum(month_totals(units))

def build_report(units, prices, products, months):
    revenue = revenue_matrix(units, prices)
    tiers = product_tiers(revenue)
 
    lines = []
    lines.append("=== SALES ANALYSIS ===")
    lines.append(f"Products: {len(products)} | Months: {len(months)}")
    lines.append(f"Total units: {units.sum()} | Total revenue: {revenue.sum():.2f}")
    lines.append("")
 
    lines.append("--- Per product ---")
    for p, u, r, t in zip(products, product_totals(units), revenue_by_product(revenue), tiers):
        lines.append(f"{p}: {u} units, revenue {r:.2f}, {t}")
    lines.append("")
 
    lines.append("--- Per month ---")
    for m, u, r in zip(months, month_totals(units), revenue_by_month(revenue)):
        lines.append(f"{m}: {u} units, revenue {r:.2f}")
    lines.append("")
 
    lines.append("--- Highlights ---")
    name, total = best_product(units, products)
    lines.append(f"Best product by units: {name} ({total})")
    name, total = best_month(units, months)
    lines.append(f"Best month by units: {name} ({total})")
    lines.append(f"Top 3 by revenue: {', '.join(top_products_by_revenue(revenue, products))}")
    f_name, f_pct, s_name, s_pct = fastest_and_slowest(units, products)
    lines.append(f"Fastest growing: {f_name} (+{f_pct:.1f} percent)")
    lines.append(f"Slowest growing: {s_name} (+{s_pct:.1f} percent)")
    name, jump = biggest_total_jump(units, months)
    lines.append(f"Biggest jump in total units: {name} (+{jump})")
    lines.append(f"Any month below 50: {', '.join(products_with_low_month(units, products))}")
    lines.append(f"Steady sellers (100+ every month): {', '.join(steady_sellers(units, products))}")
    lines.append(f"Peak months: {' '.join(peak_months(units, months))}")
    return lines                             # function level, NOT inside a loop
 
def save_report(lines, filename):
    with open(filename, "w") as file:
        file.write("\n".join(lines) + "\n")

if __name__ == "__main__":
    report = build_report(units, prices, products, months)
    print("\n".join(report))
    save_report(report, BASE / "report.txt")
    print(f"\nReport saved to {BASE / 'report.txt'}")



