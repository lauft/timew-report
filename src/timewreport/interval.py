from datetime import datetime, date
from importlib.metadata import version

import dateutil.parser

from dateutil.tz import tz
from deprecated import deprecated

VERSION = version('timew_report').split("+")[0]


class TimeWarriorInterval(object):
    def __init__(self, ID, start, end, tags, annotation):
        self.__id = ID
        self.__start = self.__get_local_datetime(start)
        self.__end = self.__get_local_datetime(end) if end is not None else None
        self.__tags = tags
        self.__annotation = annotation

    def __eq__(self, other):
        return self.__id == other.get_id() \
            and self.__start == other.get_start() \
            and self.__end == other.get_end() \
            and self.__tags == other.get_tags() \
            and self.__annotation == other.get_annotation()

    def __hash__(self):
        return hash(repr(self))

    def get_id(self):
        return self.__id

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

    @deprecated(version='1.4.0', reason="Disallowed in v2.0.0, use ``get_start_date`` instead")
    def get_date(self):
        return date(self.__start.year, self.__start.month, self.__start.day)

    def get_start_date(self):
        return date(self.__start.year, self.__start.month, self.__start.day)

    def get_end_date(self):
        if self.is_open():
            return date.today()

        return date(self.__end.year, self.__end.month, self.__end.day)

    @staticmethod
    def __get_local_datetime(datetime_input):
        if type(datetime_input) is str:
            local_datetime = dateutil.parser.parse(datetime_input)
        elif type(datetime_input) is datetime:
            if datetime_input.tzinfo is None:
                local_datetime = datetime_input.replace(tzinfo=tz.tzutc())
            else:
                local_datetime = datetime_input

        else:
            raise TypeError("Unknown type for datetime input: {}".format(type(datetime_input)))

        return local_datetime.astimezone(tz.tzlocal())
