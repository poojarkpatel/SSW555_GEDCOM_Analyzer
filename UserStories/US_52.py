def US_52(individual):
    """ US52 List Individual Male Names"""
    lst = []

    for key, value in individual.items():
        if individual[key]._gender == 'M':
            print("US 52:", individual[key]._name)

