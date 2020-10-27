def US_29(self):
    result=[]
    for key, individual in self._individual.items():
        if individual._death_date != 'NA':
            result.append(f'{individual._name} on line number {individual.get_line_numbers()["date"]["birth"]}')
    return(result)
