#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
 @desc:
 @author: hanxianfeng
 @software: PyCharm  on 2020/9/24
"""
import setuptools
from setuptools import setup
setup(name='workday-duration',
      version='1.0.1',
      description='calculator duration days from one time to another',
      url='https://github.com/hanxianfeng123/workday-duration',
      author='hanxianfeng123',
      author_email='hanxianfeng123@foxmail.com',
      license='MIT',
      install_requires=['chinesecalendar'],
      packages=setuptools.find_packages(),
      python_requires='>=3.6',
      )