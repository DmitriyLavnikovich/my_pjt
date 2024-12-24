from calendar import month

from src.masks import get_mask_card_number, get_mask_account

def mask_account_card(user_input: str) -> str:
    """ возврат маски информации о счетах и картах """
    dividing_line = user_input.split( )
    name = " ".join(dividing_line[:-1])
    number = dividing_line[-1]
    if name == "Счет":
        mask_numbers = get_mask_account(number)
        return f"{name} {mask_numbers}"
    else:
        mask_numbers = get_mask_card_number(number)
        return f"{name} {mask_numbers}"


def get_date(date: str) -> str:
    """возврат корректный формат даты"""
    correct_date = date.split("T")[0]
    year, month, day = correct_date.split("-")
    return f"{day}.{month}.{year}"

