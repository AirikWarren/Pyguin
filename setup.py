import setuptools

with open("README.md", "r", encoding="utf-8") as fh:
    long_description = fh.read()

setuptools.setup(
    name="pyguin",
    version="0.0.1",
    author="Airik Warren",
    author_email="airikwarren@gmail.com",
    description="A minimalistic static site generator intended to be very quick and intuitive to understand and extend",
    long_description=long_description,
    long_description_content_type="text/markdown",
    url="https://github.com/airikWarren/pyguin",
    project_urls={
        "Bug Tracker": "https://github.com/airikWarren/pyguin/issues",
    },
    classifiers=[
        "Programming Language :: Python :: 3", 
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ],
    entry_points={
        'console_scripts': [
            'pyguin = pyguin.pyguin:main',
            ],
    },
    install_requires=['Jinja2', 'click', 'requests'],
    packages=setuptools.find_packages(),
    python_requires=">=3.6",
)
