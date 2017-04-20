import json
import re

from timewreport.config import TimeWarriorConfig
from timewreport.interval import TimeWarriorInterval


class TimeWarriorParser(object):
    def __init__(self):
        self.__config = {
            'confirmation': 'off',
            'debug': 'off',
            'verbose': 'off',
        }
        self.__intervals = []

    def parse(self, input_stream):
        self.__parse_configuration_section(input_stream)
        self.__parse_intervals_section(input_stream)

    def __parse_configuration_section(self, input_stream):
        config = {}

        for line in input_stream:
            if line == u'\x0A':
                break

            m = re.search('^([^:]+): (.*)$', line, re.MULTILINE)
            config[m.group(1)] = m.group(2)

        self.__config = TimeWarriorConfig(config)

    def __parse_intervals_section(self, input_stream):
        json_string = ''

        for line in input_stream:
            json_string += line

        intervals = json.loads(json_string)

        for interval in intervals:
            self.__intervals.append(TimeWarriorInterval(interval['start'], interval['end'], interval['tags']))

    def get_config(self):
        return self.__config

    def get_intervals(self):
        return self.__intervals
