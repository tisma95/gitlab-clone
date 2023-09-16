#################################################################
#               Author: Ismael Maurice                          #
#               Language: Python                                #
#               Projet: Gitlab Clone                            #
#               Version: V1                                     #
#               File: helpers.py                                #
#################################################################

"""
    The helper functions which will be used inside the main file.
"""

def getSecondsConvertion(seconds):
    """
        Name
        ----
        getSecondsConvertion

        Description
        -----------
        Return the conversion of seconds to years, months, days, hours, minutes and seconds

        Parameters
        ----------
        :param seconds (required number): the number of seconds which will be converted.

        Response
        --------
        :return string

        Examples
        -------
        getSecondsConvertion(10000) => Return '0 year(s) and 0 month(s) and 0 day(s) and 2 hour(s) and 46 minute(s) and 40 second(s)'
        getSecondsConvertion(100000000) => Return '3 year(s) and 2 month(s) and 17 day(s) and 9 hour(s) and 46 minute(s) and 40 second(s)'
    """
    functionName = "getSecondsConvertion"
    import logging

    # Verify the parameter
    if seconds < 0:
        message = f"\n{functionName}::The parameter 'seconds' must be a positive number\n"
        logMessage(message=message, logType="error")
        exit(0)

    # Defines constantes
    oneMinuteSeconds = 60 #=> 1 minute = 60 seconds
    oneHourMinutes = 60 #=> 1 hour = 60 minutes
    oneDayHours = 24 #=> 1 day = 24 hours
    oneMonthDays = 30 #=> 1 month = 30 days generally
    oneYearMonths = 12 #=> 1 year = 12 months
    # Get the seconds to user entry
    howManySeconds = seconds
    # Convert to int
    try:
        # Calculate the number of year, month, days, hours, minutes and seconds
        minutes, seconds = howManySeconds // oneMinuteSeconds, howManySeconds % oneMinuteSeconds
        hours, minutes = minutes // oneHourMinutes, minutes % oneHourMinutes
        days, hours = hours // oneDayHours, hours % oneDayHours
        months, days = days // oneMonthDays, days % oneMonthDays
        years, months = months // oneYearMonths, months % oneYearMonths
        return f"{int(years)} year(s) and {int(months)} month(s) and {int(days)} day(s) and {int(hours)} hour(s) and {int(minutes)} minute(s) and {int(seconds)} second(s)"

    except AssertionError:
        message = f"{functionName}::You must give a positive number for second(s) !"
        logMessage(message=message, logType="error")
        exit(0)
    except ValueError:
        message = f"{functionName}::You must give a number for second(s) !"
        logMessage(message=message, logType="error")
        exit(0)
    except:
        message = f"{functionName}::Error has met!"
        logMessage(message=message, logType="error")
        exit(0)

def verificationConfig(config):
    """
        Name
        -----
        verificationCnfig

        Description
        ------------
        Helper function which will verify that the configuration file for dotenv is correct and contains the expected values.

        The function will stop the program if incorrect config file.

        Parameters
        -----------
        :param config(required dict): the dictionary which contains the environment variables.

        Response
        ---------
        None
    """
    functionName = "verificationCnfig"
    try:
        # Define the list of expected .env variable
        expectedKeys = ["DOMAIN", "TOKEN", "FOLDER", "PROTOCOL"]

        # Verify if the contains of env
        if not config or len(config) == 0:
            message = "The .env file is empty or not found"
            logMessage(message=message, logType="error")
            exit(0)
        elif not isinstance(config, dict):
            message = "The .env file is not dictionary"
            logMessage(message=message, logType="error")
            exit(0)
        # Verify that each expected keys are present
        for key in expectedKeys:
            if key not in config:
                message = f"The key/value of {key} is required inside .env"
                logMessage(message=message, logType="error")
                exit(0)
            elif len(config[key]) < 1:
                message = f"The {key} inside .env is empty"
                logMessage(message=message, logType="error")
                exit(0)
    except Exception as err:
        message = f"{functionName}::Unexpected {err}, {type(err)}"
        logMessage(message=message, logType="error")
        exit(0)

def logMessage(message, logType, addSeparator=True):
    """
        Name
        -----
        logMesaage

        Description
        ------------
        Helper function use to display the message in terminal and in log.

        Parameters
        -----------
        :param message(required str): the log message to display.
        :param logType (requied str): the log type between error, warning, info
        :param addSeparator (required boolean): define if for terminal the seperator should be done

        Response
        ---------
        None
    """
    import logging
    # Display the log in terminal
    if addSeparator:
        print(f"\n{message}\n")
    else:
        print(message)
    # Display the log in log file according to message type
    if logType and logType.lower() == "info":
        logging.info(message)
    elif logType and logType.lower() == "error":
        logging.error(message)
    elif logType and logType.lower() == "warning":
        logging.warning(message)