from setuptools import setup, find_packages
from os import path
from lokalise._version import __version__


this_directory = path.abspath(path.dirname(__file__))
with open(path.join(this_directory, 'README.md'), encoding='utf-8') as f:
    long_description = f.read()

setup(
    name="python-lokalise-api",
    version=__version__,
    author="Ilya Bodrov",
    author_email="bodrovis@protonmail.com",
    description="Official Python interface for the Lokalise API v2",
    long_description=long_description,
    long_description_content_type="text/markdown",
    url="https://github.com/lokalise/python-lokalise-api",
    keywords='lokalise api client',
    license='MIT',
    packages=find_packages(where='lokalise'),
    package_dir={'': 'lokalise'},
    platforms=['Any'],
    install_requires=['requests>2,<3'],
    tests_require=['pytest', 'vcrpy', 'pytest-vcr', 'pytest-cov'],
    classifiers=[
        "Intended Audience :: Developers",
        "Topic :: Software Development :: Libraries :: Python Modules",
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: BSD License",
        "Operating System :: OS Independent",
    ],
    python_requires='>=3.6',
)
