# instasize-automation

# Requirements:

Install Appium using the instructions on http://appium.io/.  

Install android sdk tools from https://developer.android.com/studio/index.html. You don't need android studio, just the 
command line tools located at the bottom of the webpage.  

Python must be installed on your system.  You can install it with homebrew: brew install python

Install the nose2 plugin: pip install nose2

Install Path module: pip install path.py

Add this path to your bash_profile: export PYTHONPATH=$PYTHONPATH:path/to/testInstasizeAutomation.  This allows the test scripts to be stored in their own folder and still be able to import all of the modules.

Optional: Add appium path to your bash profile so it can be run in terminal just by typing 'appium'

Create a folder to put the Instasize apk and add that folder to your bash_profile as: IS_ANDROID_APK_PATH.  Do not put any other files in this folder.  The APKInstall.py script refers to this path in your profile to install the apk and may throw an exception if there are other files in the folder.

# To run the tests:

In terminal: nose2 -v -s /path/to/testInstasizeAutomation/folder
