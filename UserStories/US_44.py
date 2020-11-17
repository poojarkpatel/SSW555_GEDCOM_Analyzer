def US_44(individual):
    """Death and age should be less than 150 years for individuals"""
    warning = []

    for indi in individual.values():
        if indi._age >= 100:
            warning.append(indi._name)
    return(warning)