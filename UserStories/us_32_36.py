"""
US_35 Returns the list of person born in last 30 days
recent births.
"""

import datetime
from typing import Dict


def us_36(individual):

    """This function returns the name of people
    who died recently """

    return [f"Line number:{value._line_numbers['date']['death']} {value.get_name()} "\
            f"died recently" for value in individual.values()
            if value._death_date != "NA"
            if abs((datetime.datetime.today().date() - value._death_date).days) <= 30]


def us_32(individuals):
    warnings = []
    birth_dates = dict()
    for individual in individuals:
        if individuals[individual]._birth_date != "NA":
            if str(individuals[individual]._birth_date) not in birth_dates.keys():
                birth_dates[str(individuals[individual]._birth_date)] = [individual]
            else:
                birth_dates[str(individuals[individual]._birth_date)].append(individual)

    for key, value in birth_dates.items():
        if len(birth_dates[key]) >= 2:
            for i in value:
                warnings.append(f"Line number:{individuals[i]._line_numbers['date']['birth']}"
                                f" The two or more individuals were born at the same time "
                                f"{i}:{individuals[i]._name}")
    return warnings