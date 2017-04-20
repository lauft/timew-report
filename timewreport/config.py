import re


class TimeWarriorConfig(object):
    def __init__(self, config=None):
        self.__config = config if config is not None else {}

    def get_value(self, key, default):
        if key in self.__config:
            return self.__config[key]
        else:
            return default

    def get_boolean(self, key, default):
        value = self.get_value(key, default)

        return True if re.search('{}'.format(value), "(on|1|yes|y|true)") else False
