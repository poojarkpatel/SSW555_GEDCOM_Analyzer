def US_12(individual, family):
    ''' Difference in Mother's age and Son's age should be Less than 60
    Difference in Father's age and Son's age should be Less than 80 '''
    warnings = []
    for k, v in family.items():
        if v._husband_id != 'NA' and v._wife_id != 'NA':
            husband_age = individual[v._husband_id]._age
            wife_age = individual[v._wife_id]._age
            if v._children:
                if v._children!='NA':

                    for child in [individual[c] for c in v._children]:

                        if husband_age - child._age >=80:
                            output = f"US_12: {individual[v._husband_id]._name} with {v._husband_id} is 80 years or older than {child._name} id:{v._children} in line number {family[k].get_line_numbers()['family_id']} "

                            warnings.append(output)

                        if wife_age - child._age >= 60:
                            output = f"US_12: {individual[v._wife_id]._name} with {v._wife_id} is 60 years or older than {child._name} id:{v._children} in line number {family[k].get_line_numbers()['family_id']} "

                            warnings.append(output)

    return warnings

