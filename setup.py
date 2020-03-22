import setuptools

with open("README.md", "r") as fh:
    long_description = fh.read()

setuptools.setup(
    name="klp",  # Replace with your own username
    version=attr: build.__version__.VERSION
    author="crhuber",
    author_email="crhuber@example.com",
    description="python replacement for homebrew",
    long_description=long_description,
    long_description_content_type="text/markdown",
    url="https://github.com/crhuber/kelp",
    packages=setuptools.find_packages(),
    include_package_data=True,
    install_requires=[
        'requests==2.22.0',
        'Click==7.0',
        'filetype==1.0.5'
    ],
    entry_points='''
        [console_scripts]
        kelp=kelp.kelp:cli
    ''',
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ],
    python_requires='>=3.6',
)
