from timewreport.interval import TimeWarriorInterval


def test_interval_should_be_hashable():
    a = TimeWarriorInterval("20180816T100209Z", "20180816T110209Z", [], None)
    b = TimeWarriorInterval("20180816T090319Z", "20180816T100700Z", [], None)

    assert {a, b}
