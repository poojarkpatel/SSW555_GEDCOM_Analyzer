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
            yield f"Birthdate on Line: {item._line_numbers.get('date').get('birth')}\nUS_01: Birthdate \"{item._birth_date}\" for individual id {item._individual_id} is illeagal"
        if item._death_date != "NA" and item._death_date > today:
            """Checks for the date of death of an Individual"""
            yield f"On Line: {item._line_numbers.get('date').get('death')}\nUS_01: Date of death \"{item._death_date}\" for individual id {item._individual_id} is illeagal"
    for item in family.values():
        if item._marriage_date != "NA" and item._marriage_date > today:
            """Checks for the marriage date of a Family"""
            yield f"On Line: {item._line_numbers.get('date').get('marriage')}\nUS_01: Marriage date \"{item._marriage_date}\" for family id {item._family_id} is illeagal"
        if item._divorce_date != "NA" and item._divorce_date > today:
            """Checks for the divorce date of a Family"""
            yield f"On Line: {item._line_numbers.get('date').get('divorce')}\nUS_01: Divorce date \"{item._divorce_date}\" for family id {item._family_id} is illeagal"