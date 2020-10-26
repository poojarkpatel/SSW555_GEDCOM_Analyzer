warnings = list()

def US_20(family, individual):
    """ To check aunts/uncles do not marry nieces/nephews """
    for individual_id, value in individual.items():
        individual_child_in_family = value._famC   
        
        if individual_child_in_family != 'NA':
            siblings_list = list()
            for family_id in individual_child_in_family:
                siblings_list.extend(family[family_id]._children)

            for sibling_id in siblings_list:
                sibling_spouse_in_family = individual[sibling_id]._famS

                if sibling_spouse_in_family != 'NA':
                    for sibling_family_id in sibling_spouse_in_family:
                            nieces = family[sibling_family_id]._children

                            for niece_id in nieces:
                                for k, v in family.items():
                                    if (v._husband_id == individual_id and v._wife_id == niece_id) or (v._wife_id == individual_id and v._husband_id == niece_id):
                                        warnings.append(f'US_20: Individuals {individual_id} and {niece_id} are uncle/aunt and niece/nephew married on line number {family[k].get_line_numbers()["wife_id"]}')

    return warnings

