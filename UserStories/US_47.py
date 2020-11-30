def US_47(individual, family):
    for fam in family.values():
        husband_birth = individual[fam._husband_id]._age
        wife_Birth = individual[fam._wife_id]._age
        if (husband_birth - wife_Birth) > 25:
            yield f"Husband {fam._husband_id} is 25 or more year older than wife {fam._wife_id}."
        elif (wife_Birth - husband_birth) > 25:
            yield f"Wife {fam._wife_id} is 25 or more year older than husband {fam._husband_id}."
