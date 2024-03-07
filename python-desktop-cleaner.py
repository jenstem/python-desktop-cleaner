import os
import json
import shutil
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

        # Create the folder if it does not exist
        if not os.path.exists(folder):
            os.makedirs(folder)


# Loop through the files in the desktop
    for desktop_file in os.listdir(desktop):
        # Get the file extension
        if desktop_file.endswith(f'.{type}'):
            file_path = os.path.join(desktop, desktop_file)
            new_folder = os.path.join(folder, desktop_file)

# Move the files to the appropriate folder based on the parameters
            shutil.move(file_path, new_folder)


# Log the files that were moved



# Add main function



# Call the main function