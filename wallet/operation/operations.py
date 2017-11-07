from wallet.utils.settings import charge_wallet, credit_wallet, get_balance
from wallet.utils.settings import create_wallet as _create_wallet


class Operations():
    def __init__(self, config):
        self.__util = config

    def charge_wallet(self, transaction_reference, phone_number,
                      transaction_pin,
                      amount):
        data = {'TransactionReference': transaction_reference,
                'PhoneNumber': phone_number,
                'TransactionPin': transaction_pin, 'Amount': amount}

        return self.__util.self.__util.post_requests(charge_wallet, data)

    def credit_wallet(self, transaction_reference, phone_number, amount):
        data = {'TransactionReference': transaction_reference,
                'PhoneNumber': phone_number,
                'Amount': amount}

        return self.__util.post_requests(credit_wallet, data)

    def get_balance(self, phone_number, transaction_pin):
        data = {'PhoneNumber': phone_number, 'TransactionPin': transaction_pin}

        response = self.__util.post_requests(get_balance, data)
        response['Balance'] = response.get('Message')
        return response

    def create_wallet(self, first_name, last_name, email, phone_number,
                      password):
        data = {'FirstName': first_name, 'LastName': last_name, 'Email': email,
                'phoneNumber': phone_number, 'Password': password}

        return self.__util.post_requests(_create_wallet, data)
