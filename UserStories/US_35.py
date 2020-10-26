
"""
US_35 Returns the list of person born in last 30 days
recent births.
"""

import datetime


def US_35(individual):
    """This function returns the name of people
       who were born recently """

    return [f"Line number:{value._line_numbers['date']['birth']} " \
            f" {value.get_name()} has recent birthday" for value in individual.values()
            if value._birth_date != "NA"
            if abs((datetime.datetime.today().date() - value._birth_date).days) <= 30]
