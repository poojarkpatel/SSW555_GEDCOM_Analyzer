"""
Author: Priyankaben Shyiani
SSW 555 Agile Methods for Software Development
Purpose: user story 44
"""
def US_44(individual):
    """List alive individuals who are more than 100 years old in a file"""
    warning = []
    for indi in individual.values():
        if indi._age >= 100:
            warning.append(f'{indi._name} is alive and age is more than 100 years old on line number {indi.get_line_numbers()["date"]["birth"]}')
    return warning