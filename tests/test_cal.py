#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
 @desc:
 @author: hanxianfeng
 @software: PyCharm  on 2020/9/24
"""
import unittest
from datetime import datetime

from parameterized import parameterized

from workday_duration.utils import duration_days, duration_days2, union, intersection


class BasicTests(unittest.TestCase):
    def test_cal_duration_days(self):
        start_datetime = datetime.strptime('2020-08-01 0:0:0', "%Y-%m-%d %H:%M:%S")
        end_datetime = datetime.strptime('2020-08-02 12:0:0', "%Y-%m-%d %H:%M:%S")
        work_days, total_days = duration_days(start_datetime, end_datetime)  # 区间全部在休息日)
        assert 0 == work_days
        assert total_days == 1.5

    @parameterized.expand(
        [
            # 2020-08-02,03是周六日
            ('2020-08-01 0:0:0', '2020-08-02 12:0:0', '%Y-%m-%d %H:%M:%S', 0, 1.5),  # 区间全部在休息日
            ('2020-08-01 0:0:0', '2020-08-03 12:0:0', '%Y-%m-%d %H:%M:%S', 0.5, 2.5),  # 区间结束部分在休息日
            ('2020-07-31 12:0:0', '2020-08-02 12:0:0', '%Y-%m-%d %H:%M:%S', 0.5, 2.0),  # 区间开始部分在休息日
            ('2020-07-31 12:0:0', '2020-08-03 12:0:0', '%Y-%m-%d %H:%M:%S', 1, 3),  # 区间包含休息日
            ('2020-08-02 12:0:0', '2020-08-09 12:0:0', '%Y-%m-%d %H:%M:%S', 5, 7),  # 区间在休息日内（左边周六日，右边周六日）
            ('2020-07-31 12:0:0', '2020-08-16 12:0:0', '%Y-%m-%d %H:%M:%S', 10.5, 16),  # 区间跨两个周末
            ('2020-08-01 12:0:0', '2020-08-23 12:0:0', '%Y-%m-%d %H:%M:%S', 15, 22),  # 区间跨多个周末
            ('2020-08-01 12:0:0', '2020-08-31 12:0:0', '%Y-%m-%d %H:%M:%S', 20.5, 30),  # 区间跨多个周末
            ('2020-08-20 17:47:00', '2020-08-21 11:19:56', '%Y-%m-%d %H:%M:%S', 0.7312, 0.7312),
            ('2020-09-03 15:00:00.000000', '2020-09-07 14:00:00.000000', '%Y-%m-%d %H:%M:%S.%f', 1.9583, 3.9583),
            ('2020-09-10 16:08:00', '2020-09-10 16:32:00', '%Y-%m-%d %H:%M:%S', 0.0167, 0.0167),
            ('2020-09-10 23:08:00', '2020-09-12 16:32:00', '%Y-%m-%d %H:%M:%S', 1.0361, 1.725),
            ('2020-09-12 23:00:00', '2020-09-14 12:00:00', '%Y-%m-%d %H:%M:%S', 0.5, 1.5417),
            ('2020-09-06 23:00:00', '2020-09-07 23:00:00', '%Y-%m-%d %H:%M:%S', 0.9583, 1),
            ('2020-09-30 23:00:00', "2020-10-08 0:0:0", '%Y-%m-%d %H:%M:%S', 0.0417, 7.0417),
            ('2020-09-30 23:00:00', "2020-10-09 0:0:0", '%Y-%m-%d %H:%M:%S', 0.0417, 8.0417),
            ('2020-09-30 23:00:00', "2020-10-09 11:0:0", '%Y-%m-%d %H:%M:%S', 0.5, 8.5),
            ('2020-09-30 23:00:00', "2020-10-10 11:0:0", '%Y-%m-%d %H:%M:%S', 1.5, 9.5),
            ('2020-10-01 23:00:00', "2020-10-10 12:0:0", '%Y-%m-%d %H:%M:%S', 1.5, 8.5417),
            ('2020-10-01 23:00:00', "2020-10-11 12:0:0", '%Y-%m-%d %H:%M:%S', 2, 9.5417),
            # 带时区的时间
            ('2020-08-24 04:00:00 +0000', '2020-08-30 04:00:00 +0000', '%Y-%m-%d %H:%M:%S %z', 4.5, 6),
            # 带时区且转为北京时间后属于节假日
            ('2020-09-30 16:00:00 +0000', '2020-10-02 04:00:00 +0000', '%Y-%m-%d %H:%M:%S %z', 0, 1.5),
            ('2020-09-30 16:00:00.000000 +0000', '2020-10-02 04:00:00.000000 +0000', '%Y-%m-%d %H:%M:%S.%f %z', 0, 1.5),

        ])
    def test_cal_duration_days2(self, start_datetime, end_datetime, dt_fmt, expect_wd, expect_total_day):
        work_days, total_days = duration_days2(start_datetime, end_datetime,
                                               dt_fmt=dt_fmt)  # 区间全部在休息日)
        assert expect_wd == work_days
        assert expect_total_day == total_days

    def test_union(self):
        l1 = [(1, 7), (4, 8), (10, 15), (20, 30), (50, 60)]
        l2 = [(3, 6), (8, 11), (15, 20)]
        assert [(1, 30), (50, 60)] == list(union(l1, l2))

    def test_intersection(self):
        l1 = [(1, 7), (4, 8), (10, 15), (20, 30), (50, 60)]
        l2 = [(3, 6), (8, 11), (15, 20)]
        assert list(intersection(l1, l2)) == [(3, 6), (10, 11)]

    def test_intersection2(self):
        l1 = [(datetime(2020, 11, 25, 1, 1, 1), datetime(2020, 11, 25, 10, 1, 1)), ]
        l2 = [(datetime(2020, 11, 25, 2, 1, 1), datetime(2020, 11, 25, 8, 1, 1)), ]
        assert list(intersection(l1, l2)) == l2
