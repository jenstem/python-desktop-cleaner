import os
import json

# Load the parameters from the config file
def open_config_file():
    with open('config.json', 'r') as jsonfile:
        data = json.load(jsonfile)
        return data.get('parameters')

# Arrange files in the desktop based on the parameters
# def arrange_files(parameters):




#     for file in os.listdir('C:/Users/username/Desktop'):



# Create a log or append new entries to the existing log file


# Loop through the parameters



# Loop through the files in the desktop



# Move the files to the appropriate folder based on the parameters



# Log the files that were moved



# Add main function



# Call the main function