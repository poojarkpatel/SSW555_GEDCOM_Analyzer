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
    warnings = []
    for value in individual.values():
        birth_date = value._birth_date
        if value._birth_date != "NA":
            if birth_date.strftime("%Y") <= datetime.datetime.today().strftime("%Y"):
                delta: datetime = datetime.datetime.today() + timedelta(days=30)
                if delta.strftime("%m %d") >= birth_date.strftime("%m %d") \
                        >= datetime.datetime.today().strftime("%m %d"):
                    warnings.append(
                     f'Line number {value._line_numbers["date"]["birth"]}, '
                     f'{value._name} has upcoming birthday')

    return warnings