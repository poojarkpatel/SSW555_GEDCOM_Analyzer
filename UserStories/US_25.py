from typing import List, Dict

def US_25(individual,familys):
    """ this function returns name, birthdate, family id of multiple people born on same day and
        multiple people with same name
        No more than one child with the same name and birth date should appear in a family
        """
    warnings: List = []
    birth_names: Dict[tuple] = {}
    for family in familys.values():
        if family._children != "NA":
            for child in family._children:
                if (individual[child]._name,individual[child]._birth_date) not in birth_names.keys():
                    birth_names[(individual[child]._name,individual[child]._birth_date)] = [individual[child]._individual_id]
                else:
                    birth_names[(individual[child]._name,individual[child]._birth_date)].append(individual[child]._individual_id)
    for key, value in birth_names.items():
        indi_name_line = []
        indi_date_line = []
        if len(birth_names[key]) > 1:
            for item in value:
                indi_name_line.append(str(individual[item]._line_numbers['individual_name']))
                indi_date_line.append(str(individual[item]._line_numbers['date']['birth']))
            lines_name = ",".join(sorted(indi_name_line))
            lines_birth_date = ",".join(sorted(indi_date_line))
            warnings.append(f"Line number {lines_name} There are multiple individual born with same name: {individual[value[0]]._name} ")
            warnings.append(f"Line number {lines_birth_date} There are multiple individual born on same date: {individual[value[0]]._birth_date}")
    return warnings

"""
    i1's name 61
    i2's name 70
    
    i1's dob 39
    i2's dob 48
    max(all the line numbers)
    
    birthdatesnames = {
    name1: date1,
    name2: date2....
    }
"""










