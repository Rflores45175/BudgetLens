from transaction import Transaction

class BudgetManager:

    def __init__(self, starting_balance):
        self.starting_balance = starting_balance
        self.transactions = []

    def add_transaction(self, transaction: Transaction):
        self.transactions.append(transaction)
        return True

    def current_balance(self):
        return self.starting_balance + self.total_income() - self.total_expenses()

    def total_income(self):
        income = 0
        for transaction in self.transactions:
            if transaction.is_income():
                income += transaction.amount

        return income

    def total_expenses(self):
        expenses = 0
        for transaction in self.transactions:
            if transaction.is_expense():
                expenses += transaction.amount

        return abs(expenses)

    def spending_by_category(self):
        category_totals = {}

        for transaction in self.transactions:
            if transaction.is_income():
                category = transaction.category
                amount = abs(transaction.amount)

                if category not in category_totals:
                    category_totals[category] = 0

                category_totals[category] += amount

        return category_totals

    def transactions_in_range(self, start_date, end_date):
        transactions_results = []

        for transaction in self.transactions:
            if start_date <= transaction.date <= end_date:
                transactions_results.append(transaction)

        return transactions_results
