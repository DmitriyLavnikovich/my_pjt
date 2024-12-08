from src.masks import get_mask_card_number, get_mask_account

if __name__ == "__main__":
    print(get_mask_card_number(input("введите номер карты из 16-ти цифр: ")))
    print(get_mask_account(input("введите номер счета из 6-ти цифр: ")))