from wallet.airtime import Airtime
from wallet.bank import Bank
from wallet.bill import Bill
from wallet.operation import Operations
from wallet.transaction import Transaction
from wallet.utils.functions import Config


class Wallet(object):
    def __init__(self, secret_key, public_key):
        self.config = Config(secret_key, public_key)
        self.bank = Bank(self.config)
        self.bill = Bill(self.config)
        self.operations = Operations(self.config)
        self.transaction = Transaction(self.config)
        self.airtime = Airtime(self.config)
