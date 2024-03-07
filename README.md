# Python Desktop Cleaner


## Table of Contents
+ [Description](#description)
+ [User Story](#userstory)
+ [Acceptance Criteria](#acceptance)
+ [Installation](#installation)
+ [Usage](#usage)
+ [License](#license)
+ [Video & Screenshots](#screenshots)
+ [Contact Me](#contact)
+ [Notes](#notes)
##

<a id='description'></a>
## Description

As a current grad, I wanted to a create an automatic desktop application with Python.  The app arranges file types into their appropriate corresponding folders on the user's desktop.
##

<a id='userstory'></a>
## User Story

AS A busy worker that is looking for a way to clean up my desktop\
I WANT an app that can quickly arrange files on my desktop into their appropriate folders\
SO THAT I can better focus on the work-at-hand instead of wasting time, cleaning up the desktop
##

<a id='acceptance'></a>
## Acceptance Criteria

GIVEN a Python automated app\
WHEN I follow the usage directions and run the file python-desktop-cleaner through the command line\
THEN I see in a short period of time, all files on my desktop have been put into their corresponding folders\
WHEN I open the PDF folder that was created\
THEN I see only the PDF documents that were on my desktop\
WHEN I open the Spreadsheets folder created\
THEN I see only the spreadsheet files that were on my desktop etc.\
WHEN I open the log file\
THEN I see that the start and end time of the file cleanup\
WHEN I see that all files are in their corresponding folders\
THEN I see the app has stopped running
##

<a id='installation'></a>
## Installation
You will need to install Python 3.0+

Clone the repo:
Use the following command lines:
- git clone https://github.com/jenstem/python-desktop-cleaner.git
- cd python-desktop-cleaner

Install the requirements.txt using command lines:
- pip freeze > requirements.txt
- pip install -r requirements.txt

Install the virtual environment using command line:
- python -m venv venv

Run the virtual environment using command line:
- . venv/bin/activate

Run the app with the following command line:
- python space_invasion.py
##

<a id='usage'></a>
## Usage
You can edit the config file to add/remove file types/folders you need to have cleaned-up on your desktop.
##

<a id='license'></a>
## License:  MIT
##

<a id='screenshots'></a>
## Screenshots/Gifs:

<img src="https://github.com/jenstem/python-desktop-cleaner/blob/main/python-desktop-cleaner-ezgif.com-video-to-gif-converter.gif" width=1000>

<a id='contact'></a>
## Contact Me
GitHub URL:  https://github.com/jenstem

##
<a id='notes'></a>
## Notes:

I received help/code from [Tutswiki](https://tutswiki.com/read-write-json-config-file-in-python/),
[Joeltabe](https://github.com/Joeltabe/Automatic-Desktop-Cleaner/tree/main),
[Python.org](https://docs.python.org/3/library/shutil.html),
[CareerKarma](https://careerkarma.com/blog/python-valueerror-io-operation-on-closed-file/)
