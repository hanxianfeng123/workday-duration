#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
 @desc:
 @author: hanxianfeng
 @software: PyCharm  on 2020/9/24
"""
import datetime
from itertools import product
from operator import itemgetter
from typing import List

import pytz
from chinese_calendar import get_workdays, get_dates, is_workday


def _tz_convert_to_chinese(dt: datetime):
    chinese_zone = pytz.timezone('Asia/Shanghai')
    dt = chinese_zone.localize(dt) if not dt.tzinfo else dt.astimezone(chinese_zone)
    return dt


def duration_days(start_datetime: datetime.datetime, end_datetime: datetime.datetime):
    """
    计算两个datetime间的实际工作日、相对差（不排除周六日、节假日）
    Note: 目前只支持中国时区，因为按中国节假日计算
    :param start_datetime: 年月日 时分秒
    :param end_datetime:
    :return:
    """
    start_datetime = _tz_convert_to_chinese(start_datetime)
    end_datetime = _tz_convert_to_chinese(end_datetime)

    work_day_num = len(get_workdays(start_datetime, end_datetime))
    total_day_num = len(get_dates(start_datetime, end_datetime))

    free_day_num = total_day_num - work_day_num
    actual_day_len = round((end_datetime - start_datetime).total_seconds() / (24 * 60 * 60), 4)

    if free_day_num == 0:
        return actual_day_len, actual_day_len
    is_start_work = is_workday(start_datetime)
    is_end_work = is_workday(end_datetime)

    cut_diff = 0
    if is_start_work:
        diff = (start_datetime - datetime.datetime(year=start_datetime.year, month=start_datetime.month,
                                                   day=start_datetime.day,
                                                   tzinfo=start_datetime.tzinfo)).total_seconds()
        cut_diff += round(diff / (24 * 60 * 60), 4)
    if is_end_work:
        diff = 24 * 60 * 60 - (end_datetime - datetime.datetime(year=end_datetime.year, month=end_datetime.month,
                                                                day=end_datetime.day,
                                                                tzinfo=end_datetime.tzinfo)).total_seconds()
        cut_diff += round(diff / (24 * 60 * 60), 4)

    wd = round(total_day_num - free_day_num - cut_diff, 4)
    return wd, actual_day_len


def duration_days2(start_date_time: str, end_date_time: str, dt_fmt='%Y-%m-%d %H:%M:%s'):
    """
    计算两个datetime间的工作日、以及相对差（不排除周六日、节假日）
    :param start_date_time: 年月日 时分秒
    :param end_date_time:
    :return:
    """

    start_dt = datetime.datetime.strptime(start_date_time, dt_fmt)
    end_dt = datetime.datetime.strptime(end_date_time, dt_fmt)

    return duration_days(start_dt, end_dt)


def _consolidate(intervals):
    sorted_intervals = sorted(intervals, key=itemgetter(0))

    if not sorted_intervals:  # no intervals to merge
        return

    # low and high represent the bounds of the current run of merges
    low, high = sorted_intervals[0]

    for iv in sorted_intervals[1:]:
        if iv[0] <= high:  # new interval overlaps current run
            high = max(high, iv[1])  # merge with the current run
        else:  # current run is over
            yield low, high  # yield accumulated interval
            low, high = iv  # start new run

    yield low, high  # end the final run


def union(l1: List[datetime.datetime], l2: List[datetime.datetime]):
    """
    时间并集
    :param l1:
    :param l2:
    :return:
    """
    return _consolidate([*l1, *l2])


def intersection(l1: List[datetime.datetime], l2: List[datetime.datetime]):
    """
    时间交集
    :param l1:
    :param l2:
    :return:
    """
    result = ((max(s1, s2), min(e1, e2)) for (s1, e1), (s2, e2) in product(l1, l2) if s1 < e2 and e1 > s2)
    return _consolidate(result)
