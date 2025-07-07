import datetime

import pytest

from dateutil.tz import tz

from timewreport.interval import TimeWarriorInterval

UTC = datetime.UTC if hasattr(datetime, 'UTC') else datetime.timezone.utc


def test_get_date_is_deprecated():
    test_interval = TimeWarriorInterval(2, "20180816T090319Z", "20180816T100700Z", [], None)
    with pytest.deprecated_call():
        interval_start = test_interval.get_date()


def test_get_date_warning_has_version():
    test_interval = TimeWarriorInterval(2, "20180816T090319Z", "20180816T100700Z", [], None)
    with pytest.warns(DeprecationWarning) as record:
        start_date = test_interval.get_date()
        warn_msg = record[0].message.args[0]
    print(warn_msg)
    assert "Deprecated since version 1.4.0" in warn_msg


def test_interval_should_be_hashable():
    a = TimeWarriorInterval(1, "20180816T100209Z", "20180816T110209Z", [], None)
    b = TimeWarriorInterval(2, "20180816T090319Z", "20180816T100700Z", [], None)

    assert {a, b}


def test_interval_should_be_creatable_from_utc_string():
    test_start = datetime.datetime.now(tz=tz.tzlocal()).replace(microsecond=0)
    test_start_utc = test_start.now(UTC)
    test_end = test_start + datetime.timedelta(hours=1)
    test_end_utc = test_start_utc + datetime.timedelta(hours=1)

    interval = TimeWarriorInterval(
        1,
        "{:%Y%m%dT%H%M%S}Z".format(test_start_utc),
        "{:%Y%m%dT%H%M%S}Z".format(test_end_utc),
        [],
        None)

    assert interval.get_start() == test_start \
           and interval.get_end() == test_end \
           and interval.get_start_date() == test_start.date() \
           and interval.get_end_date() == test_end.date()


def test_interval_should_be_creatable_from_local_string():
    test_start = datetime.datetime.now(tz=tz.tzlocal()).replace(microsecond=0)
    test_end = test_start + datetime.timedelta(hours=1)

    interval = TimeWarriorInterval(
        1,
        "{:%Y%m%dT%H%M%S}".format(test_start),
        "{:%Y%m%dT%H%M%S}".format(test_end),
        [],
        None)

    assert interval.get_start() == test_start \
           and interval.get_end() == test_end \
           and interval.get_start_date() == test_start.date() \
           and interval.get_end_date() == test_end.date()


def test_interval_should_be_creatable_from_local_datetime():
    test_start = datetime.datetime.now(tz=tz.tzlocal()).replace(microsecond=0)
    test_end = test_start + datetime.timedelta(hours=1)

    interval = TimeWarriorInterval(
        1,
        test_start,
        test_end,
        [],
        None)

    assert interval.get_start() == test_start \
           and interval.get_end() == test_end \
           and interval.get_start_date() == test_start.date() \
           and interval.get_end_date() == test_end.date()


def test_interval_should_be_creatable_from_utc_datetime():
    test_start = datetime.datetime.now(tz=tz.tzlocal()).replace(microsecond=0)
    test_start_utc = test_start.now(UTC).replace(microsecond=0)
    test_end = test_start + datetime.timedelta(hours=1)
    test_end_utc = test_start_utc + datetime.timedelta(hours=1)

    interval = TimeWarriorInterval(
        1,
        test_start_utc,
        test_end_utc,
        [],
        None)

    assert interval.get_start() == test_start \
           and interval.get_end() == test_end \
           and interval.get_start_date() == test_start.date() \
           and interval.get_end_date() == test_end.date()
