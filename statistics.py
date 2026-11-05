def calculate_income(transactions):
    """обчислює загальний дохід"""
    return sum(t['amount'] for t in transactions if t["type"] == "income")


def calculate_expenses(transactions):
    """обчислює загальні витрати"""
    return sum(t['amount'] for t in transactions if t["type"] == "expense")


def calculate_balance(transactions):
    """обчислює поточний баланс"""
    income = calculate_income(transactions)
    expenses = calculate_expenses(transactions)
    return income - expenses