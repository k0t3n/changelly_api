import hashlib
import hmac
import json
from json import JSONDecodeError

import requests

from changelly_api.exceptions import *


class ChangellyAPI:
    def __init__(self, api_key, secret, url='https://api.changelly.com'):
        self._api_key = api_key
        self._secret = secret
        self._url = url

    def _generate_sign(self, json_data):
        return hmac.new(self._secret.encode('utf-8'), json_data.encode('utf-8'), hashlib.sha512).hexdigest()

    def _parse_response(self, response):
        if response.status_code == 401:
            raise AuthorizationError('Invalid api_key or api_secret')
        elif response.status_code != 200:
            raise UnexpectedResponseStatusCode(
                f'Unexpected response status code received: {response.status_code} {response.text}')

        try:
            data = response.json()
        except JSONDecodeError:
            raise JSONResponseParseError('Error parsing JSON response')

        if data.get('error'):
            raise ChangellyAPIError(data['error'])

        return data.get('result')

    def _make_request(self, method, params=None):
        message = {
            'jsonrpc': '2.0',
            'id': 1,
            'method': method,
            'params': params or []
        }

        serialized_data = json.dumps(message)

        sign = hmac.new(self._secret.encode('utf-8'), serialized_data.encode('utf-8'), hashlib.sha512).hexdigest()

        headers = {'api-key': self._api_key, 'sign': sign, 'Content-type': 'application/json'}
        response = requests.post(self._url, headers=headers, data=serialized_data)

        return self._parse_response(response)

    def get_currencies(self, currency_from, currency_to, **kwargs):
        method = 'getCurrencies'
        data = {
            'from': currency_from,
            'to': currency_to,
            **kwargs
        }

        return self._make_request(method, data)

    def get_currencies_full(self, **kwargs):
        method = 'getCurrenciesFull'

        return self._make_request(method, kwargs)

    def get_min_amount(self, **kwargs):
        method = 'getMinAmount'

        return self._make_request(method, kwargs)

    def create_transaction(self, currency_from, currency_to, amount, address, **kwargs):
        method = 'createTransaction'
        data = {
            'from': currency_from,
            'to': currency_to,
            'amount': amount,
            'address': address,
            **kwargs
        }

        return self._make_request(method, data)

    def validate_address(self, currency, address, **kwargs):
        method = 'validateAddress'
        data = {
            # TODO: validate ticker using getCurrenciesFull method
            'currency': currency,
            'address': address,
            **kwargs
        }

        return self._make_request(method, data)

    def get_transactions(self, **kwargs):
        method = 'getTransactions'

        return self._make_request(method, **kwargs)

    def get_fix_rate(self, pairs_list):
        method = 'getFixRate'
        # TODO: validate pairs_list
        return self._make_request(method, pairs_list)

    def get_fix_rate_for_amount(self, pairs_list):
        method = 'getFixRateForAmount'
        # TODO: validate pairs_list
        return self._make_request(method, pairs_list)

    def get_fix_rate_bulk(self, **kwargs):
        method = 'getFixRateBulk'

        return self._make_request(method, **kwargs)

    def create_fix_transaction(self, currency_from, currency_to, address, refund_address, amount_from, amount_to,
                               rate_id, **kwargs):
        method = 'createFixTransaction'
        data = {
            'from': currency_from,
            'to': currency_to,
            'address': address,
            'refundAddress': refund_address,
            'amountFrom': amount_from,
            'amountTo': amount_to,
            'rateId': rate_id,
            **kwargs
        }

        return self._make_request(method, data)
