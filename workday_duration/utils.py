#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
 @desc:
 @author: hanxianfeng
 @software: PyCharm  on 2020/9/24
"""
import datetime as datetime
from chinese_calendar import get_workdays, get_dates, is_workday


def duration_days(start_datetime: datetime, end_datetime: datetime):
    """
    计算两个datetime间的实际工作日、相对差（不排除周六日、节假日）
    :param start_datetime: 年月日 时分秒
    :param end_datetime:
    :return:
    """

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

#
# def duration_days2(start_date_time, end_date_time, from_tz='Asia/Shanghai'):
#     """
#     计算两个datetime间的工作日、以及相对差（不排除周六日、节假日）
#     :param start_date_time: 年月日 时分秒
#     :param end_date_time:
#     :param from_tz: 日期的时区
#     :return:
#     """
#     to_tz = 'Asia/Shanghai'
#     def tz_datetime(dt, from_tz, to_tz):
#         t = pb.to_datetime(dt)
#         t = t.tz_localize(from_tz) if t.tz is None else t
#         t = t.tz_convert(to_tz)
#         return t
#
#     start_date_time = tz_datetime(start_date_time, from_tz, to_tz)
#     end_date_time = tz_datetime(end_date_time, from_tz, to_tz)
#     import datetime
#     start_dt = datetime.datetime.fromtimestamp(start_date_time.timestamp(), start_date_time.tzinfo)
#     end_dt = datetime.datetime.fromtimestamp(end_date_time.timestamp(), end_date_time.tzinfo)
#
#     return duration_days(start_dt, end_dt)
