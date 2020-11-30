def US_50(family):
    """ Function that lists people who remarried. """
    names_seen = set()
    warnings = set()

    for family_id, family_details in family.items():
        if family_details._husband_name in names_seen:
            warnings.add(family_details._husband_name)

        if family_details._wife_name in names_seen:
            warnings.add(family_details._wife_name)

        names_seen.add(family_details._husband_name)
        names_seen.add(family_details._wife_name)

    print(warnings)
    return warnings
