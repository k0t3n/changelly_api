# Changelly API
[![Pypi](https://img.shields.io/pypi/v/changelly-api.svg)](https://pypi.python.org/pypi/changelly-api)
[![Build Status](https://travis-ci.com/k0t3n/changelly_api.svg?branch=master)](https://travis-ci.com/k0t3n/changelly_api)
[![codecov](https://codecov.io/gh/k0t3n/changelly_api/branch/master/graph/badge.svg)](https://codecov.io/gh/k0t3n/changelly_api)
![GitHub Pipenv locked Python version](https://img.shields.io/github/pipenv/locked/python-version/k0t3n/changelly_api)

**Changelly API** is a python wrapper library over Changelly RPC API.

Please, [read the docs](https://github.com/changelly/api-changelly) before usage.

## Usage
```python
from changelly_api import ChangellyAPI

api = ChangellyAPI('<your_api_key_here>', '<your_secret_here>')

# create float rate tx
float_tx = api.create_transaction('btc', 'eth', 1, '<your_addres_here>')

# create fixed rate tx
rate = api.get_fix_rate_for_amount([{'from': 'btc', 'to': 'eth', 'amountFrom': 0.5}])[0]
tx = api.create_fix_transaction(
    currency_from='btc', currency_to='eth',
    payout_address='<your_address_here>', refund_address='<your_address_here>',
    amount_from=rate['amountFrom'], amount_to=rate['amountTo'],
    rate_id=rate['id']
)

```
Supported methods:
* getCurrencies
* getCurrenciesFull
* getMinAmount
* getPairsParams
* getExchangeAmount
* createTransaction
* createFixedTransaction
* getFixRate
* getFixRateBulk
* getFixRateForAmount
* validateAddress
* getTransactions
