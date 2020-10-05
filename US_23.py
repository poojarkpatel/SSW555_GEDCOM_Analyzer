def US_23(individual_object):
    """ Function that checks if multiple individuals with same name and birth date occur in the file """
    result = list()
    individuals = dict()

    for individual in individual_object:
        individual_name = individual.get_name()
        individual_birth_date = individual._birth

        if individual_name in individuals and individuals[individual_name] == individual_birth_date:
            result.append(f'US_23: Multiple individuals with name {individual_name} born on {individual_birth_date} present.')
        else:
            individuals[individual_name] = individual_birth_date

    return result
