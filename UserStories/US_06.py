def US_06(individual,family):
    """ US06 : Divorce of the husband or wife must be before death date of the individual"""

    lst = []
    for k, v in family.items():
        if v._divorce_date != 'NA':
            #get husband and wife ids death date
            husband_death = individual[v._husband_id]._death_date
            wife_death = individual[v._wife_id]._death_date

            if husband_death != 'NA' and husband_death < v._divorce_date:
                lst.append(f"US_06: {v._husband_name} Death {husband_death} occured prior to the divorce date {v._divorce_date}")
            
            elif wife_death != 'NA' and wife_death < v._divorce_date:
                lst.append(f"US_06: {v._wife_name} Death {wife_death} occured prior to the divorce date {v._divorced}")

    return lst
