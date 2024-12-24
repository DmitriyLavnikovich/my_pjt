import pytest

from src.widget import mask_account_card, get_date


def test_mask_account_card():
    assert mask_account_card('Visa Classic 6831982476737658') == 'Visa Classic 6831 98** **** 7658'

    assert mask_account_card('Счет 73654143567') == 'Счет **3567'


@pytest.mark.parametrize('original_date, result', [
    ('2024-03-11T02:26:18.671407', '11.03.2024'),
    ('2023-05-12T04:25:14.252234', '12.05.2023'),
    ('2020-01-09T03:32:15.786983', '09.01.2020')
])
def test_get_date(original_date, result):
    assert get_date(original_date) == result
