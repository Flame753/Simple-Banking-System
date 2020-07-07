import random
import sys


class Card:
    def __init__(self, card, pin, account, balance):
        self.card = card
        self.pin = pin
        self.account = account
        self.balance = balance


class Bank:
    def __init__(self, bank_id):
        self.bank_id = bank_id
        self.cards: dict = dict()
        self.active_card: Card = None

    def run(self):
        while True:
            print('1. Create an account')
            print('2. Log into account')
            print('0. Exit\n')
            action = input()
            if action == '1':
                self.create_account()
            elif action == '2':
                self.login()
            elif action == '0':
                break

    def create_account(self):
        while True:
            account = format(random.randint(0, int("9" * 9)), '09d')
            card = f'{self.bank_id}{account}5'
            try:
                has = self.cards[card]
            except KeyError:
                pin = format(random.randint(0, 9999), '04d')
                self.cards[card] = Card(card, pin, account, 0)
                break
        print('Your card has been created')
        print('Your card number:')
        print(card)
        print('Your card PIN:')
        print(pin)

    def login(self):
        card = input('Enter your card number:')
        pin = input('Enter your PIN:')
        if self.check_card(card, pin):
            self.active_card = self.cards[card]
            print('You have successfully logged in!')
            self.run_logged()
        else:
            print('Wrong card number or PIN!')

    def check_card(self, card, pin) -> bool:
        try:
            c = self.cards[card]
            if c.pin == pin:
                return True
        except KeyError:
            return False
        return False

    def run_logged(self):
        while True:
            print('1. Balance')
            print('2. Log out')
            print('0. Exit   ')
            action = input()
            if action == '1':
                self.show_balance()
            elif action == '2':
                self.logout()
                break
            elif action == '0':
                sys.exit()

    def logout(self):
        self.active_card = None
        print('You have successfully logged out!')

    def show_balance(self):
        if self.active_card == None:
            return
        balance = self.active_card.balance
        print(f"Balance: {balance}")


if __name__ == "__main__":
    m = Bank('400000')
    m.run()
