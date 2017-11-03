import subprocess
from subprocess import Popen, PIPE, STDOUT
import os

pid = subprocess.Popen(args=[
    "/Applications/Utilities/Terminal.app", "--command=appium"]).pid
print pid






