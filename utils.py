# utils.py
def calculate_fine(overdue_days, rate_per_day=2):
    """Calculate fine for overdue items."""
    return overdue_days * rate_per_day
