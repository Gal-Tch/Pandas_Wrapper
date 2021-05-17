import setuptools

with open("README.md", "r", encoding="utf-8") as fh:
    long_description = fh.read()
REQUIRED = ['bottle-websocket','pandas', 'numpy', 'eel']
setuptools.setup(
    name="Pandas_Wrapper-Gal-Tch",
    version="0.2.1",
    author="Gal-Tch",
    author_email="author@example.com", #???
    description="A wrapper to the pandas package",
    install_requires=REQUIRED,
    long_description=long_description,
    long_description_content_type="text/markdown",
    url="https://github.com/Gal-Tch/Pandas_Wrapper.git",
    project_urls={
        "Bug Tracker": "https://github.com/pypa/sampleproject/issues",  # TODO: change this maybe
    },
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",  # TODO: choose licence, also update licence file
        "Operating System :: OS Independent",
    ],
    py_modules=['Pandas_Wrapper_pcg'],
    package_dir={"": "src"},
    packages=setuptools.find_packages(where="src"),
    python_requires=">=3.8",  # TODO: make sure its 3.8
)