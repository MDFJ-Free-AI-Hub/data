from setuptools import setup, find_packages

with open("README.md", "r", encoding="utf-8") as fh:
    long_description = fh.read()

setup(
    name="data",
    version="11.0",
    author="Steve",
    author_email="stevenetworkesp267@gmail.com",
    description="This library allows the use of datasets that are in the repository.",
    long_description=long_description,
    long_description_content_type="text/markdown",
    url="https://github.com/mdfjbotss/data",
    packages=find_packages(),
    classifiers=[
        "Programming Language :: Python :: 3",
        "Programming Language :: Python :: 3.8",
        "Programming Language :: Python :: 3.9",
        "Programming Language :: Python :: 3.10",
        "Programming Language :: Python :: 3.11",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ],
    python_requires=">=3.8",
    keywords="data processing analysis validation",
)
