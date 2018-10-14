#!/usr/bin/env python3
# Author Zuxing Gu
import random
import time

# tm_year=2018, tm_mon=6, tm_mday=6, tm_hour=15, tm_min=29, tm_sec=17, tm_wday=2, tm_yday=157, tm_isdst=0
# Y m d H M S a z A
print(time.localtime())

# strftime() -- convert time tuple to string according to format specification
'''
    %Y  Year with century as a decimal number.
    %m  Month as a decimal number [01,12].
    %d  Day of the month as a decimal number [01,31].
    %H  Hour (24-hour clock) as a decimal number [00,23].
    %M  Minute as a decimal number [00,59].
    %S  Second as a decimal number [00,61].
    %z  Time zone offset from UTC.
    %a  Locale's abbreviated weekday name.
    %A  Locale's full weekday name.
    %b  Locale's abbreviated month name.
    %B  Locale's full month name.
    %c  Locale's appropriate date and time representation.
    %I  Hour (12-hour clock) as a decimal number [01,12].
    %p  Locale's equivalent of either AM or PM.
'''
# 2018 06 06 15 33 29 +0800 Wed Wednesday
print(time.strftime("%Y %m %d %H %M %S %z %a %A"))

# strptime -- Parse a string to a time tuple according to a format specification
'''
    %Y  Year with century as a decimal number.
    %m  Month as a decimal number [01,12].
    %d  Day of the month as a decimal number [01,31].
    %H  Hour (24-hour clock) as a decimal number [00,23].
    %M  Minute as a decimal number [00,59].
    %S  Second as a decimal number [00,61].
    %z  Time zone offset from UTC.
    %a  Locale's abbreviated weekday name.
    %A  Locale's full weekday name.
    %b  Locale's abbreviated month name.
    %B  Locale's full month name.
    %c  Locale's appropriate date and time representation.
    %I  Hour (12-hour clock) as a decimal number [01,12].
    %p  Locale's equivalent of either AM or PM.

'''
curTime = time.strptime("2018:6:7, 15:41:57", "%Y:%m:%d, %H:%M:%S")
print(curTime)

current = random.randrange(0, 100)
print(current)
