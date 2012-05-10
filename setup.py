
try:
    from setuptools import setup
except ImportError:
    print "Falling back to distutils. Functionality may be limited."
    from distutils.core import setup

config = {
    'description'  : 'A harness for running Project Euler solutions',
    'author'       : 'Brandon Sandrowicz',
    'url'          : 'http://github.com/bsandrow/muzzler',
    'author_email' : 'brandon@sandrowicz.org',
    'version'      : 0.1.
    'packages'     : [ 'muzzler' ],
    'name'         : 'muzzler',
    'test_suite'   : '',
}

setup(**config)
