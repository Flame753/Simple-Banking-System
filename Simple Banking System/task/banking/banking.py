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
    page = "home"

    def __init__(self):
        self.menu = None

    def print_menu(self):
        for key, value in self.menu.items():
            print(f"{key}. {value}")

    @staticmethod
    def page_switch(new_page):
        Menu.page = new_page

    @staticmethod
    def is_page(page):
        """ Checks what is the current page"""
        if Menu.page == page:
            return True
        return False


class StartingMenu(Menu):
    def __init__(self):
        super().__init__()
        self.menu = {1: "Create an account", 2: "Log into account", 0: "Exit"}


class AccountMenu(Menu):
    def __init__(self):
        super().__init__()
        self.menu = {1: "Balance", 2: "Log out", 0: "Exit"}


def get_action():
    if Menu.is_page("home"):
        StartingMenu().print_menu()
    elif Menu.is_page("account"):
        AccountMenu().print_menu()

    action_input = input()
    if action_input == 1:  # Creating an account or Check balance
        if Menu.is_page("home"):
            pass
        elif Menu.is_page("account"):
            pass
    elif action_input == 2:  # Log into account or Log out
        if Menu.is_page("home"):
            pass
        elif Menu.is_page("account"):
            pass
    elif action_input == 0:  # Exit
        return True


if __name__ == "__main__":
    action = None
    while not action:
        action = get_action()
