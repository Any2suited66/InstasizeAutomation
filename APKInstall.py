import subprocess
from time import sleep
import os

from path import Path


def installAPK():
    """This method finds an apk file in a path set in your bash_profile and returns it in the driverbuilder method
    for appium testing.  The driverbuilder method will install ANY apk file in this folder so make sure it is the
    correct apk file.  Also, make sure there is only one apk file in this folder as this method will install all apk files
    to the test device."""

    # Edit this path to your dedicated Instasize APK folder
    d = Path(os.environ['IS_ANDROID_APK_PATH'])
    output = d.files('*.apk')
    listed = ''.join(str(e) for e in output)
    return listed

