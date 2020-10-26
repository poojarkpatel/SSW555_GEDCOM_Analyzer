"""Children should be born after marriage of parents (and not more than 9 months after their divorce)"""


def US_08(individual, family):
    for fam in family.values():
        if fam._children != 'NA':
            husband_birth = individual[fam._husband_id]._birth
            wife_birth = individual[fam._wife_id]._birth
            for child in fam._children:
                if individual[child]._birth < husband_birth:
                    yield f"Family id Line number: {fam._line_numbers.get('family_id')}\nThe Father {fam._husband_id}" \
                          f" is younger than his child {individual[child]._individual_id} which is illeagal. "
                elif individual[child]._birth < wife_birth:
                    yield f"Family id Line number: {fam._line_numbers.get('family_id')}\nThe Mother {fam._wife_id} " \
                          f"is younger than her child {individual[child]._individual_id} which is illeagal. "
