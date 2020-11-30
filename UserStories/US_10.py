"""Marriage after 14"""

import math


def US_10(individual, family):
    for fam in family.values():
        marriage_date = fam._marriage_date
        if marriage_date != 'NA':
            husband_marriage_age = marriage_date - individual[fam._husband_id]._birth_date
            wife_marriage_age = marriage_date - individual[fam._wife_id]._birth_date
            if math.floor(husband_marriage_age.days / 365) <= 14:
                yield f"Family id Line number: {fam._line_numbers.get('family_id')}\n" \
                    f"The husband {fam._husband_id} was younger than 14 at the time of marriage for {fam._family_id}"
            if math.floor(wife_marriage_age.days / 365) <= 14:
                yield f"Family id Line number: {fam._line_numbers.get('family_id')}\n" \
                    f"The wife {fam._wife_id} was younger than 14 at the time of marriage for {fam._family_id}"