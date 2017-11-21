
from subprocess import check_output


class GetDeviceID(object):

     def getDeviceID(self):
          adb_ouput = check_output(["adb", "devices"])
          str = adb_ouput.decode()
          removeFirst = str.replace('List of devices attached', '')
          device = removeFirst.replace('device', '')
          return device


