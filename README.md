# instasize-automation

# To run the tests make sure to:

install Appium using the instructions on http://appium.io/.  

Install android sdk tools from https://developer.android.com/studio/index.html. You don't need android studio, just the 
command line tools located at the bottom of the webpage.  

Make sure your capabilities in the DriverBuilder7zero.py file are set correctly for the device you are testing on.

Python must be installed are your system.  You can install it with homebrew: brew install python.

Install the nose2 plugig: pip install nose2

Add this to your bash_profile: export PYTHONPATH=$PYTHONPATH:path/to/testInstasizeAutomation.  This allows the test scripts to be stored in their own folder and still be able to import all of the modules.

To run the tests run appium and type into terminal: nose2 -v -s /path/to/test/scripts
