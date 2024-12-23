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
    """ сортировка словарей в списке по дате """
    sorted_list_dict = sorted(list_dict, key=lambda x: x["date"], reverse=reversed)
    return sorted_list_dict


print(filter_by_state([{'id': 41428829, 'state': 'EXECUTED', 'date': '2019-07-03T18:35:29.512364'},
                       {'id': 939719570, 'state': 'EXECUTED', 'date': '2018-06-30T02:08:58.425572'},
                       {'id': 594226727, 'state': 'CANCELED', 'date': '2018-09-12T21:27:25.241689'},
                       {'id': 615064591, 'state': 'CANCELED', 'date': '2018-10-14T08:21:33.419441'}]))

print(sort_by_date([{'id': 41428829, 'state': 'EXECUTED', 'date': '2019-07-03T18:35:29.512364'},
                       {'id': 939719570, 'state': 'EXECUTED', 'date': '2018-06-30T02:08:58.425572'},
                       {'id': 594226727, 'state': 'CANCELED', 'date': '2018-09-12T21:27:25.241689'},
                       {'id': 615064591, 'state': 'CANCELED', 'date': '2018-10-14T08:21:33.419441'}]))
