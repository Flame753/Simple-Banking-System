import random
import sys
import sqlite3


class Bank:
    def __init__(self, bank_id):
        self.bank_id = bank_id
        self.active_card = None
        self.data_base = DataBase()

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
                self.data_base.close_file()
                break
            self.data_base.dis_all()  # Test, will need to be removed

    def create_account(self):
        account = format(random.randint(0, int("9" * 9)), '09d')
        card = f'{self.bank_id}{account}0'
        check_sum = self.luhn_algorithm(card)
        card = f'{self.bank_id}{account}{check_sum}'  # Set card number
        pin = format(random.randint(0, 9999), '04d')
        self.data_base.insert_card(account, card, pin)
        print('Your card has been created')
        print('Your card number:')
        print(card)
        print('Your card PIN:')
        print(pin)

    def login(self):
        card = input('Enter your card number:')
        pin = input('Enter your PIN:')
        if self.check_card(card, pin):
            self.update_active_card(card, pin)
            print('You have successfully logged in!')
            self.run_logged()
        else:
            print('Wrong card number or PIN!')

    def check_card(self, user_card, user_pin) -> bool:
        try:
            card_info = self.data_base.retrieve_card_info(user_card, user_pin)
            number = card_info['number']
            pin = card_info['pin']
            if pin == user_pin and self.luhn_algorithm(user_card) == int(number[-1]):
                return True
        except TypeError:
            return False
        return False

    def run_logged(self):
        while True:
            print('1. Balance      ')
            print('2. Add income   ')
            print('3. Do transfer  ')
            print('4. Close account')
            print('5. Log out      ')
            print('0. Exit         ')
            action = input()
            if action == '1':
                self.show_balance()
            elif action == '2':
                self.add_income()
            elif action == '3':
                pass
            elif action == '4':
                self.close_account()
                break
            elif action == '5':
                self.logout()
                break
            elif action == '0':
                self.data_base.close_file()
                sys.exit()
            self.data_base.dis_all()  # Test, will need to be removed

    def logout(self):
        self.update_active_card()
        print('You have successfully logged out!')

    def close_account(self):
        id = self.active_card['id']
        card_number = self.active_card['number']
        pin = self.active_card['pin']
        self.data_base.delete_account(id, card_number, pin)
        self.update_active_card()
        print("The account has been closed!")

    def show_balance(self):
        if not self.active_card:  # Card doesn't exist
            return
        balance = self.active_card["balance"]
        print(f"Balance: {balance}")

    def add_income(self):
        amount = int(input('Enter income: '))
        id = self.active_card['id']
        card_number = self.active_card['number']
        pin = self.active_card['pin']
        self.data_base.add_to_balance(id, amount)
        self.update_active_card(card_number, pin)
        print('Income was added!')

    def update_active_card(self, card=None, pin=None):
        if card is None or pin is None:
            self.active_card = None
        else:
            self.active_card = self.data_base.retrieve_card_info(card, pin)

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


class DataBase:
    def __init__(self):
        # define connection and cursor
        self.conn = sqlite3.connect('card.s3db')
        self.cur = self.conn.cursor()
        # Create a Table
        self.cur.execute('CREATE TABLE IF NOT EXISTS card ('
                         'id INTEGER, '
                         'number TEXT, '
                         'pin TEXT, '
                         'balance INTEGER DEFAULT 0);')
        self.conn.commit()

    def insert_card(self, account, card, pin):
        self.cur.execute('INSERT INTO card (id, number, pin)VALUES (?, ?, ?);', (account, card, pin))
        self.conn.commit()

    def retrieve_card_info(self, card_number, pin):
        card_info = ('id', 'number', 'pin', 'balance')
        self.cur.execute('SELECT * FROM card WHERE number = ? AND pin = ?;', (card_number, pin))
        card_values = self.cur.fetchone()
        card_dict = dict()
        for position, name in enumerate(card_info):
            card_dict[name] = card_values[position]
        return card_dict

    def close_file(self):
        self.conn.commit()
        self.cur.close()

    def add_to_balance(self, id, amount):
        self.cur.execute('UPDATE card SET balance = balance + ? WHERE id = ?;', (amount, id))
        self.conn.commit()

    def do_transfer(self):
        pass

    def delete_account(self, id, card_number, pin):
        self.cur.execute('DELETE FROM card WHERE id = ? AND number = ? AND pin = ?;', (id, card_number, pin))
        self.conn.commit()

    def dis_all(self):  # For Testing
        self.cur.execute('SELECT * FROM card;')
        print(self.cur.fetchall())


if __name__ == "__main__":
    m = Bank('400000')
    m.run()
