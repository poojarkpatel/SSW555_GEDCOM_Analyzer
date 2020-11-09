def us_34(individual,family):
    warnings = []
    l1 = []
    l2 = []
    for family1 in family.values():
        if family1._husband_id != "" and family1._wife_id != "":
            hubdetail = individual[family1._husband_id]
            wifedetail = individual[family1._wife_id]
            hubage = hubdetail._age
            wifeage = wifedetail._age
            if hubage !=0 and wifeage != 0:
                l1.append(hubage)
                l2.append(wifeage)
                agediff = hubage / wifeage
                l1=[]
                l2=[]
                if agediff >= 2 or agediff <= 0.5:
                    warnings.append(f'{family1._husband_name},{hubage} and {family1._wife_name} ,{wifeage}  are the couples who were married when the older spouse was more than as twice as old as the younger spouse on line number {family1.get_line_numbers()["husband_id"]}')

    return warnings



