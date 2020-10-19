"""
File with the User Story US04
Author: Varun Mullins
"""


def us04(family):
    """Function to implement user story US04"""
    for item in family.values():
        if item.divorced != 'NA':
            if item.married > item.divorced:
                """Compares the marriage and the divorce dates"""
                yield f"US04: This family id {item.family} has an illegal dates for marriage and divorce"