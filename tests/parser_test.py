import pytest
import re

from timewreport.interval import TimeWarriorInterval
from timewreport.parser import TimeWarriorParser


@pytest.fixture(scope='function')
def plain_export(tmpdir):
    fn = tmpdir.mkdir('data').join('plain_export')
    fn.write("""\
name1: value1
name2: value2
name3: value3

[]
""")
    return fn


@pytest.fixture(scope='function', params=['on', 1, 'yes', 'y', 'true'])
def export_with_verbose(tmpdir, request):
    fn = tmpdir.mkdir('data').join('export_with_verbose')
    fn.write("""\
name1: value1
name2: value2
name3: value3
verbose: {}

[]
""".format(request.param))
    return fn


@pytest.fixture(scope='function', params=['on', 1, 'yes', 'y', 'true'])
def export_with_debug(tmpdir, request):
    fn = tmpdir.mkdir('data').join('export_with_debug')
    fn.write("""\
debug: {}
name1: value1
name2: value2
name3: value3

[]
""".format(request.param))
    return fn


@pytest.fixture(scope='function', params=['on', 1, 'yes', 'y', 'true'])
def export_with_confirmation(tmpdir, request):
    fn = tmpdir.mkdir('data').join('export_with_confirmation')
    fn.write("""\
confirmation: {}
name1: value1
name2: value2
name3: value3

[
]
""".format(request.param))
    return fn


@pytest.fixture(scope='function')
def export_with_intervals(tmpdir):
    fn = tmpdir.mkdir('data').join('export_with_confirmation')
    fn.write("""\

[
{"start":"20160405T160000Z","end":"20160405T161000Z","tags":["This is a multi-word tag","ProjectA","tag123"]},
{"start":"20160405T161000Z","end":"20160405T162000Z","tags":["This is a multi-word tag","ProjectA","tag123"]},
{"start":"20160405T162000Z","end":"20160405T163000Z","tags":["This is a multi-word tag","ProjectA","tag123"]}
]
""")
    return fn


def test_parser_with_default_settings(plain_export):
    parser = TimeWarriorParser(plain_export.open('r'))

    config = parser.get_config()

    assert (config.get_boolean('verbose', True) is False)
    assert (config.get_boolean('debug', True) is False)
    assert (config.get_boolean('confirmation', True) is False)


def test_parser_should_detect_verbose_setting(export_with_verbose):
    parser = TimeWarriorParser(export_with_verbose.open('r'))

    config = parser.get_config()

    assert (config.get_boolean('verbose', False) is True)


def test_parser_should_detect_debug_setting(export_with_debug):
    parser = TimeWarriorParser(export_with_debug.open('r'))

    config = parser.get_config()

    assert (config.get_boolean('debug', False) is True)


def test_parser_should_detect_confirmation_setting(export_with_confirmation):
    parser = TimeWarriorParser(export_with_confirmation.open('r'))

    config = parser.get_config()

    assert (config.get_boolean('confirmation', False) is True)


def test_parser_should_parse_intervals(export_with_intervals):
    parser = TimeWarriorParser(export_with_intervals.open('r'))

    intervals = parser.get_intervals()
    expected = [
        TimeWarriorInterval('20160405T160000Z', '20160405T161000Z', ['This is a multi-word tag', 'ProjectA', 'tag123']),
        TimeWarriorInterval('20160405T161000Z', '20160405T162000Z', ['This is a multi-word tag', 'ProjectA', 'tag123']),
        TimeWarriorInterval('20160405T162000Z', '20160405T163000Z', ['This is a multi-word tag', 'ProjectA', 'tag123']),
    ]
    assert (intervals == expected)