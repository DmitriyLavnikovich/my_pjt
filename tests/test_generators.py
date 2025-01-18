import pytest

from src.generators import filter_by_currency, card_number_generator, transaction_descriptions


@pytest.mark.parametrize(
    "transactions",
    [
        [
            {
                "id": 939719570,
                "state": "EXECUTED",
                "date": "2018-06-30T02:08:58.425572",
                "operationAmount": {"amount": "9824.07", "currency": {"name": "USD", "code": "USD"}},
                "description": "Перевод организации",
                "from": "Счет 75106830613657916952",
                "to": "Счет 11776614605963066702",
            }
        ]
    ],
)
def test_filter_by_currency(transactions):
    generator = filter_by_currency(transactions, "USD")
    assert next(generator) == [{
        "id": 939719570,
        "state": "EXECUTED",
        "date": "2018-06-30T02:08:58.425572",
        "operationAmount": {"amount": "9824.07", "currency": {"name": "USD", "code": "USD"}},
        "description": "Перевод организации",
        "from": "Счет 75106830613657916952",
        "to": "Счет 11776614605963066702",
    }]


@pytest.mark.parametrize(
    "transactions",
    [
        (
            [
                {
                    "id": 939719570,
                    "state": "EXECUTED",
                    "date": "2018-06-30T02:08:58.425572",
                    "operationAmount": {"amount": "9824.07", "currency": {"name": "USD", "code": "USD"}},
                    "description": "Перевод организации",
                    "from": "Счет 75106830613657916952",
                    "to": "Счет 11776614605963066702",
                }
            ]
        )
    ],
)
def test_transaction_descriptions(transactions):
    generator = transaction_descriptions(transactions)
    assert next(generator) == "Перевод организации"


@pytest.mark.parametrize(
    "start, stop, expected",
    [
        (1234123412341230, 1234123412341231, "1234 1234 1234 1230"),
        (1234123412341231, 1234123412341232, "1234 1234 1234 1231"),
        (1234123412341232, 1234123412341233, "1234 1234 1234 1232"),
    ],
)
def test_card_number_generator(start, stop, expected):
    generator = card_number_generator(start, stop)
    assert next(generator) == expected
