"""
This file
"""
from typing import List


def us_25(individual, family_id):
    """ this function returns name, birthdate, family id of multiple people born on same day and
    multiple people with same name
    """
    warnings: List = []
    for family in family_id.values():
        birth_dates_names = []
        if family.children != "NA":
            for child in family.children:
                if individual[child].name in birth_dates_names:
                    warnings.append(f"The family {family.family} has multiple individuals "
                                    f"with same name {individual[child].name}")
                if individual[child].birth in birth_dates_names:
                    warnings.append(f"There are multiple people born on {individual[child].birth} "
                                    f"date in family {family.family}")
                birth_dates_names.extend([individual[child].birth, individual[child].name])
    return warnings
