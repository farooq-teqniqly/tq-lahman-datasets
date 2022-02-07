import teqniqly
from setuptools import setup, find_packages

install_requires = ["pandas", "requests", "tqdm"]


def long_description():
    with open("README.md", encoding="utf-8") as f:
        return f.read()


PROJECT_URL = "https://github.com/farooq-teqniqly/tq-lahman-datasets"

setup(
    name="tq-lahman-datasets",
    version=teqniqly.__version__,
    description=teqniqly.__doc__.strip(),
    long_description=long_description(),
    long_description_content_type="text/markdown",
    url=PROJECT_URL,
    author=teqniqly.__author__,
    author_email="farooq@teqniqly.com",
    license=teqniqly.__license__,
    packages=find_packages(include=["teqniqly", "teqniqly.*"]),
    python_requires=">=3.9",
    install_requires=install_requires,
    classifiers=[
        "Development Status :: 4 - Alpha",
        "Programming Language :: Python",
        "Programming Language :: Python :: 3 :: Only",
        "Intended Audience :: Developers",
        "License :: OSI Approved :: MIT License",
        "Topic :: Software Development :: Libraries :: Python Modules",
        "Topic :: Database",
    ],
    project_urls={"GitHub": PROJECT_URL},
)