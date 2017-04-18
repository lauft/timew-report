import json
import re

from timewreport.config import TimeWarriorConfig
from timewreport.interval import TimeWarriorInterval


class TimeWarriorParser(object):
    def __init__(self, input_stream):
        self.__config = self.__parse_configuration_section(input_stream)
        self.__intervals = self.__parse_intervals_section(input_stream)

    @staticmethod
    def __parse_configuration_section(input_stream):
        config = {}

        for line in input_stream:
            if line == u'\x0A':
                break

            m = re.search('^([^:]+): (.*)$', line, re.MULTILINE)
            config[m.group(1)] = m.group(2)

        return TimeWarriorConfig(config)

    @staticmethod
    def __parse_intervals_section(input_stream):
        json_string = ''

        for line in input_stream:
            json_string += line

        intervals = []

        for interval in json.loads(json_string):
            intervals.append(TimeWarriorInterval(
                interval['start'],
                interval['end'] if 'end' in interval else None,
                interval['tags'] if 'tags' in interval else []
            ))

        return intervals

    def get_config(self):
        return self.__config

    def get_intervals(self):
        return self.__intervals
