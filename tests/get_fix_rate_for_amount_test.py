from unittest.mock import Mock, patch

import pytest
import requests_mock

from changelly_api.conf import API_ROOT_URL
from changelly_api.exceptions import AmountGreaterThanMaximum, AmountLessThanMinimum


@requests_mock.Mocker(kw='requests_mock')
def test(api, get_fix_rate_for_amount_data, **kwargs):
    r_mock = kwargs['requests_mock']
    r_mock.post(API_ROOT_URL, json=get_fix_rate_for_amount_data['response'])
    response = api.get_fix_rate_for_amount(get_fix_rate_for_amount_data['request'])

    assert response == get_fix_rate_for_amount_data['response']['result']


@patch('changelly_api.ChangellyAPI.get_fix_rate_for_amount')
@requests_mock.Mocker(kw='requests_mock')
def test_invalid_minimum_amount(get_fix_rate_for_amount_mock, api, get_fix_rate_for_amount_data, **kwargs):
    minimum_amount = 10
    get_fix_rate_for_amount_mock.side_effect = Mock(side_effect=AmountLessThanMinimum(minimum_amount))
    r_mock = kwargs['requests_mock']
    r_mock.post(API_ROOT_URL, json=get_fix_rate_for_amount_data['response'])
    with pytest.raises(AmountLessThanMinimum) as error:
        api.get_fix_rate_for_amount(get_fix_rate_for_amount_data['request'])

    assert error.value.threshold_value == minimum_amount


@patch('changelly_api.ChangellyAPI.get_fix_rate_for_amount')
@requests_mock.Mocker(kw='requests_mock')
def test_invalid_maximum_amount(get_fix_rate_for_amount_mock, api, get_fix_rate_for_amount_data, **kwargs):
    maximum_amount = 10
    get_fix_rate_for_amount_mock.side_effect = Mock(side_effect=AmountGreaterThanMaximum(maximum_amount))
    r_mock = kwargs['requests_mock']
    r_mock.post(API_ROOT_URL, json=get_fix_rate_for_amount_data['response'])
    with pytest.raises(AmountGreaterThanMaximum) as error:
        api.get_fix_rate_for_amount(get_fix_rate_for_amount_data['request'])

    assert error.value.threshold_value == maximum_amount
