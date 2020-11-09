from datetime import date
def us_37(individual,family):
    warnings = []
    for family1 in family.values():
        if family1._husband_id != "" and family1._wife_id != "":
            hdetail = individual[family1._husband_id]
            wdetail = individual[family1._wife_id]
            try:
                if hdetail._famS.intersection(wdetail._famS) or wdetail._famS.intersection(hdetail._famS):
                    if hdetail._death_date != "NA":
                        d1 = (hdetail._death_date)
                        d2 = (date.today())
                        if(d2-d1).days < 30:
                            for key,value in individual.items():
                                if family1._children == {key}:
                                    if wdetail._death_date == "NA":
                                        warnings.append(f' Living spouse: {wdetail._name} and Descendant : {value._name} on line number {family1.get_line_numbers()["wife_id"]} ')


                    if wdetail._death_date != "NA":
                        d3 = (wdetail._death_date)
                        d4 = (date.today())
                        if (d4 -d3).days < 30:
                            for key, value in individual.items():
                                if family1._children == {key}:
                                    if hdetail._death_date == "NA":
                                        warnings.append(f'Living Spouse: {hdetail._name} and descendant : {value._name} on line number {family1.get_line_numbers()["husband_id"]}')
            except:
                pass

    return warnings

