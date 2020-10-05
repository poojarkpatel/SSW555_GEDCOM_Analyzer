def US_07(individual):
    """Death and age should be less than 150 years for individuals"""
    lst = []

    for v in individual.values():
        if v._age >= 150:
            lst.append(v._name)
    return(lst)