from setuptools import setup, find_packages

from bookpy import __version__


with open("README.md") as f:
    long_description = f.read()

# get the dependencies and installs
with open("requirements.txt") as f:
    install_requires = f.read().split('\n')

setup(
    name='bookpy',
    version=__version__,
    description='A cli tool for rename your e-books.',
    long_description=long_description,
    url='https://github.com/stsewd/bookpy',
    license='MIT',
    packages=find_packages(exclude=['docs', 'tests*']),
    include_package_data=True,
    author='Santos Gallegos',
    install_requires=install_requires,
    author_email='santos_g@outlook.com',
    entry_points={
        'console_scripts': [
            'bookpy=bookpy.cli:bookpy',
        ],
    }
)
