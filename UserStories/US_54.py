def US_54(individual, family):
    """ Child must not be older than parent """
    warnings = []
    for k, v in family.items():
        if v._husband_id != 'NA' and v._wife_id != 'NA':
            husband_age = individual[v._husband_id]._age
            wife_age = individual[v._wife_id]._age
            if v._children:
                if v._children!='NA':

                    for child in [individual[c] for c in v._children]:

                        if husband_age < child._age:
                            output = f"US_54: {individual[v._husband_id]._name} with {v._husband_id} is younger than child {child._name}  in line number {family[k].get_line_numbers()['family_id']} "

                            warnings.append(output)

                        if wife_age < child._age:
                            output = f"US_54: {individual[v._wife_id]._name} with {v._wife_id} is younger than child {child._name} in line number {family[k].get_line_numbers()['family_id']} "

                            warnings.append(output)

    return warnings

