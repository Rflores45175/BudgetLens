class Transaction:
    def __init__(self, date, amount, category, description):

        self.date = date
        self.amount = amount
        self.category = category
        self.description = description

    def is_income(self):
        return self.amount > 0

    def is_expense(self):
        return self.amount < 0

    def __str__(self):
        sign = "+" if self.amount > 0 else ""
        return (
            f"{self.date}\t"
            f"{sign}${self.amount:.2f}\t"
            f"{self.category}\t"
            f"{self.description}"
        )