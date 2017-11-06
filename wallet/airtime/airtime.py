from wallet.utils.settings import list_providers, buy_airtime


class Airtime():
    def __init__(self, config):
        self.__util = config

    def list_providers(self):
        return self.__util.post_requests(list_providers, {})

    def purchase(self, code, amount, phone_number):
        data = {'Code': code, 'Amount': amount, 'PhoneNumber': phone_number}

        return self.__util.post_requests(buy_airtime, data)