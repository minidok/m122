#!/usr/bin/env python3

import psutil
import shutil

def check_disk_usage(disk):
    disk_usage = shutil.disk_usage(disk)
    free_precentage = disk_usage.free / disk_usage.total * 100
    print(free_precentage)
    return free_precentage > 15

def check_cpu_load():
    usage = psutil.cpu_percent(1)
    print(usage)
    return usage < 80

if not check_disk_usage("/") or not check_cpu_load():
    print("Red")
else:
    print("Green")