from setuptools import setup, find_packages

with open("README.md", "r") as readme_file:
    readme = readme_file.read()

requirements = []#["ipython>=6", "nbformat>=4", "nbconvert>=5", "requests>=2"]

setup(
    name="repositoryTutorial3",
    version="0.1.0",
    author="T d g",
    author_email="tdg@hotmail.com",
    description="A package to convert your Jupyter Notebook",
    long_description=readme,
    long_description_content_type="text/markdown",
    url="https://github.com/organizationNameTutorial3/repositoryTutorial3",
    packages=find_packages(),
    install_requires=requirements,
    classifiers=[
        "Programming Language :: Python :: 3.8",
        "License :: OSI Approved :: GNU General Public License v3 (GPLv3)",
    ],
)
