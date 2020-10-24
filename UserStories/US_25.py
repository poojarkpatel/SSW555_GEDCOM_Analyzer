def US_25(individual,family):
    warnings = []
    for family in family.values():
        names = []
        birth_dates = []
        if family._children != "NA":
            for child in family._children:
                if individual[child]._name in names:
                    warnings.append(f"The family {family._family_id} has multiple individuals with same name {individual[child]._name}")
                names.append(individual[child]._name)
                if individual[child]._birth_date in birth_dates:
                    warnings.append(f"There are multiple people born on {individual[child]._birth_date} date in family {family._family_id}")
                birth_dates.append(individual[child]._birth_date)

    return warnings











