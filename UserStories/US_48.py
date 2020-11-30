def US_48(individual, family):
    for fam in family.values():
        husband_birth = individual[fam._husband_id]._birth_date
        wife_Birth = individual[fam._wife_id]._birth_date
        if husband_birth > wife_Birth:
            yield f"Wife {fam._wife_id} is older than husband {fam._husband_id}."