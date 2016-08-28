from setuptools import setup, find_packages

from bookpy import __version__


setup(
    name='bookpy',
    version=__version__,
    description='A cli tool for rename your e-books.',
    url='https://github.com/stsewd/bookpy',
    license='MIT',
    packages=find_packages(exclude=['docs', 'tests*']),
    include_package_data=True,
    author='Santos Gallegos',
    install_requires=[
        'isbnlib',
        'isbntools',
        'click',
    ],
    author_email='santos_g@outlook.com',
    entry_points={
        'console_scripts': [
            'bookpy=bookpy.cli:bookpy',
        ],
    }
)
