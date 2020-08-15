from setuptools import setup

with open("README.md", "r") as fh:
    long_description = fh.read()

config = {
    'name': 'timew-report',
    'version': '1.3.1',
    'description': 'An interface for TimeWarrior report data',
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
    'install_requires': ['python-dateutil'],
}

setup(**config)
