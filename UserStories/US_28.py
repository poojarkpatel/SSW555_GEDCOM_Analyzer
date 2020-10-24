def US_28(self):
    result = []
    temp=[]
    p=[]
    for key, family in self.family.items():
        result1 = []
        list_children = family.children
        if list_children != "NA":
            for child in list_children:
                result1.append(self.individual[child])
                result1.sort(key=lambda x:self.individual[child].age, reverse=False)
                if len(result1)>1:
                    result.append("List of siblings" + family.family + "after sorting is")
                    for child in result1:
                        if child.age >= 0:
                            temp.append(str(len(str(child.age))) + " " + str(child.age) + " :- " + child.name + " from FamID " + family.family)
            temp=list(set(temp))
    for _ in sorted(temp,reverse=True):
        x=_.split(" ")
        y=" ".join(map(str,x[1:]))
        p.append(y)
    return sorted(p,reverse=True)
