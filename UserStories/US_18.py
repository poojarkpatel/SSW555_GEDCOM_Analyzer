def US_18(family_object, individual):
    """ Siblings should not marry one another """
    warnings = list()
    for attribute in family_object.values():    
        child = list(attribute._children)
        if child != ['N','A']:    
            for i in range(0, len(child)):          
                for j in range(i + 1, len(child)):
                    person_one_id = child[i] 
                    person_two_id = child[j]

                    for attribute in family_object.values():
                        husband_name = attribute._husband_name
                        wife_name = attribute._wife_name

                        if (individual[person_one_id]._name == husband_name and individual[person_two_id]._name == wife_name) or (individual[person_one_id]._name == wife_name and individual[person_two_id]._name == husband_name):
                            array = [person_one_id, person_two_id]
                            sorted(array)
                            warnings.append(f"{array[0]} and {array[1]} are siblings and a couple. Line number: {attribute.get_line_numbers()['wife_id']}")

    return warnings




