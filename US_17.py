def US_17(family_object):
    """ Function that checks if parents are married to their children """
    result = list()
    parents_to_children = dict()

    for attribute in family_object:
        family_info = attribute.info_family()

        husband_id = family_info[3]
        wife_id = family_info[5]

        if husband_id not in parents_to_children:
            parents_to_children[husband_id] = set()

        if wife_id not in parents_to_children:
            parents_to_children[wife_id] = set()

        for child in family_info[7]:
            parents_to_children[husband_id].add(child)
            parents_to_children[wife_id].add(child)

    for attribute in family_object:
        family_info = attribute.info_family()

        husband_id = family_info[3]
        wife_id = family_info[5]

        if wife_id in parents_to_children[husband_id]:
            result.append(f'US_17: {husband_id} married to his daughter {wife_id}')
        elif husband_id in parents_to_children[wife_id]:
            result.append(f'US_17: {wife_id} married to her son {husband_id}')

    return result
