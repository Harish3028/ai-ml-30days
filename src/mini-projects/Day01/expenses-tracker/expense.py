class Expense:
    def __init__(self, date, category, amount):
        self.date = date
        self.category = category
        self.amount = amount

    def __str__(self):
        return f"Date: {self.date}, Category: {self.category}, Amount: {self.amount:.2f}"

if __name__ == "__main__":
        print(Expense("2026-10-01", "Food", 12.5))
        print(Expense("2026-10-02", "Rent", 450))
