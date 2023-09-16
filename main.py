#################################################################
#               Author: Ismael Maurice                          #
#               Language: Python                                #
#               Projet: Gitlab Clone                            #
#               Version: V1                                     #
#               File: main.py                                   #
#################################################################

"""
    The main package which will load the env variable to clone the gihub repositories.
"""

# Import the modules
import pyfiglet
import os
from helpers import *
import constants
import logging

# Init the date
import datetime
now = datetime.datetime.now()
displayDate = now.strftime("%Y-%m-%d")
# Configure the logging
if not os.path.exists('logs') or not os.path.isdir('logs'):
    os.makedirs('logs')
logging.basicConfig(filename=f'logs/{displayDate}.log', format='%(levelname)s:%(message)s', filemode='w', level=logging.DEBUG)

# Display the application logo
ASCII_art = pyfiglet.figlet_format(constants.APP_NAME + f'\n{displayDate}', justify="center")
print(ASCII_art)
message = constants.APP_NAME + f' - {now.strftime("%Y-%m-%d")}'
logging.debug(message)

# Init start time
import time
startTime = time.time()

try:
    # Import the env
    pass

except Exception as err:
    message = f"Unexpected {err}, {type(err)}"
    logMessage(message=message, logType="error")

finally:
    # Show analyse time
    endTime = time.time()
    message = f"This programme takes: {getSecondsConvertion(endTime-startTime)}"
    logMessage(message=message, logType="info")