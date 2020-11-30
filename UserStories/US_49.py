def US_49(individual):
    """ Function that lists names that appear more than once in the GEDCOM file. """
    names_seen = set()
    warnings = set()

    for individual_id, individual_details in individual.items():
        if individual_details._name in names_seen:
            warnings.add(individual_details._name)
        else:
            names_seen.add(individual_details._name)

    return warnings
