import random


class Bank:
    BIN = 400000
    checksum = 5

    def __init__(self):
        self.account_identifier = Bank.add_zeros(random.randint(0, int('9' * 9)), 9)
        self.card_number = int(str(Bank.BIN) + str(self.account_identifier) + str(Bank.checksum))
        self.pin = random.randint(0, 9999)

    @staticmethod
    def add_zeros(num, length):
        if len(str(num)) < length:
            missing_zero = "0" * (length - len(str(num)))
            return missing_zero + str(num)
        return num


if __name__ == "__main__":
    a = Bank()
    b = Bank()
    print(a.card_number, a.pin)
    print(b.card_number, b.pin)