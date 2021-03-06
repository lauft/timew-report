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


@pytest.fixture(scope='function', params=['off', 0, 'no', 'n', 'false'])
def falseish_value(request):
    return request.param


def test_get_boolean_should_return_false_on_falseish_values(falseish_value):
    config = TimeWarriorConfig({'KEY': falseish_value})

    assert config.get_boolean('KEY', True) is False


def test_get_boolean_should_return_default_if_key_not_available():
    config = TimeWarriorConfig({})

    assert config.get_boolean('FOO', True) is True


def test_get_int_should_return_value_for_valid_strings():
    config = TimeWarriorConfig({'KEY': '1'})

    assert config.get_int('KEY', 2) == 1


def test_get_int_should_return_raise_exception_for_invalid_strings():
    with pytest.raises(ValueError):
        config = TimeWarriorConfig({'KEY': 'bla'})

        config.get_int('KEY', 2)


def test_get_int_should_return_default_if_key_not_available():
    config = TimeWarriorConfig({'BAR': '1'})

    assert config.get_int('FOO', 2) == 2
