import os
import subprocess





def subprocess_cmd(command):
    process = subprocess.Popen(command, stdout=subprocess.PIPE, shell=True)
    proc_stdout = process.communicate()[0].decode('utf-8').strip()
    print (proc_stdout)


def getVersion():
    version = subprocess_cmd('adb shell getprop ro.build.version.release')
    return version
    pass











