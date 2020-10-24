def US_17(family_object):
    """ Function that checks if parents are married to their children """
    result = dict()
    parents_to_children = dict()

    for attribute in family_object:
        family_info = attribute.info_family()

        husband_id = family_info[3]
        wife_id = family_info[5]

        if husband_id not in parents_to_children:
            parents_to_children[husband_id] = list()

        if wife_id not in parents_to_children:
            parents_to_children[wife_id] = list()

        for child in family_info[7]:
            parents_to_children[husband_id].append(child)
            parents_to_children[wife_id].append(child)

    for attribute in family_object:
        family_info = attribute.info_family()

        husband_id = family_info[3]
        husband_name = family_info[4]
        wife_id = family_info[5]
        wife_name = family_info[6]

        if (husband_id in parents_to_children and wife_id in parents_to_children[husband_id]) or (wife_id in parents_to_children and husband_id in parents_to_children[wife_id]):
            result[husband_name] = wife_name

    return result
