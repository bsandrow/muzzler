
try:
    from setuptools import setup
except ImportError:
    print "Falling back to distutils. Functionality may be limited."
    from distutils.core import setup

config = {
    'description'  : 'Project Euler utils + solutions',
    'author'       : 'Brandon Sandrowicz',
    'url'          : 'http://github.com/bsandrow/project-euler',
    'author_email' : 'brandon@sandrowicz.org',
    'version'      : 0.1.
    'packages'     : [ 'project-euler' ],
    'name'         : 'project-euler',
    'test_suite'   : '',
}

setup(**config)
