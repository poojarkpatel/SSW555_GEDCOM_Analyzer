def US_17(familyList):
    """ Function that checks if parents are married to their children """
    parents_to_children = dict()

    for value in familyList.values():
        husband_id = value[2]
        wife_id = value[4]

        if husband_id not in parents_to_children:
            parents_to_children[husband_id] = set()

        if wife_id not in parents_to_children:
            parents_to_children[wife_id] = set()

        for child in value[6]:
            parents_to_children[husband_id].add(child)
            parents_to_children[wife_id].add(child)

    for value in familyList.values():
        husband_id = value[2]
        wife_id = value[4]

        if wife_id in parents_to_children[husband_id] or husband_id in parents_to_children[wife_id]:
            raise ValueError('Parents married to their children.')