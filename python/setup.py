#!/usr/bin/env python

from setuptools import setup
import webim

setup(name="python-webim",
  version=webim.__version__,
  description="Python WebIM Client",
  long_description=open("README").read(),
  author="Ery Lee",
  author_email="ery.lee@gmail.com",
  maintainer="Ery Lee",
  maintainer_email="ery.lee@gmail.com",
  url="http://www.webim20.cn",
  download_url="http://www.github/webim/webim-api/",
  py_modules=["webim"],
  classifiers=[
    "Development Status :: 1 - Beta/Unstable",
    "Intended Audience :: Developers",
    "License :: OSI Approved :: Python Software Foundation License",
    "Operating System :: OS Independent",
    "Programming Language :: Python",
    "Topic :: Internet",
    "Topic :: Software Development :: Libraries :: Python Modules",
    ])
