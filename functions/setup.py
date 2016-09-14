from setuptools import setup, find_packages
from setuptools.command.install import install as _install
import os

# Post-install engine configuration
def _post_install(dir):

    is_cmd_running = os.system('toilet -f bigmono9 -F gay Functions Installed -t')
    if is_cmd_running !=0:
       print (
           "\n\n\n************************************\n\n\n"
           "Functions Installed!\n"
           "You can now use them after 'import <name>'"
           "\n\n\n************************************\n\n\n"
       )


class install(_install):
    def run(self):
        _install.run(self)
        self.execute(
            _post_install, (self.install_lib,),
            msg="\nRunning post install tasks...")


# Normal setup stuff
setup(name='name',
      version='0.1',
      description='Functions used by the tests',
      author='JD',
      author_email='jaydeepc@thuoghtworks.com',
      packages=['name'],
      cmdclass={'install': install},
      zip_safe=False)