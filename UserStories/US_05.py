"""Marriage should occur before death of either spouse"""


def US_05(individual, family):
    for fam in family.values():
        married = fam._marriage_date
        for indi in individual.values():
            if fam._husband_id == indi._individual_id and indi._death_date != 'NA':
                if indi._death < married:
                    yield f"Marriage date Line: {fam._line_numbers.get('date').get('marriage')}" \
                        f"\nDeath of Husband date Line: {indi._line_numbers.get('date').get('death')}\n" \
                        f"The family {fam._family_id} has a death of husband {fam._husband_id} before the marriage date."
            elif fam._wife_id == indi._individual_id and indi._death_date != 'NA':
                if indi._death_date < married:
                    yield f"Marriage date Line: {fam._line_numbers.get('date').get('marriage')}" \
                        f"\nDeath of wife date Line: {indi._line_numbers.get('date').get('death')}\n" \
                        f"The family {fam._family_id} has a death of wife {fam._wife_id} before the marriage date."

