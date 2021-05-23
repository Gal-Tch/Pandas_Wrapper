import setuptools

with open("README.md", "r", encoding="utf-8") as fh:
    long_description = fh.read()
REQUIRED = ['bottle-websocket','pandas', 'numpy', 'eel']
setuptools.setup(
    name="Pandas_Wrapper",
    version="0.0.2",
    author="Alon Shevach, Gal Tchinio, Guy Sudri, Tamir Or.",
    author_email="alon.shevach1@gmail.com",
    description="A wrapper to the pandas package",
    install_requires=REQUIRED,
    long_description=long_description,
    long_description_content_type="text/markdown",
    url="https://github.com/Gal-Tch/Pandas_Wrapper.git",
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: BSD License",
        "Operating System :: OS Independent",
    ],
    py_modules=['Pandas_Wrapper_pcg'],
    package_dir={"": "src"},
    packages=setuptools.find_packages(where="src"),
    python_requires=">=3.8",
)