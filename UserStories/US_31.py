

def US_31(individuals):
    warnings = []
    for individual in individuals.values():
        if individual._famS == set() and individual._age > 30 and individual._death_date == "NA":\
                warnings.append(f"Line number: {individual._line_numbers['individual_name']} "
                            f"{individual._name}is over 30 and still not married")

        elif individual._famS == "NA" and individual._age > 30 and individual._death_date == "NA":\
                warnings.append(f"Line number: {individual._line_numbers['individual_name']} "
                            f"{individual._name}is over 30 and still not married")
    return warnings