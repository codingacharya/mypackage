from setuptools import setup, find_packages

setup(
    name="mypackage",
    version="0.1",
    packages=find_packages(),
    install_requires=[],  # Add dependencies here if needed
    author="thirupathi",
    author_email="kandadithirupathi@chaitanya.edu.in",
    description="A simple Python package to greet and add numbers",
    long_description=open("README.md").read(),
    long_description_content_type="text/markdown",
    url="https://github.com/codingacharya/mypackage",  # Replace with your repo
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ],
    python_requires=">=3.6",
)
