"""
Author: Priyankaben Shyiani
SSW 555 Agile Methods for Software Development
Purpose: user story 43
"""
def US_43(individual, family):
        """List all living people who is divorced in file"""
        warnings = list()

        for family in family.values():
            if family._divorce_date != "NA":
                if family._wife_id != 'NA':
                    if individual[family._wife_id]._birth_date != 'NA':
                        if individual[family._wife_id]._is_alive == True and family._is_divorced == False:
                            warnings.append(f'{individual[family._wife_id]._name} is divorced and alive on line number {individual[family._wife_id].get_line_numbers()["date"]["birth"]}')

                if family._husband_id != 'NA':
                    if individual[family._husband_id]._birth_date != 'NA':
                        if individual[family._husband_id]._is_alive == True and family._is_divorced == False:
                            warnings.append(f'{individual[family._husband_id]._name} is divorced and alive on line number {individual[family._husband_id].get_line_numbers()["date"]["birth"]}')

        return warnings