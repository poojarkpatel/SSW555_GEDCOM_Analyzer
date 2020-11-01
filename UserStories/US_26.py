def us_26(individual,family):
    warnings = []
    for indi in individual:
        family_child = individual[indi]._famC
        #print(family_child)
        if family_child != 'NA':
            for fam_id in family_child:
                #print(fam_id)
                if indi in family[fam_id]._children:
                    warnings.append("Individual in family:" +fam_id+ " is on line number "+ str(family[fam_id].get_line_numbers()["family_id"]))
    return warnings