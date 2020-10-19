def US_06(individual,family):
    """ US06 : Divorce of the husband or wife must be before death date of the individual"""

    lst = []
    for k, v in family.items():
        if v.divorced != 'NA':
            #get husband and wife ids death date
            husband_death = individual[v.husband_id].death
            wife_death = individual[v.wife_id].death

            if husband_death != 'NA' and husband_death < v.divorced:
                lst.append(f"US_06: {v.husband_name} Death {husband_death} occured prior to the divorce date {v.divorced}")
            
            elif wife_death != 'NA' and wife_death < v.divorced:
                lst.append(f"US_06: {v.wife_name} Death {wife_death} occured prior to the divorce date {v.divorced}")

    return lst
