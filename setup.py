from gettext import install
from importlib.metadata import entry_points
from setuptools import setup

setup(
    name='hello',
    version='1.0',
    # Telling setuptools that the hello module is a Python module.
    py_modules=['hello'],
    install_requires=[
        'Click',
    ],
  # Telling setuptools that the hello module is a Python module.
    entry_points='''
        [console_scripts]
        hello=hello:cli
    '''    
)