from setuptools import setup, find_packages

setup(
    name="og-testing",
    version="1.0.0",
    description="Python Hello World project",
    author="",
    author_email="",
    packages=find_packages(where="src"),
    package_dir={"": "src"},
    python_requires=">=3.8",
    install_requires=[],
)
