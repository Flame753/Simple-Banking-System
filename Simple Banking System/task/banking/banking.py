import random


class Bank:
    BIN = 400000
    checksum = 5

    def __init__(self):
        self.account_identifier = random.randint(0, int('9' * 9))
        self.card_number = int(str(Bank.BIN) + str(self.account_identifier) + str(Bank.checksum))
        self.pin = random.randint(0, 9999)


if __name__ == "__main__":
    a = Bank()
    b = Bank()
    print(a.card_number, a.pin)
    print(b.card_number, b.pin)
    print(Bank().card_number)
    print(Bank().card_number)
    print(Bank().card_number)
    print(a.card_number, a.pin)
