from setuptools import setup, find_packages

with open("README.md", "r", encoding="utf-8") as fh:
    long_description = fh.read()

with open("requirements.txt", "r", encoding="utf-8") as fh:
    requirements = fh.read().splitlines()

setup(
    name="ruplika",
    version="3.1.2",
    author="Ruplika Team",
    author_email="support@ruplika.com",
    description="A comprehensive Python library for Rubika Bot API - Version 3.1.2",
    long_description=long_description,
    long_description_content_type="text/markdown",
    url="https://github.com/ruplika/ruplika",
    packages=find_packages(),
    classifiers=[
        "Development Status :: 5 - Production/Stable",
        "Intended Audience :: Developers",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
        "Programming Language :: Python :: 3",
        "Programming Language :: Python :: 3.6",
        "Programming Language :: Python :: 3.7",
        "Programming Language :: Python :: 3.8",
        "Programming Language :: Python :: 3.9",
        "Programming Language :: Python :: 3.10",
        "Programming Language :: Python :: 3.11",
        "Topic :: Software Development :: Libraries :: Python Modules",
        "Topic :: Communications :: Chat",
    ],
    python_requires=">=3.6",
    install_requires=requirements,
    keywords="rubika bot api messenger library ruplika",
    project_urls={
        "Documentation": "https://ruplika.github.io/docs",
        "Source": "https://github.com/ruplika/ruplika",
        "Tracker": "https://github.com/ruplika/ruplika/issues",
        "Download": "https://pypi.org/project/ruplika/",
    },
    include_package_data=True,
)