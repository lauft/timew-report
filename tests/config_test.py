import pytest

from timewreport.config import TimeWarriorConfig


def test_get_value_should_return_value_if_key_available():
    config = TimeWarriorConfig({'FOO': 'foo'})

    assert config.get_value('FOO', 'bar') == 'foo'


def test_get_value_should_return_default_if_key_not_available():
    config = TimeWarriorConfig({'BAR': 'foo'})

    assert config.get_value('FOO', 'bar') == 'bar'


@pytest.fixture(scope='function', params=['on', 1, 'yes', 'y', 'true'])
def trueish_value(request):
    return request.param


def test_get_boolean_should_return_true_on_trueish_values(trueish_value):
    config = TimeWarriorConfig({'KEY': trueish_value})

    assert config.get_boolean('KEY', False) is True


def test_get_boolean_should_return_false_on_falseish_values():
    config = TimeWarriorConfig({'KEY': 'foo'})

    assert config.get_boolean('KEY', True) is False
