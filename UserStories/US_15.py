def US_15(family):
    """ US15	Fewer than 15 siblings. There should be fewer than 15 siblings in a family
    """
    
    warnings = []
    for key, value in family.items():
        if(len(value._children)) >= 15:
            warnings.append(f"US:15 Family id:{key} has 15 or more children on line number {family[key].get_line_numbers()['family_id']}")

    return warnings
