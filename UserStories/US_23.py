def US_23(individual_object):
    """ Function that checks if multiple individuals with same name and birth date occur in the file """
    result = dict()
    individuals = dict()

    for individual in individual_object.values():
        individual_name = individual.get_name()
        individual_birth_date = individual._birth_date

        if individual_name in individuals:
            if individuals[individual_name] == individual_birth_date:
                result[individual_name] = individual_birth_date

        individuals[individual_name] = individual_birth_date

    return result
