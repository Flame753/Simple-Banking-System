import random


class Bank:
    BIN = 400000
    checksum = 5
    accounts = {}

    def __init__(self):
        self.account_identifier = Bank.add_zeros(random.randint(0, int('9' * 9)), 9)
        self.card_number = int(str(Bank.BIN) + self.account_identifier + str(Bank.checksum))
        self.pin = random.randint(0, 9999)
        Bank.accounts.update({self.pin: self.card_number})

    @staticmethod
    def add_zeros(num, length):
        if len(str(num)) < length:
            missing_zero = "0" * (length - len(str(num)))
            return missing_zero + str(num)
        return str(num)


def print_menu(menu):
    for key, value in menu.items():
        print(f"{key}. {value}")


if __name__ == "__main__":
    starting_menu = {1: "Create an account", 2: "Log into account", 0: "Exit"}
    logging_in_menu = {1: "Balance", 2: "Log out", 0: "Exit"}

    action = None
    while not action:
        print_menu(starting_menu)
        action = input()
        if action == 1:
            pass
        elif action == 2:
            pass

        action = True
