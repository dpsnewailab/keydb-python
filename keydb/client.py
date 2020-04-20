from redis import *


class KeyDB(StrictRedis):

    def __init__(self, **kwargs):
        super(KeyDB, self).__init__(**kwargs)

    def expiremember(self, key, subkey, delay, unit=None):
        """
        Set timeout on a subkey. This feature only available on KeyDB
        https://docs.keydb.dev/docs/commands/#expiremember
        :param key: key added by `SADD key [subkeys]`
        :param subkey: subkey on the set
        :param delay: timeout
        :param unit: `s` or `ms`
        :return: 0 if the timeout was set, otherwise 0
        """
        args = [key, subkey, delay]
        if unit is not None and unit not in ['s', 'ms']:
            raise ValueError("`unit` must be s or ms")

        if unit:
            args.append(unit)

        return self.execute_command('EXPIREMEMBER', *args)

    def expirememberat(self, key, subkey, timestamp):
        """
        Set timeout on a subkey by timestamp instead of seconds
        https://docs.keydb.dev/docs/commands/#expirememberat
        :param key:
        :param subkey:
        :param timestamp:
        :return:
        """
        return self.execute_command('EXPIREMEMBERAT', key, subkey, timestamp)
