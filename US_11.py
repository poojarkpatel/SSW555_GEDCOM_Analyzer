"""
Author: ...Priyankaben Shyiani....
SSW 555 Agile Methods for Software Development 
Purpose: user story 11
"""
def US_11(self):
        """US11: checks if there is bigamy happening in a family in where husband/wife is married twice in the same time."""
        data = list()
        processed = set()
        for fam in self._family.values():
            for fam2 in self._family.values():
                ids = tuple(sorted([fam._family, fam2._family]))
                if fam._family != fam2._family and ids not in processed:
                    processed.add(ids)
                    if fam._husband_id == fam2._husband_id:
                        if fam._divorced == 'NA' and fam2._divorced == 'NA' \
                        or fam._married < fam2._married < fam._divorced:
                            try:
                                data.append(self._individual[fam._husband_id]._name + "married twice at the same time")
                            except KeyError:
                                print(f'Husband or Wife is married twice at the same time.')
                    if fam._wife_id == fam2._wife_id:
                        if fam._divorced == 'NA' and fam2._divorced == 'NA' \
                        or fam._married < fam2._married < fam._divorced:
                            try:
                                data.append(self._individual[fam._wife_id]._name + "married twice at the same time")
                            except KeyError:
                                print(f'Husband or Wife is married twice at the same time.')
        return data

