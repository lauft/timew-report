from datetime import datetime, timedelta

from dateutil.tz import tz

from timewreport.interval import TimeWarriorInterval


def test_interval_should_be_hashable():
    a = TimeWarriorInterval("20180816T100209Z", "20180816T110209Z", [], None)
    b = TimeWarriorInterval("20180816T090319Z", "20180816T100700Z", [], None)

    assert {a, b}


def test_interval_should_be_creatable_from_utc_string():
    test_start = datetime.now(tz=tz.tzlocal()).replace(microsecond=0)
    test_start_utc = test_start.utcnow()
    test_end = test_start + timedelta(hours=1)
    test_end_utc = test_start_utc + timedelta(hours=1)

    interval = TimeWarriorInterval(
        "{:%Y%m%dT%H%M%S}Z".format(test_start_utc),
        "{:%Y%m%dT%H%M%S}Z".format(test_end_utc),
        [],
        None)

    assert interval.get_start() == test_start and interval.get_end() == test_end


def test_interval_should_be_creatable_from_local_string():
    test_start = datetime.now(tz=tz.tzlocal()).replace(microsecond=0)
    test_end = test_start + timedelta(hours=1)

    interval = TimeWarriorInterval(
        "{:%Y%m%dT%H%M%S}".format(test_start),
        "{:%Y%m%dT%H%M%S}".format(test_end),
        [],
        None)

    assert interval.get_start() == test_start and interval.get_end() == test_end
