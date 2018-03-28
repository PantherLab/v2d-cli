from setuptools import setup
import configparser

config = configparser.ConfigParser()
config.read('config')

setup(
    name=config['APPLICATION_INFO']['NAME'],
    version=config['APPLICATION_INFO']['VERSION'],
    packages=[config['APPLICATION_INFO']['NAME']],
    description=config['APPLICATION_INFO']['DESCRIPTION'],
    author=config['APPLICATION_INFO']['AUTHOR'],
    author_email=config['APPLICATION_INFO']['AUTHOR_EMAIL'],
    url=config['APPLICATION_INFO']['URL'],
    python_requires='>3.5.0',
    install_requires=[
        'tqdm',
        'colorama'
    ],
    extras_require={
        'dev': [
            'flake8'
        ]
    },
    entry_points={
        'console_scripts': [
            'unicode = unicode.main:main'
        ]
    })
