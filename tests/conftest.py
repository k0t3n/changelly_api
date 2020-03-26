import pytest

from changelly_api import ChangellyAPI


@pytest.fixture(scope='module')
def api():
    return ChangellyAPI('key', 'secret')


@pytest.fixture()
def get_fix_rate_for_amount_data():
    return {
        'response': {
            "jsonrpc": "2.0",
            "id": 1,
            "result": {
                "id": "test",
                "from": "btc",
                "to": "eth",
                "result": "48.520938768637152700759353642",
                "amountFrom": "1",
                "amountTo": "48.520938768637152700"
            }
        },
        'request': {
            'from': 'btc',
            'to': 'eth',
            'amountFrom': 1,
        }
    }
