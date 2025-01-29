import json
import requests


def get_json_transaction(filename):
    """"Функция принимает на вход json-файл и возвращает список словарей"""
    try:
        transactions = json.load(open(filename, encoding = 'utf-8'))
    except FileNotFoundError:
        return []
    else:
        return transactions

if __name__ == "__main__":
    open_file = get_json_transaction('data/operations.json')
    print(open_file)


def sum_transactions():