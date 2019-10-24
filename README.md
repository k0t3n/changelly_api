# Changelly API
**Changelly API** is a python wrapper library over Changelly RPC API.
Please, [read the docs](https://github.com/changelly/api-changelly) before usage.

## Examples
```python
from changelly_api import ChangellyAPI

api = ChangellyAPI('<your_api_key_here>', '<your_secret_here>')

# create float rate tx
float_tx = api.create_transaction('btc', 'eth', 1, '<your_addres_here>')

# create fixed rate tx
rate = api.get_fix_rate_for_amount([{'from': 'btc', 'to': 'eth', 'amountFrom': 0.5}])[0]
tx = api.create_fix_transaction(
    currency_from='btc', currency_to='eth',
    address='0x514910771AF9Ca656af840dff83E8264EcF986CA', refund_address='0x514910771AF9Ca656af840dff83E8264EcF986CA',
    amount_from=rate['amountFrom'], amount_to=rate['amountTo'],
    rate_id=rate['id']
)

```
Supported methods:
* getCurrencies
* getCurrenciesFull
* getMinAmount
* createTransaction
* createFixedTransaction
* getFixRate
* getFixRateForAmount
* validateAddress
* getTransactions
