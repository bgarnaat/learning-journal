import os

from setuptools import setup, find_packages

here = os.path.abspath(os.path.dirname(__file__))
with open(os.path.join(here, 'README.txt')) as f:
    README = f.read()
with open(os.path.join(here, 'CHANGES.txt')) as f:
    CHANGES = f.read()

requires = [
    'pyramid',
    'pyramid_jinja2',
    'pyramid_tm',
    'SQLAlchemy',
    'transaction',
    'zope.sqlalchemy',
    'waitress',
    'psycopg2',
    'passlib',
    'wtforms',
    'markdown',
    ]

tests_require = ['pytest',
                 'pytest-watch',
                 'tox',
                 'webtest']

dev_requires = ['ipython',
                'pyramid-ipython',
                'pyramid_debugtoolbar',
                'coverage']

setup(name='journal',
      version='0.0',
      description='journal',
      long_description=README + '\n\n' + CHANGES,
      classifiers=[
        "Programming Language :: Python",
        "Framework :: Pyramid",
        "Topic :: Internet :: WWW/HTTP",
        "Topic :: Internet :: WWW/HTTP :: WSGI :: Application",
        ],
      author='',
      author_email='',
      url='',
      keywords='web wsgi bfg pylons pyramid',
      packages=find_packages(),
      include_package_data=True,
      zip_safe=False,
      test_suite='journal',
      install_requires=requires,
      extras_require={
        'test': tests_require,
        'dev': dev_requires,
      },
      entry_points="""\
      [paste.app_factory]
      main = journal:main
      [console_scripts]
      initialize_db = journal.scripts.initializedb:main
      load_api = journal.scripts.load_class_api:main
      """,
      )
