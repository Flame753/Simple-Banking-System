import random


class Bank:
    BIN = 400000
    checksum = 5
    accounts = {}

    def __init__(self):
        self.account_identifier = Bank.add_zeros(random.randint(0, int('9' * 9)), 9)
        self.card_number = int(str(Bank.BIN) + self.account_identifier + str(Bank.checksum))
        self.pin = Bank.add_zeros(random.randint(0, 9999), 4)
        self.user_name = "User" + self.account_identifier
        self.balance = 0
        self.add_to_data_base()

    def add_to_data_base(self):
        Bank.accounts.update({self.user_name: {'pin': self.pin,
                                               'card number': self.card_number,
                                               'balance': self.balance}})

    @staticmethod
    def add_zeros(num, length):
        """ Adds any missing leading zeros"""
        if len(str(num)) < length:
            missing_zero = "0" * (length - len(str(num)))
            return missing_zero + str(num)
        return str(num)


class Menu:
    def __init__(self):
        self.menu = None
        self.page = None

    def print_menu(self):
        for key, value in self.menu.items():
            print(f"{key}. {value}")

    def page_switch(self, new_page):
        self.page = new_page

    @staticmethod
    def exit():
        return True


class StartingMenu(Menu):
    def __init__(self):
        super().__init__()
        self.menu = {1: "Create an account", 2: "Log into account", 0: "Exit"}
        self.page = "starting"


class AccountMenu(Menu):
    def __init__(self):
        super().__init__()
        self.menu = {1: "Balance", 2: "Log out", 0: "Exit"}
        self.page = "account"


if __name__ == "__main__":
    print(Menu().menu)
    print(StartingMenu().menu)
    a = Bank().accounts
    print(a)




    action = "s"
    while not action:
        print_menu(starting_menu)
        action = input()
        if action == 1:
            pass
        elif action == 2:
            pass

        action = True
