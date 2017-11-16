# web.py==0.38
try:
    from setuptools import setup, find_packages
except ImportError:
    from distutils.core import setup

config = {
    'description': 'Fraud Detector Engine',
    'author': 'Ha Tran',
    'url': '',
    'download_url': 'NA',
    'author_email': 'tranluuha@gmail.com',
    'version': '0.1',
    'install_requires': [
        'urllib'
    ],
    'packages': find_packages(),
    'scripts': [],
    'name': 'fraud_detector'
}

setup(**config)
