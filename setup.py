from setuptools import setup, find_packages

with open("requirements.txt") as f:
	install_requires = f.read().strip().split("\n")

# get version from __version__ variable in secore/__init__.py
from secore import __version__ as version

setup(
	name="secore",
	version=version,
	description="Software Engineering Core App",
	author="Software Engineering Department",
	author_email="chaow@up.ac.th",
	packages=find_packages(),
	zip_safe=False,
	include_package_data=True,
	install_requires=install_requires
)
