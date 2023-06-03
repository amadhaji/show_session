from setuptools import setup, find_packages

with open("requirements.txt") as f:
	install_requires = f.read().strip().split("\n")

# get version from __version__ variable in show_session/__init__.py
from show_session import __version__ as version

setup(
	name="show_session",
	version=version,
	description="Show Default Session in navbar",
	author="almad.alaaa@proton.me",
	author_email="almad.alaaa@proton.me",
	packages=find_packages(),
	zip_safe=False,
	include_package_data=True,
	install_requires=install_requires
)
