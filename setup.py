from setuptools import setup, find_packages

with open("requirements.txt") as f:
	install_requires = f.read().strip().split("\n")

# get version from __version__ variable in oa/__init__.py
from oa import __version__ as version

setup(
	name="oa",
	version=version,
	description="OA",
	author="Mizusho",
	author_email="admin@mizusho.cn",
	packages=find_packages(),
	zip_safe=False,
	include_package_data=True,
	install_requires=install_requires
)
