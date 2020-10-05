"""
File with the User Story US01
Author: Varun Mullins
"""

import datetime


def us01(individual, family):
    """Function to implement user story US01"""
    today = datetime.datetime.today().date()
    for item in individual.values():
        if item._birth != "NA" and item._birth > today:
            """Checks for Birthdate of an Individual"""
            yield f"US01: Birthdate \"{item._birth}\" for individual id {item._individual} is illeagal"
        if item._death != "NA" and item._death > today:
            """Checks for the date of death of an Individual"""
            yield f"US01: Date of death \"{item._death}\" for individual id {item._individual} is illeagal"
    for item in family.values():
        if item._married != "NA" and item._married > today:
            """Checks for the marriage date of a Family"""
            yield f"US01: Marriage date \"{item._married}\" for family id {item._family} is illeagal"
        if item._divorced != "NA" and item._divorced > today:
            """Checks for the divorce date of a Family"""
            yield f"US01: Divorce date \"{item._divorced}\" for family id {item._family} is illeagal"