import subprocess
import os
from pathlib import Path



def install_apk_to_all_devices():

    """This method finds an apk file in a path set in your bash_profile and returns it in the driverbuilder method
        for appium testing.  The driverbuilder method will install ANY apk file in this folder so make sure it is the
        correct apk file.  Also, make sure there is only one apk file in this folder as this method will install all apk files
        to the test device."""

    # Edit this path to your dedicated Instasize APK folder
    d = Path(os.environ['IS_ANDROID_APK_PATH'])
    output = list(d.glob('*.apk'))
    listed = ''.join(str(e) for e in output)
    print(listed)

    install_apk = subprocess.check_call(["adb+", "install", "-r", listed])
    return install_apk


install_apk_to_all_devices()

