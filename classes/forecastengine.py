from datetime import date, timedelta
import math


class ForecastEngine:
    def __init__(self, budget_manager, lookback_days=30):
        self.budget_manager = budget_manager
        self.lookback_days = lookback_days

    def average_daily_net(self):
        end_date = date.today()
        start_date = end_date - timedelta(days=self.lookback_days)

        recent_transactions = self.budget_manager.transactions_in_range(start_date, end_date)

        net_total = 0.0
        for t in recent_transactions:
            net_total += t.amount

        return net_total / self.lookback_days

    def forecast_balance(self, days=30):
        avg_net = self.average_daily_net()
        return self.budget_manager.current_balance() + (avg_net * days)

    def days_until_zero(self):
        avg_net = self.average_daily_net()

        if avg_net >= 0:
            return "N/A"

        current = self.budget_manager.current_balance()

        if current <= 0:
            return 0

        return math.ceil(current / (-avg_net))