# instasize-automation

# Requirements:

Install Pycharm IDE (makes everything easier)

Install Appium using the instructions on http://appium.io/

Install android sdk tools from https://developer.android.com/studio/index.html. You don't need android studio, just the 
command line tools located at the bottom of the webpage.  

Python3 must be installed on your system.  You can install it with homebrew: brew install python3

Run in terminal:  pip3 install -r path/to/requirements.txt

Add this path to your bash_profile: export PYTHONPATH=$PYTHONPATH:path/to/testInstasizeAutomation.  This allows the test scripts to be stored in their own folder and still be able to import all of the modules.

Optional: Add appium path to your bash profile so it can be run in terminal just by typing 'appium' otherwise you must run appium by entering path/to/appium then the arguments required for testing.

Optional: Create a folder to put the Instasize apk and add that folder to your bash_profile as: IS_ANDROID_APK_PATH.  Do not put any other files in this folder.
The APKInstall.py script refers to this path in your profile to install the apk and may throw an exception if there are other files in the folder.  This option
is commented out in the desired_capabilities but can be reinstated if desired.

# To create a new test_runner for a new device:
1. Copy the contents of one of the included test runners, does not matter which one
2. Create a new python file and name it test_runner_DeviceName.py
3. Paste the test_runner contents copied in step one
4. Change the UDID, platformVersion, systemPort(just choose a different port than the other devices, cannot be the same as appium port), and the port number for webdriver.Remote(127.0.0.1:(diff port #)/wd/hub, desired_caps)
5. Now the new device is ready for the tests.  Make sure developer options is turned on, as well as usb debugging.

# To run the tests:
Each of these tests is designed to run in parallel with other devices to speed up testing.

Before you run any tests you must start an appium instance for each device you wish to test on and each of these instances will be assigned a port number determined by the driver instance.  If you
have 3 devices you want to test on, there will be 3 seperate terminal windows open with each having an appium instance connected to each device test runner.  This will separate each device and allow
the tests to run in parallel.

In terminal type: appium -p (port # based on the test runner) -U (serial # of device under test)
    -p: this is the port number found in the desired_capabilities under the self.driver = webdriver.Remote(127.0.0.1:(portNumber)/wd/hub)
    -U: this is the serial number of the test device

Example for samsung s6 using test_runner_s6.py:

appium -p 4444 -U 05157df532e5e40e

In terminal: pytest path/to/test/runner

In Pycharm IDE: Go to the test_runner for the device you wish to run the tests on and click the green triangle at the bottom of the script to start the entire test suite or the other green
triangles will run the individual tests which is ideal for debugging in case one of the tests failed.

# To add other filters and elements to tests

In Instasize most of the elements are found by xpath and they can be put into a list and iterated through a base test in the base_tests.py file. The test will finish once all of the list items are tested.

1. Open the common_lists.py file in pycharm or text editor
2. Find the list that applies to the test you want to edit
3. Add the element to the list, usually at the end, by it's xpath

# Integration into Jenkins CI

The jobs folder in this repository is the backup for Jenkins jobs which run the tests in parallel depending on which devices are plugged into the host machine.  Research needs to be done on how to
setup multiple nodes so remote devices can be tested on each node.  Right now, jenkins must be run locally with the devices attached to the desktop running jenkins.

To setup a new device for Jenkins simply look at one of the jenkins jobs created previously and copy the format to the new device job.  The parallel tests job will need to be edited based on the jobs
created to test on different devices.  The current jobs backed up are for specific devices that were attached to my local machine.  The format is very simple and should be easily adapted for use with
other devices.