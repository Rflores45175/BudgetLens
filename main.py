from classes.transaction import Transaction
from classes.budgetmanager import BudgetManager
from classes.forecastengine import ForecastEngine
from datetime import date, timedelta


def main():
    manager = BudgetManager(starting_balance=500.00)

    today = date.today()

    # Sample transactions (mix of recent days)
    manager.add_transaction(Transaction(today - timedelta(days=2), 1500.00, "Income", "Paycheck"))
    manager.add_transaction(Transaction(today - timedelta(days=1), -120.45, "Groceries", "HEB"))
    manager.add_transaction(Transaction(today - timedelta(days=4), -45.20, "Gas", "Shell"))
    manager.add_transaction(Transaction(today - timedelta(days=10), -200.00, "Utilities", "Electric bill"))
    manager.add_transaction(Transaction(today - timedelta(days=15), -80.00, "Eating Out", "Dinner"))
    manager.add_transaction(Transaction(today - timedelta(days=20), -60.00, "Subscriptions", "Streaming"))
    manager.add_transaction(Transaction(today - timedelta(days=28), -300.00, "Rent", "Partial rent"))

    print("\n--- BudgetLens ---\n")
    print(f"Starting balance: ${manager.starting_balance:.2f}")
    print(f"Total income:     ${manager.total_income():.2f}")
    print(f"Total expenses:   ${manager.total_expenses():.2f}")
    print(f"Current balance:  ${manager.current_balance():.2f}")

    print("\nSpending by category:")
    cat_totals = manager.spending_by_category()
    for cat, total in sorted(cat_totals.items(), key=lambda x: x[1], reverse=True):
        print(f"  {cat:<15} ${total:.2f}")

    # Forecasting
    engine = ForecastEngine(manager, lookback_days=30)
    avg_net = engine.average_daily_net()
    print("\nForecasting (based on last 30 days):")
    print(f"Average daily net: ${avg_net:.2f} per day")
    print(f"Forecast balance in 30 days: ${engine.forecast_balance(30):.2f}")
    print(f"Forecast balance in 60 days: ${engine.forecast_balance(60):.2f}")
    print(f"Days until $0: {engine.days_until_zero()}")

    # Show last 7 days of transactions
    print("\nTransactions in the last 7 days:")
    start = today - timedelta(days=6)
    recent = manager.transactions_in_range(start, today)
    for t in recent:
        print(" ", t)


if __name__ == "__main__":
    main()