import random


class Account:
    BIN = 400000
    checksum = 5

    def __init__(self):
        self.account_identifier = self.add_zeros(random.randint(0, int('9' * 9)), 9)
        self.card_number = str(self.BIN) + self.account_identifier + str(self.checksum)
        self.pin = self.add_zeros(random.randint(0, 9999), 4)
        self.balance = 0

    def __repr__(self):
        return self.account_identifier

    @staticmethod
    def add_zeros(num, length):
        """ Adds any missing leading zeros. Returns: A string of numbers"""
        if len(str(num)) < length:
            missing_zero = "0" * (length - len(str(num)))
            return missing_zero + str(num)
        return str(num)

    def get_card_number(self):
        return self.card_number

    def get_pin(self):
        return self.pin

    def get_balance(self):
        return self.balance


class Menu:
    pages = {}
    current_page = None

    def __init__(self):
        self.menu = None

    def print_current_menu(self):
        current_page = self.current_page
        menu_book = self.pages
        if current_page:
            for key, value in menu_book[current_page].items():
                print(f"{key}. {value}")
        else:
            print("There is no current menu to print.")

    def set_current_page(self, new_page):
        self.current_page = new_page

    def get_current_page(self):
        return self.current_page

    def get_menu_book(self):
        return self.pages

    def is_page_currently_on(self, page):
        """ Checks what is the current page"""
        if self.current_page == page:
            return True
        return False


class StartingMenu(Menu):
    def __init__(self):
        super().__init__()
        self.menu = {1: "Create an account", 2: "Log into account", 0: "Exit"}
        self.pages.update({"Home": self.menu})


class AccountMenu(Menu):
    def __init__(self):
        super().__init__()
        self.menu = {1: "Balance", 2: "Log out", 0: "Exit"}
        self.pages.update({"Account": self.menu})


def create_account(bank):
    account = Account()
    bank.append(account)
    print(f"Your card number: \n{account.get_card_number()}")
    print(f"Your card PIN: \n{account.get_pin()}")
    print()
    return account


def load_menu():
    menu = Menu()
    StartingMenu()
    AccountMenu()
    menu.set_current_page("Home")
    return menu


def check_account_exist(banking_accounts, card_number, pin):
    for account in banking_accounts:
        if card_number == account.get_card_number() and pin == account.get_pin():
            return account


def main():
    leave = None
    banking_accounts = []
    account_logged_in = None
    menu = load_menu()
    while not leave:
        if menu.is_page_currently_on("Home"):
            menu.print_current_menu()
            action_input = int(input())
            print()
            if action_input == 1:  # Creating an account
                create_account(banking_accounts)
            elif action_input == 2:  # Log into account
                exist = check_account_exist(banking_accounts,
                                            input("Enter your card number: "),
                                            input("Enter your PIN: "))
                print()
                if exist:
                    print("You have successfully logged in!")
                    print()
                    account_logged_in = exist
                    menu.set_current_page("Account")
                else:
                    print("Wrong card number or PIN!")
                    print()
            elif action_input == 0:  # Exit
                leave = True
        elif menu.is_page_currently_on("Account"):
            menu.print_current_menu()
            action_input = int(input())
            print()
            if action_input == 1:  # Check balance
                print(f"Balance: {account_logged_in.get_balance()}")
            elif action_input == 2:  # Log out
                print("You have successfully logged out!")
                print()
                menu.set_current_page("Home")
            elif action_input == 0:  # Exit
                leave = True
    print("Bye!")


if __name__ == "__main__":
    main()
