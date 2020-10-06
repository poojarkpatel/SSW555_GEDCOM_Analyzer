"""
Author: Priyankaben Shyiani
SSW 555 Agile Methods for Software Development 
Purpose: user story 33
"""
def US_33(self):
        """List all orphaned children (both parents dead and child < 18 years old) in a GEDCOM file"""
        orphans = list()
        for fam in self._family.values():
            if fam._children != 'NA':
                for child in fam._children:
                    if fam._husband_id and fam._wife_id:
                        if self._individual[fam._husband_id]._death != 'NA' and self._individual[fam._wife_id]._death != 'NA' and \
                                self._individual[child]._age != 'NA' and self._individual[child]._age < 18:
                            orphans.append(f"{self._individual[child]._individual} {self._individual[child]._name} "
                                           f"has age {self._individual[child]._age} and is orphan")

        return orphans

