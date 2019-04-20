"""
setup.py is the build script for setuptools. It tells setuptools about your
package (such as the name and version) as well as which code files to include.

"""

import setuptools

with open("README.md", "r") as fh:
    long_description = fh.read()

setuptools.setup(
    name="example-pkg-mas16",
    version="0.0.1",
    author="matt stetz",
    author_email="mattstetzdata@gmail.com",
    description="A small example package",
    long_description=long_description,
    long_description_content_type="text/markdown",
    url="https://github.com/mas16/packaging_tutorial",
    packages=setuptools.find_packages(),
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ],
)