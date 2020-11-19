import datetime
from datetime import timedelta


def US_55(individual):
    warnings = []
    for value in individual.values():
        birth_date = value._birth_date
        death_date = value._death_date
        if value._birth_date != "NA":
            delta: datetime = datetime.datetime.today().date() + timedelta(days=30)
            if birth_date > delta:
                warnings.append(
                        f'Line number {value._line_numbers["date"]["birth"]},'
                        f'{value._name} has illegal birthdate')
        if value._death_date != "NA":
            delta: datetime = datetime.datetime.today().date() + timedelta(days=30)
            if death_date > delta:
                warnings.append(
                    f'Line number {value._line_numbers["date"]["death"]},'
                    f'{value._name} has illegal deathdate')
    return warnings


def US_56(individuals):
    warnings = []
    for individual in individuals.values():
        if individual._famS != "NA" and individual._age < 30 and individual._death_date \
                == "NA":
            warnings.append(f"Line number: {individual._line_numbers['individual_name']} "
                            f"{individual._name}is below 30 and married")

    return warnings