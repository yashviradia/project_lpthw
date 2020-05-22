try:
    from setuptools import setup 
except ImportError:
    from distutils.core import setup 

config = {
    'description': 'My Gothon game on the web.',
    'author': 'Hallo',
    'url': 'http://gothonweb.com/project/',
    'download_url': 'http://gothonweb.com/download/',
    'author_email': 'help@gothonweb.com',
    'version': '0.1',
    'install_requires': ['nose'],
    'packages': ['gothonweb'],
    'scripts': [],
    'name': 'gothonweb'
}

setup(**config)

