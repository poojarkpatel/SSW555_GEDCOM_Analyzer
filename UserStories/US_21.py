"""
Author: Priyankaben Shyiani
SSW 555 Agile Methods for Software Development
Purpose: user story 21
"""
def US_21(individual, family):
    """US_21: checks the correct gender of husband and wife"""
    warnings = list()
    for family in family.values():
        if family._marriage_date != 'NA':
            if family._husband_id != 'NA':
                if individual[family._husband_id]._gender != 'NA':
                    if individual[family._husband_id]._gender != 'M':
                        warnings.append(f'US_21: {individual[family._husband_id]._name} gender is supposed to be male but is not on line number {individual[family._husband_id]._line_numbers["gender"]}')

            if family._wife_id != 'NA':
                if individual[family._wife_id]._gender != 'NA':
                    if individual[family._wife_id]._gender != 'F':
                        warnings.append(f'US_21: {individual[family._wife_id]._name} gender is supposed to be female but is not on line number {individual[family._wife_id]._line_numbers["gender"]}')

    return warnings

