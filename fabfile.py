from fabric.api import *
from periscope.config.base_config import BaseConfig
import os

project_parent_dir = "periscope"
current_dir = os.getcwd()
config_path = "{0}/{1}/common_config/common.properties".format(current_dir, project_parent_dir)


@task()
def run_tests_in_firefox():
    set_browser_type("firefox")
    os.system('pytest {0}/{1}/projects/paa_lite/tests/opportunity/test_opportunity.py'.format(current_dir, project_parent_dir))

@task()
def run_tests_in_chrome():
    set_browser_type("chrome")
    os.system('pytest {0}/{1}/projects/paa_lite/tests/opportunity/test_opportunity.py'.format(current_dir, project_parent_dir))

@task()
def run_tests_in_parallel_in_chrome(thread_count):
    set_browser_type("chrome")
    print("Started execution in {0} parallel threads".format(thread_count))
    os.system('pytest -n {0} {1}/{2}/projects/paa_lite/tests/opportunity/test_opportunity.py'.format(thread_count, current_dir, project_parent_dir))

@task()
def run_tests_in_parallel_in_firefox(thread_count):
    set_browser_type("firefox")
    print("Started execution in {0} parallel threads".format(thread_count))
    os.system('pytest -n {0} {1}/{2}/projects/paa_lite/tests/opportunity/test_opportunity.py'.format(thread_count, current_dir, project_parent_dir))


def set_browser_type(browser):
    config = BaseConfig().read_config(config_path)
    config.set("WEBDRIVER", "browser", browser)
    with open(config_path, 'w') as configfile:
        config.write(configfile)