def US_23(checklist):
    """ Function that checks if multiple individuals with same name and birth date occur in the file """
    individuals = dict()

    for value in checklist.values():
        name = value[0]
        birth_date = value[2]

        if name in individuals and individuals[name] == birth_date:
            raise ValueError('Individuals with same name and birth date present.')
        else:
            individuals[name] = birth_date
