from setuptools import setup

setup(
    name="v2d-cli",
    version="0.0.2",
    description="DUCG: Deep Unicode Confusable Generation - System based on the similarity of the characters unicode by means of Deep Learning. This provides a greater number of variations and a possible update over time",
    author="José Ignacion Escribano & Miguel Hernández & Alfonso Muñoz",
    author_email="douncoge@gmail.com",
    url="https://github.com/jiep/unicode",
    python_requires='>3.5.0',
    install_requires=[
        'tqdm',
        'colorama',
        'python-whois',
        'requests'
    ],
    extras_require={
        'dev': [
            'flake8'
        ]
    },
    entry_points={
        'console_scripts': [
            'v2d = v2d.main:main'
        ]
    })
