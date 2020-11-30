def US_53(individual, family):
    """ This function checks if Husband and wife have the same name """
    warnings = []
    for k, v in family.items():
        if v._husband_id != 'NA' and v._wife_id != 'NA':
            husband_age = individual[v._husband_id]._age
            wife_age = individual[v._wife_id]._age

            if individual[v._husband_id]._name == individual[v._wife_id]._name :

                output = f"US_53: Husband {individual[v._husband_id]._name} with {v._husband_id} has the same name as wife {individual[v._wife_id]._name} with {v._wife_id} in line number {family[k].get_line_numbers()['family_id']} "
                warnings.append(output)

    return warnings
