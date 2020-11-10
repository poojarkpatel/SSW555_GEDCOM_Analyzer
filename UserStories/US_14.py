from collections import defaultdict


def US_14(individual, family):
    '''No more than five siblings should be born at the same time '''

    y = []
    b, n = 0, 0
    for k, v in family.items():
        # fam_result.extend(fam_result)
        child_bday = defaultdict(int)
        if len(v._children) >= 5:
            if v._children != 'NA':
                for child in [individual[c] for c in v._children]:
                    child_bday[child._birth_date] += 1
                    for b_date, no in child_bday.items():
                        if no >= 5:
                            # y.append(b_date)
                            b = b_date
    if v._children != 'NA':
        output = f"US14: {k} has more than 5 children born on same date {b} in line number {family[k].get_line_numbers()['family_id']}"
        y.append(output)

    return y