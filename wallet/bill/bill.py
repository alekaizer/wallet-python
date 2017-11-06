from wallet.utils.settings import list_categories, list_billers, \
    list_payment_items, bill_validation, pay_bill


class Bill:
    def __init__(self, config):
        self.__util = config

    def list_categories(self):
        response = self.__util.post_requests(list_categories)
        categories = None
        if response.get('ResponseCode') == "200":
            categories = response.get('Categories')

        return categories

    def get_billers(self, category_id):
        response = self.__util.post_requests(list_billers.format(category_id))
        billers = None
        if response.get('ResponseCode') == "200":
            billers = response.get('Billers')

        return billers

    def get_payment_items(self, category_id):
        response = self.__util.post_requests(list_payment_items.format(category_id))
        payment_items = None
        if response.get('ResponseCode') == "200":
            payment_items = response.get('PaymentItems')

        return payment_items

    def validate(self, payment_code, customer_id):
        data = {'PaymentCode': payment_code, 'CustomerId': customer_id}

        response = self.__util.post_requests(bill_validation, data)

        return response.get('Message')

    def pay(self, payment_code, bill_name, phone_number, amount, customer_id,
            transaction_reference):
        data = {'PaymentCode': payment_code, 'BillName': bill_name,
                'PhoneNumber': phone_number,
                'CustomerId': customer_id,
                'TransactionReference': transaction_reference,
                'Amount': amount}

        response = self.__util.post_requests(pay_bill, data)
        return response.get('Message')
