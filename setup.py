from setuptools import setup
setup(name='chicagolugflask',
      version='1.0',
      description='ChicagoLUG website',
      author='Jim Campbell',
      author_email='jwcampbell@gmail.com',
      install_requires=['flask>=2.2.3', 'misaka>=2.1.1', 'pyyaml>=6.0',
      'gunicorn>=20.1.0','feedwork>=1.1.0','uritools>=4.0.1','werkzeug>=2.2.3',
      'setuptools>=59.6.0'],
     )
