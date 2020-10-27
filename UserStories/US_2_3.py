def US_2(individual, family):
        """checks if a person's birthday occurs before their marriage"""
        warnings = list()

        for family in family.values():
            if family._marriage_date != 'NA':
                if family._wife_id != 'NA':
                    if individual[family._wife_id]._birth_date != 'NA':
                        if individual[family._wife_id]._birth_date > family._marriage_date:
                            warnings.append(f'US_02 - {individual[family._wife_id]._name} birthday after marriage date on line number {family.get_line_numbers()["date"]["marriage"]}')
                        
                if family._husband_id != 'NA':
                    if individual[family._husband_id]._birth_date != 'NA':
                        if individual[family._husband_id]._birth_date > family._marriage_date:
                            warnings.append(f'US_02 - {individual[family._husband_id]._name} birthday after marriage date on line number {family.get_line_numbers()["date"]["marriage"]}')

        return warnings
                        
def US_3(individual):
        """ checks if a person's birthday occurs before their death day """
        warnings = list()

        for person in individual.values():
            if person._birth_date != 'NA' and person._death_date != 'NA':
                if person._birth_date > person._death_date:
                    warnings.append(f'US_03 - {person._name} birthday after death date on line number {person.get_line_numbers()["date"]["death"]}')

        return warnings

