from fabric.api import *
from periscope.common_config.base_config import BaseConfig
import os

config_path = "/Users/jaydeepc/Documents/work/paa_lite/functional_tests_python/periscope/common_config/common.properties"

@task()
def run_tests_in_firefox():
    set_browser_type("firefox")
    os.system('pytest projects/paa_lite/tests/opportunity/test_opportunity.py')

@task()
def run_tests_in_chrome():
    set_browser_type("chrome")
    os.system('pytest projects/paa_lite/tests/opportunity/test_opportunity.py')

@task()
def run_tests_in_parallel_in_chrome(thread_count):
    set_browser_type("chrome")
    print "Started execution in {0} parallel threads".format(thread_count)
    os.system('pytest -n {0} projects/paa_lite/tests/opportunity/test_opportunity.py'.format(thread_count))

@task()
def run_tests_in_parallel_in_firefox(thread_count):
    set_browser_type("firefox")
    print "Started execution in {0} parallel threads".format(thread_count)
    os.system('pytest -n {0} projects/paa_lite/tests/opportunity/test_opportunity.py'.format(thread_count))


def set_browser_type(browser):
    config = BaseConfig().read_config(config_path)
    config.set("WEBDRIVER", "browser", browser)
    with open(config_path, 'wb') as configfile:
        config.write(configfile)