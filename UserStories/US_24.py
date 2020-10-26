warnings = list()

def US_24(family):
    """ No more than one family with the same spouses by name and the same marriage date should appear in a GEDCOM file """
    fam_dict = dict()
    
    for fam, value in family.items():
        marriage_date = value._marriage_date
        if marriage_date != 'NA':
            husband_name = value._husband_name
            wife_name = value._wife_name

            if marriage_date in fam_dict:
                if husband_name in fam_dict[marriage_date] or wife_name in fam_dict[marriage_date]:
                    warnings.append(f'Family contains same husband, wife and marriage date as another family, Line number: {value.get_line_numbers()["date"]["marriage"]}')
            else:
                fam_dict[marriage_date] = set()

            fam_dict[marriage_date].add(husband_name)
            fam_dict[marriage_date].add(wife_name)

    return warnings    
