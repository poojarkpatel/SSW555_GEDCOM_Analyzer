"""
File with the User Story US04
Author: Varun Mullins
"""


def us04(family):
    """Function to implement user story US04"""
    for item in family.values():
        if item._divorced != 'NA':
            if item._married > item._divorced:
                """Compares the marriage and the divorce dates"""
                yield f"US04: This family id {item._family} has an illegal dates for marriage and divorce"