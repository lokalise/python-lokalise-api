from setuptools import setup, find_packages

with open("README.md", "r") as fh:
    long_description = fh.read()

setuptools.setup(
    name="python-lokalise-api",
    version="0.0.1",
    author="Ilya Bodrov",
    author_email="bodrovis@protonmail.com",
    description="Official Python interface for the Lokalise API v2",
    long_description=long_description,
    long_description_content_type="text/markdown",
    url="https://github.com/lokalise/python-lokalise-api",
    keywords='lokalise api client',
    license='MIT',
    packages=setuptools.find_packages(),
    package_dir={'': 'src'},
    platforms=['Any'],
    install_requires=['requests'],
    tests_require=['pytest'],
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ],
    python_requires='>=3.6',
)
