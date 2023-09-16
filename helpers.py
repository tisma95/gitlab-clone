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