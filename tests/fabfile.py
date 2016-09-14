import os

from fabric.api import *
from config.base_config import BaseConfig

config_path = "tests/config/common.properties"
tests_path = "tests/opportunity/test_opportunity.py"


@task()
def run_tests_in_firefox():
    set_browser_type("firefox")
    os.system('pytest {0}'.format(tests_path))

# @task()
# def run_tests_in_chrome():
#     set_browser_type("chrome")
#     os.system('pytest {0}/{1}/{2}'.format(current_dir, project_parent_dir, tests_path))
#
# @task()
# def run_tests_in_parallel_in_chrome(thread_count):
#     set_browser_type("chrome")
#     print("Started execution in {0} parallel threads".format(thread_count))
#     os.system('pytest -n {0} {1}/{2}/{3}'.format(thread_count, current_dir, project_parent_dir, tests_path))
#
# @task()
# def run_tests_in_parallel_in_firefox(thread_count):
#     set_browser_type("firefox")
#     print("Started execution in {0} parallel threads".format(thread_count))
#     os.system('pytest -n {0} {1}/{2}/{3}'.format(thread_count, current_dir, project_parent_dir, tests_path))


def set_browser_type(browser):
    config = BaseConfig().read_config(config_path)
    config.set("WEBDRIVER", "browser", browser)
    with open(config_path, 'w') as configfile:
        config.write(configfile)