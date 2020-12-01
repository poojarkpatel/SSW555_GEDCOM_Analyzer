def US_52(individual):
    """ US52 List Individual Male Names"""
    lst = set()

    for key, value in individual.items():
        if individual[key]._gender == 'M':
            lst.add(individual[key]._name)

    print(lst)
    return lst
