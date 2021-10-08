from setuptools import setup
from setuptools import find_packages


def read_requirements():
    # remember to pipenv lock -r > requirements.txt
    with open('requirements.txt') as req:
        content = req.read().split('\n')

    return content


setup(
    name='pkg',
    version='1.0',
    author='aron-hd',
    description='My template for building command line packages with pytest, module logging and ci-cd actions workflow.',
    packages=find_packages(),
    include_package_data=True,
    install_requires=read_requirements(),
    entry_points='''
        [console_scripts]
        pkg=pkg.cli:cli
    '''
)
