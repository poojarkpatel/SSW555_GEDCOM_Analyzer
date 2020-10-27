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
                ids = tuple(sorted([fam._family_id, fam2._family_id]))
                if fam._family_id != fam2._family_id and ids not in processed:
                    processed.add(ids)
                    if fam._husband_id == fam2._husband_id:
                        if fam._divorce_date == 'NA' and fam2._divorce_date == 'NA' \
                        or fam._marriage_date < fam2._marriage_date < fam._divorce_date:
                            try:
                                data.append(self._individual[fam._husband_id]._name + "married twice at the same time")
                            except KeyError:
                                print(f'Husband or Wife is married twice at the same time.')
                    if fam._wife_id == fam2._wife_id:
                        if fam._divorce_date == 'NA' and fam2._divorce_date == 'NA' \
                        or fam._marriage_date < fam2._marriage_date < fam._divorce_date:
                            try:
                                data.append(self._individual[fam._wife_id]._name + "married twice at the same time")
                            except KeyError:
                                print(f'Husband or Wife is married twice at the same time.')
        return data

