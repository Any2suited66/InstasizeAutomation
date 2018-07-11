import subprocess
import os
from pathlib import Path



def delete_old_builds():
    """This will delete all files in the specified folder that are older than 10 minutes.  It is important only one
    apk is present in the folder specified in the method since other methods are dependent on this factor """

    cmd_list = ['find', os.environ["IS_ANDROID_APK_PATH"], '-mmin', '+10', '-type', 'f', '-delete']

    out = subprocess.check_output(cmd_list)
    print(os.environ['IS_ANDROID_APK_PATH'])
    return out


delete_old_builds()