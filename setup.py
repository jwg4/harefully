from setuptools import setup

setup(
    name='harefully',
    version='0.1',
    description='Testing python scripts which require rabbitMQ',
    url='http://github.com/jwg4/harefully',
    author='Jack Grahl',
    author_email='jack.grahl@yahoo.co.uk',
    license='GNU GPL version 2.0',
    packages=['harefully'],
    test_suite='nose.collector',
    tests_require=['nose']
)

