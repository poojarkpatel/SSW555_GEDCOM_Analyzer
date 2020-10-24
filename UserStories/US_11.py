"""
Author: ...Priyankaben Shyiani....
SSW 555 Agile Methods for Software Development 
Purpose: user story 11
"""

def US_11(self):
        """US11: checks if there is bigamy happening in a family in where husband/wife is
        married twice in the same time."""
        data = list()
        processed = set()
        for fam in self.family.values():
            for fam2 in self.family.values():
                ids = tuple(sorted([fam.family, fam2.family]))
                if fam.family != fam2.family and ids not in processed:
                    processed.add(ids)
                    if fam.husband_id == fam2.husband_id:
                        if fam.divorced == 'NA' and fam2.divorced == 'NA' \
                        or fam.married < fam2.married < fam.divorced:
                            try:
                                data.append(self.individual[fam.husband_id].name + "married twice at the same time")
                            except KeyError:
                                print(f'Husband or Wife is married twice at the same time.')
                    if fam.wife_id == fam2.wife_id:
                        if fam.divorced == 'NA' and fam2.divorced == 'NA' \
                        or fam.married < fam2.married < fam.divorced:
                            try:
                                data.append(self.individual[fam.wife_id].name + "married twice at the same time")
                            except KeyError:
                                print(f'Husband or Wife is married twice at the same time.')
        return data

