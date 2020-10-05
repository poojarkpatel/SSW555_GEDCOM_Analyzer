import datetime

def us_25(individual,family):
    warnings = []
    for family in family.values():
        names = []
        birth_dates = []
        if family._children != "NA":
            for child in family._children:
                if individual[child]._name in names:
                    warnings.append(f"The family {family._family} has multiple individuals with same name {individual[child]._name}")
                names.append(individual[child]._name)
                if individual[child]._birth in birth_dates:
                    warnings.append(f"There are multiple people born on {individual[child]._birth} date in family {family._family}")
                birth_dates.append(individual[child]._birth)

    return warnings











