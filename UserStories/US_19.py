def US_19(individual, family):
    warnings = []

    for individual_id in individual:
        individual_child_in = individual[individual_id]._famC

        if individual_child_in != 'NA':
            for family_id in individual_child_in:
                siblings = family[family_id]._children

                for sibling_id in siblings:
                    if individual_id != sibling_id:
                        # individual_id and sibling_id found
                        individual_spouse_in = individual[individual_id]._famS
                        sibling_spouse_in = individual[sibling_id]._famS

                        individual_children = []
                        sibling_children = []

                        if individual_spouse_in != 'NA':
                            for f_id in individual_spouse_in:
                                individual_children.extend(family[f_id]._children)

                        if sibling_spouse_in != 'NA':
                            for f_id in sibling_spouse_in:
                                sibling_children.extend(family[f_id]._children)

                        for child_one in individual_children:
                            for child_two in sibling_children:
                                for key, value in family.items():
                                    if (value._husband_id == child_one and value._wife_id == child_two) or (value._husband_id == child_two and value._wife_id == child_one):
                                        warnings.append(f'US_19: First cousins {child_one} and {child_two} married on line {family[key]._line_numbers["wife_id"]}')

    return warnings
