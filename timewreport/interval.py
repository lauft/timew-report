import dateutil.parser

from datetime import datetime, date
from dateutil.tz import tz


class TimeWarriorInterval(object):
    def __init__(self, start, end, tags, annotation):
        self.__start = self.__get_local_datetime(start)
        self.__end = self.__get_local_datetime(end) if end is not None else None
        self.__tags = tags
        self.__annotation = annotation

    def __eq__(self, other):
        return self.__start == other.get_start() \
            and self.__end == other.get_end() \
            and self.__tags == other.get_tags() \
            and self.__annotation == other.get_annotation()

    def __hash__(self):
        return hash(repr(self))

    def get_start(self):
        return self.__start

    def get_end(self):
        return self.__end

    def get_tags(self):
        return self.__tags

    def get_annotation(self):
        return self.__annotation

    def is_open(self):
        return self.__end is None

    def get_duration(self):
        if self.is_open():
            return datetime.now(tz=tz.tzlocal()) - self.__start
        else:
            return self.__end - self.__start

    def get_date(self):
        return date(self.__start.year, self.__start.month, self.__start.day)

    def __get_local_datetime(self, datetime_string):
        from_zone = tz.tzutc()
        to_zone = tz.tzlocal()

        date = dateutil.parser.parse(datetime_string)
        date.replace(tzinfo=from_zone)

        return date.astimezone(to_zone)
