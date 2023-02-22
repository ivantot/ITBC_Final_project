"""Utils module."""
from app.utils import currency_exchange_rate


def convert_money_by_currency(amount, input_currency, output_currency):
    """convert_money_by_currency function"""
    currency_combination = "_".join([input_currency, output_currency])
    return round(amount * currency_exchange_rate[currency_combination], 2)
