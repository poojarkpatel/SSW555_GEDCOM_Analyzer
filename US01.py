"""
File with the User Story US01
Author: Varun Mullins
"""

import datetime


def us01(individual, family):
    """Function to implement user story US01"""
    today = datetime.datetime.today().date()
    for item in individual.values():
        if item.birth != "NA" and item.birth > today:
            """Checks for Birthdate of an Individual"""
            yield f"US01: Birthdate \"{item.birth}\" for individual id {item.individual} is illeagal"
        if item.death != "NA" and item.death > today:
            """Checks for the date of death of an Individual"""
            yield f"US01: Date of death \"{item.death}\" for individual id {item.individual} is illeagal"
    for item in family.values():
        if item.married != "NA" and item.married > today:
            """Checks for the marriage date of a Family"""
            yield f"US01: Marriage date \"{item.married}\" for family id {item.family} is illeagal"
        if item.divorced != "NA" and item.divorced > today:
            """Checks for the divorce date of a Family"""
            yield f"US01: Divorce date \"{item.divorced}\" for family id {item.family} is illeagal"