def us_45(self):
    result=[]
    for key, individual in self._individual.items():
        if individual._is_alive != False:
            result.append(f'{individual._name} on line number {individual.get_line_numbers()["date"]["birth"]}')
    return(result)
