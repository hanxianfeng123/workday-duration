# 两个时间点间实际工作时间（去除周六日、节假日）

[![Package](https://img.shields.io/pypi/v/chinesecalendar.svg)](https://pypi.python.org/pypi/chinesecalendar)
[![Travis](https://img.shields.io/travis/LKI/chinese-calendar.svg)](https://travis-ci.org/LKI/chinese-calendar)
[![License](https://img.shields.io/github/license/LKI/chinese-calendar.svg)](https://github.com/LKI/chinese-calendar/blob/master/LICENSE)
[![README](https://img.shields.io/badge/README-English-brightgreen.svg)](https://github.com/LKI/chinese-calendar/blob/master/README.en.md)

两个时间点间实际工作时间（去除周六日、节假日）。
支持 2004年 至 2020年，包括 2020年 的春节延长。

## 安装

```
pip install workday-duration
```

## 样例

``` python
from datetime import datetime

from workday_duration.utils import duration_days


start_datetime = datetime.strptime('2020-08-01 0:0:0',"%Y-%m-%d %H:%M:%S")
end_datetime = datetime.strptime('2020-08-02 12:0:0', "%Y-%m-%d %H:%M:%S")
work_days, total_days = duration_days(start_datetime, end_datetime)  # 区间全部在休息日)
assert 0 == work_days
assert total_days == 1.5
```