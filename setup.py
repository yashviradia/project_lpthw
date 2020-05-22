try:
    from setuptools import setup 
except ImportError:
    from distutils.core import setup 

config = {
    'description': 'ex47',
    'author': 'Hallo',
    'url': 'www.ex47.com',
    'download_url': 'www.ex47.com/download',
    'author_email': 'ex47@projects.com',
    'version': '0.1',
    'install_requires': ['nose'],
    'packages': ['ex47'],
    'scripts': [],
    'name': 'ex47'
}

setup(**config)

