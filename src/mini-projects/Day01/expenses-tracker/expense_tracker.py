from expense import Expense
from pathlib import Path

BASE = Path(__file__).parent
VALID_CATEGORIES = ["Food", "Transport", "Rent", "Fun"]

def parse_line(line):
    parts = line.strip().split(",")
    date = parts[0].strip()

    if not date:
        raise ValueError("Date Cannot Be Empty!")

    if len(parts) != 3:
        raise ValueError("There Must Be Exactly Contain 3 Parts!")

    category = parts[1].strip()
    if category not in VALID_CATEGORIES:
        raise ValueError("Invalid Category!")

    try:
        amount = float(parts[2])
    except ValueError:
        raise ValueError(f"Amount must be a number: {parts[2].strip()}")

    if amount <= 0:
        raise ValueError("Invalid Amount!")

    return Expense(date, category, amount)

def load_expenses(filename):
    with open(filename) as f:
        expenses = []
        skipped = []
        for line in f:
            clean = line.strip()

            if not clean:
                continue

            try:
                expenses_obj = parse_line(line)
                expenses.append(expenses_obj)
            except ValueError as e:
                skipped.append((clean, str(e)))

    return expense, skipped

def total_spent(expenses):
    if not expenses:
        return 0.0

    total = [e.amount for e in expenses]
    return sum(total)

def average_expense(expenses):
    if not expense:
        return 0.0

    amount = [a.amount for a in expenses]
    return sum(amount) / len(amount)

def biggest_expense(expenses):
    if not expenses:
        return None

    return max(expenses, key=lambda e: e.amount)

def category_totals(expenses):
    cat_total = {"Food": 0.0, "Transport": 0.0, "Rent": 0.0, "Fun": 0.0}
    for e in expenses:
        cat_total[e.category] += e.amount

    return cat_total

def build_report(expenses, skipped):
    lines = []
    lines.append("=== EXPENSE REPORT ===")
    lines.append(f"Valid: {len(expenses)} | Skipped: {len(skipped)}")
    lines.append("")
    lines.append("--- Expenses ---")
    for e in expense:
        lines.append(str(e))
    lines.append("")
    lines.append(f"Total spent: {total_spent(expense):.2f}")
    lines.append(f"Average expense: {average_expense(expense):.2f}")
    lines.append(f"Biggest expense: {biggest_expense(expense)}")
    lines.append("")
    lines.append("--- By category ---")

    for category, total in category_totals(expenses).items():
        lines.append(f"{category}: {total:.2f}")

    lines.append("")
    lines.append("--- Skipped lines ---")
    for line, reason in skipped:
        lines.append(f"Skipped: {line}, Because: {reason}")

    return lines

def save_report(lines, filename):
    with open(filename, "w") as file:
        file.write("\n".join(lines) + "\n")

if __name__ == "__main__":
    expense, skipped = load_expenses(BASE / "expenses_raw.txt")
    report = build_report(expense, skipped)
    print("\n".join(report))

    expenses, skipped = load_expenses(BASE / "expenses_raw.txt")
    report = build_report(expenses, skipped)
    print("\n".join(report))
    save_report(report, BASE / "report.txt")
    print("\nReport saved to BASE / expenses_raw.txt")


                  
