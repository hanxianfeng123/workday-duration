# 两个时间点间实际工作时间（去除周六日、节假日）

[![Package](https://img.shields.io/pypi/v/chinesecalendar.svg)](https://pypi.python.org/pypi/chinesecalendar)
[![Travis](https://img.shields.io/travis/LKI/chinese-calendar.svg)](https://travis-ci.org/LKI/chinese-calendar)
[![License](https://img.shields.io/github/license/LKI/chinese-calendar.svg)](https://github.com/LKI/chinese-calendar/blob/master/LICENSE)
[![README](https://img.shields.io/badge/README-English-brightgreen.svg)](https://github.com/LKI/chinese-calendar/blob/master/README.en.md)

两个时间点间实际工作时间（去除周六日、节假日）。
支持 2004年 至 2021年，包括 2020年 的春节延长。

## 安装

```
pip install workday-duration
```
详细使用示例请参考代码tests中的测试用例

## 样例1：时间段包含周六日 

``` python
from datetime import datetime

from workday_duration.utils import duration_days


start_datetime = datetime.strptime('2020-07-31 12:0:0',"%Y-%m-%d %H:%M:%S")
end_datetime = datetime.strptime('2020-08-03 12:0:0', "%Y-%m-%d %H:%M:%S")
work_days, total_days = duration_days(start_datetime, end_datetime)  # 区间全部在休息日)
assert 1 == work_days, "8月1号，2号是周六日，所以实际工作时间为1天"
assert total_days == 3, "绝对时间间隔为3天"
```
## 样例2：时间区间包含节假日
``` python
from datetime import datetime

from workday_duration.utils import duration_days


start_datetime = datetime.strptime('2020-09-30 12:00:00',"%Y-%m-%d %H:%M:%S")
end_datetime = datetime.strptime('2020-10-02 12:00:00', "%Y-%m-%d %H:%M:%S")
work_days, total_days = duration_days(start_datetime, end_datetime) 
assert 0.5 == work_days, "10.1开始为国庆节，所以实际工作时间只有0.5天"
assert total_days == 2
```
## 样例3：带时区的时间间隔（自动转为北京时间后计算）

``` python

from workday_duration.utils import duration_days2

work_days, total_days = duration_days2('2020-09-30 16:00:00 +0000', '2020-10-02 04:00:00 +0000', '%Y-%m-%d %H:%M:%S %z') 
assert 0 == work_days, "10.1开始为国庆节，所以实际这个区间都在休假"
assert total_days == 1.5
```