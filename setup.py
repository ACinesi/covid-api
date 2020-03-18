import pathlib

import pkg_resources
from setuptools import setup

with pathlib.Path('requirements.txt').open() as requirements_txt:
    install_requires = [
        str(requirement)
        for requirement
        in pkg_resources.parse_requirements(requirements_txt)
    ]

setup(
    name='covid-api',
    version='0.1',
    packages=['commons', 'handlers'],
    url='https://github.com/ACinesi/covid-api',
    license='MIT',
    author='Andrea Cinesi',
    author_email='andrea.cines@hotmail.it',
    description='A set of API to get updated data about COVID in Italy.',
    install_requires=install_requires,
)
