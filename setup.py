from setuptools import setuptools

with open("README.md", "r") as fh:
    long_description = fh.read()

setuptools.setup(
    name='obilisk',
    packages=setuptools.find_packages(),
    description='Symbolic Math Library for Python',
    long_description=long_description,
    long_description_content_type="text/markdown",
    version='1.0',
    url='https://github.com/TheRebelOfBabylon/obilisk',
    author='TheRebelOfBabylon',
    author_email='therebelofbabylon@protonmail.com',
    keywords=['pip','obilisk']
    )

