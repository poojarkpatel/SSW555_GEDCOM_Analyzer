
"""
US_35 Returns the list of person born in last 30 days
recent births.
"""

import datetime


def recent_births(individual):

    """This function returns the name of people
    who were born recently """

    return [f"{value.get_name()} has recent birthday" for value in individual.values()
            if value.birth != "NA"
            if abs((datetime.datetime.today().date() - value.birth).days) <= 30]
