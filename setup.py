import sys
from setuptools import setup, find_packages

requires = [
    'argparse',
    'selenium',
    'seleniumbase'
]

setup(
    name='youploader',
    description=("Automated selenium video uploader for YouTube."),
    version='1.0',
    install_requires=requires,
    packages=find_packages(),
    entry_points={
        'console_scripts': ['youploader=youploader.app:main'],
    },
    long_description=open('README.md').read(),
    keywords=['youtube', 'upload', 'uploader', 'selenium', 'automated']
)
