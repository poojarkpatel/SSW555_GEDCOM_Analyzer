
"""
US_38 Returns the list upcoming birthdays
recent births.
"""

import datetime
from datetime import timedelta


def US_38(individual):
    """This function returns the name of people
       who were born recently """
    # return [f"Line number:{value._line_numbers['date']['birth']} " \
    #         f" {value.get_name()} has recent birthday" for value in individual.values()
    #         if value._birth_date != "NA"
    #         if abs(datetime.datetime.today().date() - value._birth_date).days() >= 30
    #         ]
    for value in individual.values():
        if value._birth_date != "NA":
            today = datetime.datetime.today().date()
            today_fmt = today.strftime("%m %d")
            birth_date = value._birth_date
            birth_date_fmt = birth_date.strftime("%m %d")
            if birth_date_fmt >= today_fmt:
                print(birth_date_fmt)


