
"""
US_35 Returns the list of person born in last 30 days
recent births.
"""

import datetime

def US_35(individual):
    list_most_recent_birth = list()
    for value in individual.values():
        birth_date = value._birth_date
        # today_temp = datetime.timedelta(days=30)
        if birth_date != "NA":
            today = datetime.datetime.today().date()
            if abs((today - birth_date).days) <= 30:
                list_most_recent_birth.append(f"{value.get_name()} has recent birthday")
    return list_most_recent_birth

