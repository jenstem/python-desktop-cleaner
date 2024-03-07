import os
import json
from datetime import datetime

# Load the parameters from the config file
def open_config_file():
    with open('config.json', 'r') as jsonfile:
        data = json.load(jsonfile)
        return data.get('parameters', {})

# Arrange files in the desktop based on the parameters
def arrange_files(parameters):
    #define the path to the desktop
    desktop = os.path.expanduser('C:/Users/username/Desktop')
    # define the path to the log file
    logfile = 'python-desktop-cleaner.log'

    # Create a log or append new entries to the existing log file
    with open(logfile, 'a') as file:
        # Log the start time
        file.write(f'Start time: {datetime.now()}\n')

#     for file in os.listdir('C:/Users/username/Desktop'):


# Loop through the parameters
    for parameter in parameters:
        type = parameter.get('type')
        folder = parameter.get('folder')



# Loop through the files in the desktop



# Move the files to the appropriate folder based on the parameters



# Log the files that were moved



# Add main function



# Call the main function