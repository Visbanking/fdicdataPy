from setuptools import setup, find_packages

setup(
    name="fdicdata",
    version="0.1.7",
    description="The fdicdata package provides a set of functions for working with data from the Federal Deposit Insurance Corporation(FDIC), including retrieving financial data for FDIC-insured institutions and accessing the data taxonomy",
    long_description=open("README.md").read(),
    long_description_content_type="text/markdown",
    author="Brian Pillmore, Boray Yildiz, Ugur Dar",
    author_email="brian.pillmore@gmail.com, boray.yldz@gmail.com, ugurdarr@gmail.com", 
    url="https://github.com/Visbanking/fdicdataPy",
    classifiers=[
        "Intended Audience :: Developers",
        "Intended Audience :: Financial and Insurance Industry",
        "Topic :: Software Development :: Libraries :: Python Modules",
        "License :: OSI Approved :: MIT License",
        "Programming Language :: Python :: 3",
        "Operating System :: OS Independent",
    ],
    python_requires=">=3.7",
    install_requires=[
        "pandas",
        "requests",
        "pyyaml",
        "urllib3"
    ],
)