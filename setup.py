import os

from setuptools import setup

here = os.path.abspath(os.path.dirname(__file__))
with open(os.path.join(here, 'README.txt')) as f:
    README = f.read()

requires = [
    'pyramid',
    'pyramid_jinja2',
    'pyramid_tm',
    'SQLAlchemy',
    'transaction',
    'zope.sqlalchemy',
    'waitress',
    'bcrypt',
    'deform',
]

setup(name='sad',
      install_requires=requires,
      version='0.0',
      description='sad',
      long_description=README,
      classifiers=[
        "Programming Language :: Python",
        "Framework :: Pyramid",
        "Topic :: Internet :: WWW/HTTP",
        "Topic :: Internet :: WWW/HTTP :: WSGI :: Application",
        ],
      author='qwe',
      author_email='',
      url='',
      keywords='web wsgi bfg pylons pyramid',
      test_suite='sad',
      entry_points="""\
      [paste.app_factory]
      main = sad:main
      [console_scripts]
      initialize_sads_db = sad.scripts.initDB:main
      """,
)
