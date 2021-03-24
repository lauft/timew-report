from setuptools import setup

import timewreport

with open("README.md", "r") as fh:
    long_description = fh.read()

config = {
    'name': 'timew-report',
    'version': timewreport.__version__,
    'description': 'An interface for Timewarrior report data',
    'long_description': long_description,
    'long_description_content_type': 'text/markdown',
    'url': 'https://github.com/lauft/timew-report.git',
    'author': 'Thomas Lauf',
    'author_email': 'Thomas.Lauf@tngtech.com',
    'license': 'MIT License',
    'classifiers': [
        'Development Status :: 5 - Production/Stable',
        'Intended Audience :: Developers',
        'Topic :: Utilities',
        'License :: OSI Approved :: MIT License',
        'Operating System :: OS Independent',
        'Programming Language :: Python :: 3.4',
    ],
    'keywords': 'timewarrior taskwarrior time-tracking',
    'packages': ['timewreport'],
    'install_requires': ['python-dateutil', 'deprecation'],
}

setup(**config)
