#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
 @desc:
 @author: hanxianfeng
 @software: PyCharm  on 2020/9/24
"""
import setuptools
from setuptools import setup

import workday_duration

with open('README.md', 'r', encoding='utf-8') as f:
    long_description = f.read()

setup(name='workday-duration',
      version=workday_duration.__version__,
      description='calculator duration days from one time to another',
      long_description=long_description,
      long_description_content_type="text/markdown",
      url='https://github.com/hanxianfeng123/workday-duration',
      author='hanxianfeng123',
      author_email='hanxianfeng123@foxmail.com',
      license='MIT',
      install_requires=['chinesecalendar'],
      packages=setuptools.find_packages(),
      python_requires='>=3.6',
      )
