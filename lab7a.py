#!/usr/bin/env python3
# Student ID: mebrahimi22
class Time:
    """Simple object type for time of the day.
    data attributes: hour, minute, second
    """
    def __init__(self,hour=12,minute=0,second=0):
        """constructor for time object""" 
        self.hour = hour
        self.minute = minute
        self.second = second

def format_time(t):
    """Return time object (t) as a formatted string"""
    return f'{t.hour:02d}:{t.minute:02d}:{t.second:02d}'

def sum_times(t1, t2):
    """Add two time objests and return the sum."""
    sum = Time()
    sum.hour = t1.hour + t2.hour
    sum.minute = t1.minute + t2.minute
    sum.second = t1.second + t2.second

        # Carry over logic
    while sum.second >= 60:
        sum.second -= 60
        sum.minute += 1
    while sum.minute >= 60:
        sum.minute -= 60
        sum.hour += 1

    return sum

def valid_time(t):
    """check for the validity of the time object attributes:
        24 > hour > 0, 60 > minute > 0, 60 > second > 0 """
    return 0 <= t.hour < 24 and 0 <= t.minute < 60 and 0 <= t.second < 60