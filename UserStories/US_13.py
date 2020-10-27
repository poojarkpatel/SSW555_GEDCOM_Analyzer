import datetime

def US_13(family_object, individual_object):
    """ To check if the sibiling are twins """
    warnings = set()
    for attribute in family_object.values():    
        child = list(attribute._children)
        if child != ['N','A']:
            for i in range(0, len(child)):          
                for j in range(i + 1, len(child)):
                    person_one_id = child[i] 
                    person_two_id = child[j]

                    date_one = individual_object[person_one_id]._birth_date
                    date_two = individual_object[person_two_id]._birth_date
                    try:
                        difference = date_one - date_two
                    except:
                        continue
                    if date_one < date_two:
                        difference = date_two - date_one

                    if difference > datetime.timedelta(days=2) and difference < datetime.timedelta(days=240):
                        a = sorted([person_one_id, person_two_id])
                        warnings.add(f"The family id {attribute._family_id} has twins {individual_object[a[0]]._name} and {individual_object[a[1]]._name}")
        child = []       
    return warnings
                        