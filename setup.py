try:
  from setuptools import setup
except ImportError:
  from distutils.core import setup

config = {
  'description': 'My Project',
  'author': 'Justin Knoll',
  'url': '',
  'download_url': '',
  'author_email': 'justin.knoll@gmail.com',
  'version': '0.1',
  'install_requires': ['nose'],
  'packages': ['NAME'],
  'scripts': [],
  'name': 'projectname'
}

setup(**config)
