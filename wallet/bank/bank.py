from wallet.utils.settings import list_bank, account_enquiry, account_transfer
from wallet.utils.settings import transfer_details


class Bank():
    def __init__(self, config):
        self.__util = config

    def list_banks(self):
        banks = self.__util.post_requests(list_bank)
        return banks

    def enquiry(self, bank_code, account_number):
        data = {'AccountNumber': account_number,
                'BankCode': bank_code}

        response = self.__util.post_requests(account_enquiry, data)
        return response

    def make_transfer(self, bank_code, account_number, account_name,
                      transfer_reference):
        data = {'BankCode': bank_code, 'AccountNumber': account_number,
                'AccountName': account_name,
                'TransactionReference': transfer_reference}

        response = self.__util.post_requests(account_transfer, data)

        return response

    def get_details(self, transfer_reference):
        data = {'TransactionReference': transfer_reference}

        return self.__util.post_requests(transfer_details, data)
