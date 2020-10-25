"""
File with the User Story US04
Author: Varun Mullins
"""


def US_04(family):
    """Function to implement user story US04"""
    for item in family.values():
        if item._divorce_date != 'NA':
            if item._marriage_date > item._divorce_date:
                """Compares the marriage and the divorce dates"""
                yield f"US_04: This family id {item._family_id} has an illegal dates for marriage and divorce"