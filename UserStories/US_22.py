"""
Author: Priyankaben Shyiani
SSW 555 Agile Methods for Software Development
Purpose: user story 22
"""
def US_22(individual, family):
    """
    US_22: checks if the individual ids are unique
    """
    i = []
    warning = []

    for item in individual.keys():
        if item in i:
            warning.append(f'US22: {item} id has a duplicate in line number {individual[item]._line_numbers["individual_id"]}')
        else:
              i.append(item)

    for item in family.keys():
        if item in i:
            warning.append(f'US22: {item} id has a duplicate in line number {family[item]._line_numbers["family_id"]}')
        else:
              i.append(item)

    return warning