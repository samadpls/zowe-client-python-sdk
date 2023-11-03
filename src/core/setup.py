import sys

from setuptools import find_namespace_packages, setup

sys.path.insert(0, "..")
from _version import __version__
from setup import resolve_sdk_dep

setup(
    name="zowe_core_for_zowe_sdk",
    version=__version__,
    description="Zowe Python SDK - Core package",
    url="https://github.com/zowe/zowe-client-python-sdk",
    author="Guilherme Cartier",
    author_email="gcartier94@gmail.com",
    license="EPL-2.0",
    classifiers=[
        "Programming Language :: Python :: 3",
        "Programming Language :: Python :: 3.7",
        "License :: OSI Approved :: Eclipse Public License 2.0 (EPL-2.0)",
    ],
    install_requires=[
        "commentjson",
        "deepmerge",
        "jsonschema",
        "pyyaml",
        "requests",
        "urllib3",
    ],
    extras_require={
        "secrets": [resolve_sdk_dep("secrets", "~=0.1.0")]
    },
    packages=find_namespace_packages(include=["zowe.*"]),
)
