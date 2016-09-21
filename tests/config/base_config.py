import configparser
import os


class BaseConfig(object):

    def read_config(self, cfg_file):
        if os.path.isfile(cfg_file):
            config = configparser.ConfigParser()
            config.read(cfg_file)
        else:
            raise Exception("Config file is not found.")
        return config

