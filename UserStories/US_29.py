def US_29(self):
    result=[]
    for key, individual in self._individual.items():
        if individual._death_date != 'NA':
            result.append(individual._name)
    return(result)
