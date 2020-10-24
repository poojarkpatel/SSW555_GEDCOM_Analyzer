def US_29(self):
    result=[]
    for key, individual in self.individual.items():
        if individual.death != 'NA':
            result.append(individual.name)
    return(result)            