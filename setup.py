from setuptools import setup, find_packages

setup(
    name = "condabuildtest",
    version = "1.0",
    keywords = ["codna", "build"],
    description = "conda build",
    long_description = "Provide a test demo for conda build.",

    author = "xys",

    packages = find_packages(),
    include_package_data = True,
    platforms = "any",
    install_requires =[],
    zip_safe=False,
)
