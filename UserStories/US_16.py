def US_16(individual, family):
    """ US16	Male last names	All male members of a family should have the same last name """
    lst = []
    for k, v in family.items():
        lastname = v._husband_name.split('/')[1]
        if v._husband_id != 'NA' and v._children != 'NA':
            for id in v._children:
                if individual[id]._gender == 'M':
                    c_name = individual[id]._name
                    c_last_name = individual[id]._name.split('/')[1]
                    if lastname != c_last_name:
                        output = f"US_16: Family id {k} with father {v._husband_name} and son {c_name} have different last names on line number {family[k].get_line_numbers()['family_id']}"
                        lst.append(output)

    lst.sort()
    return lst