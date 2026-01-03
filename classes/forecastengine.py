from datetime import date, timedelta

class ForecastEngine:
    def __init__(self, budget_manager, lookback_days=30):
        self.budget_manager = budget_manager
        self.lookback_days = lookback_days

    def average_daily_net(self):
        pass

    def forecast_balance(self):
        pass

    def days_until_zero(self):
        pass

