import ConfigParser
import os


class BaseConfig(object):

    def read_config(self, cfg_file):
        if os.path.isfile(cfg_file):
            config = ConfigParser.ConfigParser()
            config.read(cfg_file)
        else:
            print ("Config file is not found.")
        return config

