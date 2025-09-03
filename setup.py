from setuptools import setup, find_packages
import pathlib

parent_dir = pathlib.Path(__file__).parent.resolve()

with open(parent_dir / 'README.md', 'r') as fh:
    long_description = fh.read()

config = {
    'name': 'timew-report',
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
        'Programming Language :: Python :: 3',
        'Programming Language :: Python :: 3.10',
        'Programming Language :: Python :: 3.11',
        'Programming Language :: Python :: 3.12',
        'Programming Language :: Python :: 3.13',
        'Programming Language :: Python :: 3 :: Only',
    ],
    'keywords': 'timewarrior taskwarrior time-tracking',
    'project_urls': {
        'Bug Reports': 'https://github.com/lauft/timew-report/issues',
        'Source': 'https://github.com/lauft/timew-report',
    },
    'package_dir': {'': 'src'},
    'packages': find_packages(where='src'),
    'include_package_data': True,
    'python_requires': '>3, <4',
    'install_requires': ['python-dateutil', 'deprecation'],
    'extras_require': {
        'test': ['pytest']
    }
}

setup(**config)
