#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
 @desc:
 @author: hanxianfeng
 @software: PyCharm  on 2020/9/24
"""
import unittest
from datetime import datetime

from workday_duration.utils import duration_days


class BasicTests(unittest.TestCase):
    def test_cal_duration_days(self):
        start_datetime = datetime.strptime('2020-08-01 0:0:0',"%Y-%m-%d %H:%M:%S")
        end_datetime = datetime.strptime('2020-08-02 12:0:0', "%Y-%m-%d %H:%M:%S")
        work_days, total_days = duration_days(start_datetime, end_datetime)  # 区间全部在休息日)
        assert 0 == work_days
        assert total_days == 1.5
