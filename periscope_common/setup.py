from setuptools import setup, find_packages
from setuptools.command.install import install as _install
import os

# Post-install engine configuration
def _post_install(dir):

    is_cmd_running = os.system('toilet -f bigmono9 -F gay Periscope Functions Installed -t')
    if is_cmd_running !=0:
       print (
           "\n\n\n************************************\n\n\n"
           "Periscope Functions Installed!\n"
           "You can now use them after 'import periscope_common'"
           "\n\n\n************************************\n\n\n"
       )


class install(_install):
    def run(self):
        _install.run(self)
        self.execute(
            _post_install, (self.install_lib,),
            msg="\nRunning post install tasks...")


# Normal setup stuff
setup(name='periscope',
      version='0.1',
      description='The funniest joke in the world',
      author='JD',
      author_email='jaydeepc@thuoghtworks.com',
      packages=['periscope_common'],
      cmdclass={'install': install},
      zip_safe=False)
