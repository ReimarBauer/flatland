import os
import sys

if sys.version_info < (2, 7):
    print("Python 2.7.x is required.")
    sys.exit(1)

try:
    from setuptools import setup, find_packages
    extra_setup = dict(
        include_package_data=True,
        zip_safe=True,
        )
except ImportError:
    from distutils.core import setup
    extra_setup = {}
    def find_packages(exclude=()):
        return [w[0].replace('/', '.')
                for w in os.walk('flatland')
                if '__init__.py' in w[2]]

# note: importing flatland so we can use flatland.__version__ here does
# NOT work at package installation time - it falls over the blinker import.
# thus, until this is fixed, we duplicate the version number here:
version = '0.8'

long_desc = open('README').read()

setup(name="flatland",
      version=version,
      packages=find_packages(exclude=['tests.*', 'tests']),
      author='Jason Kirtland',
      author_email='jek@discorporate.us',
      description='HTML form management and validation',
      keywords='schema validation data web form forms roundtrip',
      long_description=long_desc,
      license='MIT License',
      url='https://github.com/discorporate/flatland/',
      classifiers=['Development Status :: 4 - Beta',
                   'Environment :: Web Environment',
                   'Intended Audience :: Developers',
                   'License :: OSI Approved :: MIT License',
                   'Natural Language :: English',
                   'Operating System :: OS Independent',
                   'Programming Language :: Python',
                   'Programming Language :: Python :: 2.7',
                   'Topic :: Internet :: WWW/HTTP :: WSGI',
                   'Topic :: Software Development :: Libraries'],
      install_requires=[
          'blinker',
          ],
      **extra_setup)
