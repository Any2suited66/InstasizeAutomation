# instasize-automation

# Requirements:

install Appium using the instructions on http://appium.io/.  

Install android sdk tools from https://developer.android.com/studio/index.html. You don't need android studio, just the 
command line tools located at the bottom of the webpage.  

Python must be installed on your system.  You can install it with homebrew: brew install python

Install the nose2 plugin: pip install nose2

Add this path to your bash_profile: export PYTHONPATH=$PYTHONPATH:path/to/testInstasizeAutomation.  This allows the test scripts to be stored in their own folder and still be able to import all of the modules.

Optional: Add appium path to your bash profile so it can be run in terminal just by typing 'appium'

# To run the tests:

In terminal: nose2 -v -s /path/to/FilterExportTests
