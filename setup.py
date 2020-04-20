import setuptools

with open("README.md", "r") as fh:
    des = fh.read()

setuptools.setup(
    name="keydb",
    version="0.0.1",
    author="Example Author",
    author_email="kimnt93@gmail.com",
    description="A Python client for KeyDB",
    long_description=des,
    long_description_content_type="text/markdown",
    url="https://github.com/dpsnewailab/keydb-python",
    packages=setuptools.find_packages(),
    classifiers=[
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
        "Programming Language :: Python",
        "Programming Language :: Python :: 2",
        "Programming Language :: Python :: 2.7",
        "Programming Language :: Python :: 3",
        "Programming Language :: Python :: 3.5",
        "Programming Language :: Python :: 3.6",
        "Programming Language :: Python :: 3.7",
        "Programming Language :: Python :: 3.8"
    ],
    python_requires='>=2.7, !=3.0.*, !=3.1.*, !=3.2.*, !=3.3.*, !=3.4.*',
    install_requires=[
        'redis'
    ]
)
