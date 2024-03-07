import os
import json
import shutil
from datetime import datetime

# Load the parameters from the config file
def open_config_file():
    with open('config.json', 'r') as jsonfile:
        data = json.load(jsonfile)
        return data.get('parameters', [])

# Arrange files in the desktop based on the parameters
def arrange_files(parameters):
    desktop = os.path.expanduser('~/Desktop')
    logfile = os.path.join('python-desktop-cleaner.log')

    # Create a log or append new entries to the existing log file
    with open(logfile, 'a') as file:
        file.write(f'Start time: {datetime.now()}\n')

    # Loop through the parameters
    for parameter in parameters:
        type = parameter.get('type', '')
        folder = parameter.get('folder', '')
        folder_path = os.path.join(desktop, folder)
        os.makedirs(folder_path, exist_ok=True)

        # Loop through the files in the desktop
        for desktop_file in os.listdir(desktop):
            if desktop_file.endswith(f'.{type}'):
                file_path = os.path.join(desktop, desktop_file)
                new_folder = os.path.join(folder_path, desktop_file)

                shutil.move(file_path, new_folder)

    with open(logfile, 'a') as file:
        file.write(f'End time: {datetime.now()}\n')

def main():
    parameters = open_config_file()
    arrange_files(parameters)

if __name__ == '__main__':
    main()
