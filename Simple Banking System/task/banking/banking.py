import random
import sys
import sqlite3


class Bank:
    def __init__(self, bank_id):
        self.bank_id = bank_id
        self.active_card = None

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
        account = format(random.randint(0, int("9" * 9)), '09d')
        card = f'{self.bank_id}{account}0'
        check_sum = self.luhn_algorithm(card)
        card = f'{self.bank_id}{account}{check_sum}'  # Set card number
        pin = format(random.randint(0, 9999), '04d')
        insert_card(account, card, pin)
        print('Your card has been created')
        print('Your card number:')
        print(card)
        print('Your card PIN:')
        print(pin)

    def login(self):
        card = input('Enter your card number:')
        pin = input('Enter your PIN:')
        if self.check_card(card, pin):
            self.active_card = retrieve_card_info(card, pin)
            print('You have successfully logged in!')
            self.run_logged()
        else:
            print('Wrong card number or PIN!')

    def check_card(self, user_card, user_pin) -> bool:
        try:
            card_info = retrieve_card_info(user_card, user_pin)
            number = card_info['number']
            pin = card_info['pin']
            if pin == user_pin and self.luhn_algorithm(user_card) == int(number[-1]):
                return True
        except TypeError:
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
                conn.commit()
                cur.close()
                sys.exit()

    def logout(self):
        self.active_card = None
        print('You have successfully logged out!')

    def show_balance(self):
        if not self.active_card:  # Card doesn't exist
            return
        balance = self.active_card["balance"]
        print(f"Balance: {balance}")

    @staticmethod
    def luhn_algorithm(card):
        card_num = [int(x) for x in str(card)]
        card_num.pop()  # Drop the last digit
        for position in range(len(card_num)):
            if (position + 1) % 2 == 1:
                card_num[position] = card_num[position] * 2  # Multiply odd position by 2
                if card_num[position] > 9:
                    card_num[position] = card_num[position] - 9  # Subtract 9 to numbers over 9
        total = sum(card_num)  # Add all numbers
        check_sum = 10 - (total % 10)
        if check_sum == 10:
            check_sum = 0
        return check_sum


def insert_card(account, card, pin):
    cur.execute('INSERT INTO card (id, number, pin)VALUES (?, ?, ?)', (account, card, pin))
    conn.commit()


def retrieve_card_info(card_number, pin):
    card_info = ('id', 'number', 'pin', 'balance')
    cur.execute('SELECT * FROM card WHERE number = ? AND pin = ?', (card_number, pin))
    card_values = cur.fetchone()
    card_dict = dict()
    for position, name in enumerate(card_info):
        card_dict[name] = card_values[position]
    return card_dict


if __name__ == "__main__":
    # define connection and cursor
    conn = sqlite3.connect('card.s3db')
    cur = conn.cursor()
    # Create a Table
    cur.execute('CREATE TABLE IF NOT EXISTS card ('
                'id INTEGER, '
                'number VARCHAR(16), '
                'pin VARCHAR(4), '
                'balance INTEGER DEFAULT 0);')
    conn.commit()
    m = Bank('400000')
    m.run()
    conn.commit()
    # Close connection
    conn.close()
