import os
import json
import shutil
from datetime import datetime


def open_config_file():
    """
    Opens the configuration file and retrieves the parameters for file organization.

    Returns:
        list: A list of parameters extracted from the configuration file.
    """
    with open('config.json', 'r') as jsonfile:
        data = json.load(jsonfile)
        return data.get('parameters', [])


def arrange_files(parameters):
    """
    Arranges files on the desktop based on the provided parameters.

    Args:
        parameters (list): A list of dictionaries containing file types and corresponding folder names.
    """
    desktop = os.path.expanduser('~/Desktop')
    logfile = os.path.join('python-desktop-cleaner.log')


    with open(logfile, 'a') as file:
        file.write(f'Start time: {datetime.now()}\n')


    for parameter in parameters:
        type = parameter.get('type', '')
        folder = parameter.get('folder', '')
        folder_path = os.path.join(desktop, folder)
        os.makedirs(folder_path, exist_ok=True)


        for desktop_file in os.listdir(desktop):
            if desktop_file.endswith(f'.{type}'):
                file_path = os.path.join(desktop, desktop_file)
                new_folder = os.path.join(folder_path, desktop_file)

                shutil.move(file_path, new_folder)

    with open(logfile, 'a') as file:
        file.write(f'End time: {datetime.now()}\n')

def main():
    """
    Main function to execute the file arrangement process.
    It retrieves parameters from the configuration file and organizes the desktop files accordingly.
    """
    parameters = open_config_file()
    arrange_files(parameters)

if __name__ == '__main__':
    main()
