def US_18(family_object, individual):
    """ """
    warnings = list()
    for attribute in family_object.values():    
        child = list(attribute.children)
        if child != ['N','A']:    
            for i in range(0, len(child)):          
                for j in range(i + 1, len(child)):
                    person_one_id = child[i] 
                    person_two_id = child[j]

                    for attribute in family_object.values():
                        husband_name = attribute.husband_name
                        wife_name = attribute.wife_name
                        
                        if (individual[person_one_id].name == husband_name and individual[person_two_id].name == wife_name) or (individual[person_one_id].name == wife_name and individual[person_two_id].name == husband_name):
                            warnings.append(f"{person_one_id} and {person_two_id} are siblings and a couple.")

    return warnings




