from typing import Any


def filter_by_state(list_dict: list[dict[str, Any]], state: str = "EXECUTED") -> list[dict[str, Any]]:
    """
    возвращает новый список словарей, одержащий словари с ключем state == 'EXECUTED'
    """
    new_list = []
    for key in list_dict:
        if key.get("state") == state:
            new_list.append(key)
    return new_list


def sort_by_date(list_dict: list[dict[str, Any]], revers: bool = True) -> list[dict[str, Any]]:
    """сортировка словарей в списке по дате"""
    sorted_list_dict = sorted(list_dict, key=lambda x: x["date"], reverse=reversed)
    return sorted_list_dict
