from setuptools import setup, find_packages
from os import path


this_directory = path.abspath(path.dirname(__file__))
with open(path.join(this_directory, 'README.md'), encoding='utf-8') as f:
    long_description = f.read()

about = {}
with open(path.join(this_directory, 'lokalise', '_version.py'), encoding='utf-8') as f:
    exec(f.read(), about)

setup(
    name="python-lokalise-api",
    version=about['__version__'],
    author="Ilya Bodrov-Krukowski",
    author_email="bodrovis@protonmail.com",
    description="Official Python interface for the Lokalise API v2",
    long_description=long_description,
    long_description_content_type="text/markdown",
    url="https://github.com/lokalise/python-lokalise-api",
    keywords='lokalise api client',
    license='MIT',
    packages=find_packages(exclude=['tests*']),
    package_data={
        'lokalise': ['py.typed'],
    },
    package_dir={'lokalise': 'lokalise'},
    platforms=['Any'],
    install_requires=['requests'],
    tests_require=['pytest', 'vcrpy', 'pytest-vcr', 'pytest-cov'],
    classifiers=[
        'Development Status :: 5 - Production/Stable',
        "Intended Audience :: Developers",
        "Topic :: Software Development :: Libraries :: Python Modules",
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: BSD License",
        "Operating System :: OS Independent",
    ],
    python_requires='>=3.6',
)
