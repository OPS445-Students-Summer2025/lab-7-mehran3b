#!/usr/bin/env python3
# Student ID: mebrahimi22

class Time:
    def __init__(self, hour=12, minute=0, second=0):
        self.hour = hour
        self.minute = minute
        self.second = second

def format_time(t):
    return f"{t.hour:02d}:{t.minute:02d}:{t.second:02d}"

def valid_time(t):
    return 0 <= t.hour < 24 and 0 <= t.minute < 60 and 0 <= t.second < 60

def time_to_sec(time):
    minutes = time.hour * 60 + time.minute
    seconds = minutes * 60 + time.second
    return seconds

def sec_to_time(seconds):
    time = Time()
    minutes, time.second = divmod(seconds, 60)
    time.hour, time.minute = divmod(minutes, 60)
    return time

def sum_times(t1, t2):
    total_sec = time_to_sec(t1) + time_to_sec(t2)
    return sec_to_time(total_sec)

def change_time(time, seconds):
    total_sec = time_to_sec(time) + seconds
    new_time = sec_to_time(total_sec)
    time.hour = new_time.hour
    time.minute = new_time.minute
    time.second = new_time.second
