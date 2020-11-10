def US_28(individual, family):
    result = []
    temp=[]
    p=[]
    for key, family in family.items():
        result1 = []
        list_children = family._children
        if list_children != "NA":
            for child in list_children:
                result1.append(individual[child])
                result1.sort(key=lambda x:individual[child]._age,reverse=False)
                if len(result1)>1:
                    result.append("List of siblings" + family._family_id + "after sorting is")
                    for child in result1:
                        if child._age >= 0:
                            temp.append(str(len(str(child._age)))+" "+str(child._age)+" :- "+child._name +" from FamID "+family._family_id +" with individual id " + child._individual_id
                                        +" is on line number "+ str(individual[child._individual_id].get_line_numbers()["individual_id"]))
            temp=list(set(temp))
    for _ in sorted(temp,reverse=True):
        x=_.split(" ")
        y=" ".join(map(str,x[1:]))
        p.append(y)
    return sorted(p,reverse=True)
