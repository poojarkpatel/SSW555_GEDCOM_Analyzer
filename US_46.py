def us_46(individual):
    warnings = []
    for indi_id in individual:
        _individual = individual[indi_id]
        if (_individual._is_alive  == False and _individual._famS != None):
            warnings.append(f' {_individual._name} is married and dead on line number {_individual.get_line_numbers()["date"]["birth"]}')
    print(warnings)
    return warnings