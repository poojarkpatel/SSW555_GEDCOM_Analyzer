def us_45(individual):
    result=[]
    for key, individual in individual.items():
        if individual._is_alive != False:
            result.append(f'{individual._name} on line number {individual.get_line_numbers()["date"]["birth"]}')
    return(result)
