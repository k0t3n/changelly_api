import json


def test_generate_sign(api):
    data = {
        'test': 'payload'
    }
    json_data = json.dumps(data)
    sign = api._generate_sign(json_data)

    assert sign == 'd2569cf9fc610f335c1fb562289845e99e708abf1793afccd5626f368cc486b1' \
                   '9e9ec05723a27b3afed855a35ef05fe09d30835217d061f0329fb83b696312de'
