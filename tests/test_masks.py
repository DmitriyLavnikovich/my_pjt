import pytest

from src.masks import get_mask_card_number, get_mask_account


def test_get_mask_card_number():
    assert get_mask_card_number("4657382947583956") == "4657 38** **** 3956"


def test_get_mask_account():
    assert get_mask_account("789874") == "**9874"
