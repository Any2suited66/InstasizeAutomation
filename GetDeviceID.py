

import subprocess
import os

def getDeviceID():

    adb_ouput = subprocess.check_output(["adb", "devices"])
    str = adb_ouput.decode()
    removeFirst = str.replace('List of devices attached', '')
    device = removeFirst.replace('device', '')

    return device


android_ids = getDeviceID()


def create_list_of_ids():
    device_strings = getDeviceID()
    output = device_strings.split()
    my_ids = output
    print(my_ids)

create_list_of_ids()


