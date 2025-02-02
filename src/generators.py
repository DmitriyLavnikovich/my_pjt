from tabnanny import check
from typing import Iterator


def filter_by_currency(transactions_list: list[dict], currency: str = "USD") -> Iterator:
    """ " функция, принимающая на вход список словарей и возвращающая итератор,
    выдающий транзакции с валютой USD"""

    for transaction in transactions_list:
        if (transaction["operationAmount"]["currency"]["code"]) == currency:
            yield transaction


def transaction_descriptions(transactions: list[dict]) -> Iterator:
    """ " генератор, возвращающий описание транзакции"""
    for transaction in transactions:
        yield transaction.get("description", "")


def card_number_generator(start, stop):
    """генератор 16-ти значного номера карты в заданном диапазоне"""
    for number in range(start, stop):
        yield f"{str(number).zfill(16)[:4]} {str(number).zfill(16)[4:8]} {str(number).zfill(16)[8:12]} {str(number).zfill(16)[12:16]}"
