from wallet import Wallet
import pprint

pp = pprint.PrettyPrinter(indent=2)

SECRET_KEY = 'YOUR_SECRET_KEY'
PUBLIC_KEY = 'YOUR_PUBLIC_KEY'
MERCHANT_ID = 'YOUR_MERCHANT_ID'
ACCOUNT_NUMBER = 'YOUR_ACCOUNT_NUMBER'
BANK_CODE = 'YOUR_BANK_CODE'

test_wallet = Wallet(SECRET_KEY, PUBLIC_KEY)


print("\n\n=============== OPERATION =============")
print(">>> Create Wallet")
r = test_wallet.operations.create_wallet("FIRST_NAME", "LAST_NAME",
                                         "YOUR_EMAIL",
                                         "YOUR_PHONE_NUMBER", "PASSWORD")
pp.pprint(r)


rr = test_wallet.operations.get_balance("YOUR_PHONE_NUMBER", "TRANSACTION_PIN")
print(">>> Balance")
pp.pprint(rr)

print("\n\n=============== AIRTIME =============")
print(">>> irtime Providers")
pp.pprint(test_wallet.airtime.list_providers())

print("\n\n=============== BANK =============")
print(">>> Banks")
pp.pprint(test_wallet.bank.list_banks())

print("\n\n=============== BILL =============")
categories = test_wallet.bill.list_categories()
print(">>> Categories")
pp.pprint(categories)

if categories:
    cat_id = categories[0].get('categoryid')
    print("\n>>> Get Billers")
    pp.pprint(test_wallet.bill.get_billers(cat_id))
    print("\n>>> Items")
    pp.pprint(test_wallet.bill.get_payment_items(cat_id))
