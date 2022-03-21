#import obspython as obs
import shutil
import time

# consts
KB = 1024
MB = 1024 * KB
GB = 1024 * MB

path = "F:\\test"

while(True):
    time.sleep(3)
    print(round(shutil.disk_usage(path).free/GB, 2))

# https://github.com/upgradeQ/OBS-Studio-Python-Scripting-Cheatsheet-obspython-Examples-of-API#ui