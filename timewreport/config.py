import re


class TimeWarriorConfig(object):
    def __init__(self, config=None):
        self.__config = config if config is not None else {}

    def update(self, other):
        if isinstance(other, TimeWarriorConfig):
            config = other.get_dict()
        elif isinstance(other, dict):
            config = other
        else:
            raise TypeError()

        self.__config.update(config)

    def get_dict(self):
        return self.__config

    def get_value(self, key, default):
        if key in self.__config:
            return self.__config[key]
        else:
            return default

    def get_boolean(self, key, default):
        value = self.get_value(key, default)

        return True if re.search('^(on|1|yes|y|true)$', '{}'.format(value)) else False

    def get_debug(self):
        return self.get_boolean('debug', False)

    def get_verbose(self):
        return self.get_boolean('verbose', False)

    def get_confirmation(self):
        return self.get_boolean('confirmation', False)
