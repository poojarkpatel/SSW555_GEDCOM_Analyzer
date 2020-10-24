"""
File with the User Story US01
Author: Varun Mullins
"""

import datetime


def US_01(individual, family):
    """Function to implement user story US01"""
    today = datetime.datetime.today().date()
    for item in individual.values():
        if item._birth_date != "NA" and item._birth_date > today:
            """Checks for Birthdate of an Individual"""
            yield f"US01: Birthdate \"{item._birth_date}\" for individual id {item._individual_id} is illeagal"
        if item._death_date != "NA" and item._death_date > today:
            """Checks for the date of death of an Individual"""
            yield f"US01: Date of death \"{item._death}\" for individual id {item._individual} is illeagal"
    for item in family.values():
        if item._marriage_date != "NA" and item._marriage_date > today:
            """Checks for the marriage date of a Family"""
            yield f"US01: Marriage date \"{item._married}\" for family id {item._family} is illeagal"
        if item._divorce_date != "NA" and item._divorce_date > today:
            """Checks for the divorce date of a Family"""
            yield f"US01: Divorce date \"{item._divorced}\" for family id {item._family} is illeagal"