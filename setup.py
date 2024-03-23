from setuptools import setup

REQUIRES = [
    'allure-pytest',
    'curlify',
    'sqlalchemy',
    'structlog',
    'records'
]

setup(
    name='db_client',
    version='0.0.1',
    packages=['db_client'],
    url='https://github.com/Amarillia31/db_client.git',
    license='MIT',
    author='elena',
    author_email='-',
    install_requires=REQUIRES,
    description='db client'
)
