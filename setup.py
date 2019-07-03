import pathlib
from setuptools import setup

# The directory containing this file
HERE = pathlib.Path(__file__).parent

# The text of the README file
README = (HERE / "README.md").read_text()

# This call to setup() does all the work
setup(
    name="vizion-composite-key",
    version="1.0.2",
    description="Composite Key for Django >= 2.0",
    long_description=README,
    long_description_content_type="text/markdown",
    url="https://github.com/ubuviz/vizion-composite-key",
    author="Ubuviz",
    author_email="info@ubuviz.com",
    license="MIT",
    classifiers=[
        "License :: OSI Approved :: MIT License",
        "Programming Language :: Python :: 3",
        "Programming Language :: Python :: 3.5",
        "Programming Language :: Python :: 3.6",
        "Programming Language :: Python :: 3.7",
    ],
    include_package_data=True,
    install_requires=["Django>=2.0"],
)
