from wallet.utils.settings import new_transaction, transaction_details


class Transaction():
    def __init__(self, config):
        self.__util = config

    def create_transaction(self, merchant_reference, amount, name, email,
                           phone_number, redirect_url=None):
        data = {'MerchantReference': merchant_reference, 'Amount': amount,
                'Name': name, 'Email': email, 'PhoneNumber': phone_number}
        if redirect_url:
            data['RedirectUrl'] = redirect_url

        return self.__util.post_requests(new_transaction, data)

    def get_details(self, transaction_reference):
        data = {'TransactionReference': transaction_reference}

        return self.__util.post_requests(transaction_details, data)
