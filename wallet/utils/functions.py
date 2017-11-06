import requests
import json
from Crypto.Cipher import DES3
from hashlib import md5
import base64

from wallet.utils.settings import baseUrl, AUTH_HEADER


class Config(object):
    def __init__(self, secret_key, public_key):
        self.secret_key = secret_key
        self.public_key = public_key

    def post_requests(self, url, data=None):
        if data is None:
            data = dict()
        else:
            data = self.encrypt_sensibles(data)
            data['SecretKey'] = self.secret_key

        _url = baseUrl + url
        headers = {'Authorization': AUTH_HEADER.format(self.public_key),
                   'Content-Type': 'application/json'}
        req = requests.post(_url, data=json.dumps(data), headers=headers)

        return json.loads(req.text)

    def encrypt_sensibles(self, data):
        if 'TransactionReference' in data:
            data['TransactionReference'] = self.encrypt(
                data.get('TransactionReference'))
        if 'Password' in data:
            data['Password'] = self.encrypt(data.get('Password'))
        if 'PhoneNumber' in data:
            data['PhoneNumber'] = self.encrypt(data.get('PhoneNumber'))
        if 'TransactionPin' in data:
            data['TransactionPin'] = self.encrypt(data.get('TransactionPin'))
        if 'Amount' in data:
            data['Amount'] = self.encrypt(data.get('Amount'))

        return data

    def get_requests(self, url):
        pass

    def encrypt(self, message, enable_hashing=True):
        if enable_hashing:
            hashed_key = md5(self.public_key.encode()).digest()
        else:
            hashed_key = self.public_key

        block_size = 8
        padding_size = block_size - (len(message) % block_size)

        if padding_size > 0:
            message += chr(padding_size)*padding_size
        cipher = DES3.new(hashed_key, DES3.MODE_ECB)
        ciphered = cipher.encrypt(message.encode('utf-8'))
        return base64.b64encode(ciphered).decode('utf-8')
