from setuptools import setup

config = {
    'name': 'timew-report',
    'version': '0.0.0',
    'description': 'An interface for TimeWarrior report data',
    'author': 'Thomas Lauf',
    'author_email': 'Thomas.Lauf@tngtech.com',
    'license': 'MIT License',
    'classifiers': [
        'Development Status :: 3 - Alpha',
        'Intended Audience :: Developers',
        'Topic :: Utilities',
        'License :: OSI Approved :: MIT License',
        'Programming Language :: Python :: 2.7',
        'Programming Language :: Python :: 3.4',
    ],
    'keywords': 'timewarrior taskwarrior time-tracking',
    'packages': ['timewreport'],
    'install_requires': ['python-dateutil'],
}

setup(**config)
