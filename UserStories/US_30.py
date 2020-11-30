import datetime
def us_30(individual):
    warnings = []
    for indi_id in individual:
        _individual = individual[indi_id]
        if (_individual._is_alive == True and _individual._famS != None):
            warnings.append(f' {_individual._name} is married and alive on line number {_individual.get_line_numbers()["date"]["birth"]}')
    return warnings