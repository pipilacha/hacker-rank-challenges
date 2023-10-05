#!/bin/python3

import os
import sys

#
# Complete the 'timeConversion' function below.
#
# The function is expected to return a STRING.
# The function accepts STRING s as parameter.
#

def timeConversion(s):
    # Write your code here
    hour = int(s[0:2])
    am_or_pm = s[-2:]
    if am_or_pm == 'AM':
        time = str(hour) if 9 < hour < 12  else f'0{str(hour)}' if hour < 10 else '00'
    elif am_or_pm == 'PM':
        time = str(hour+12) if hour != 12 else '12'
    time += s[2:-2]
    return time

print(timeConversion('04:59:59AM'))

