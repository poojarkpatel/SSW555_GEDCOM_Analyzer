"""
Author: Priyankaben Shyiani
SSW 555 Agile Methods for Software Development 
Purpose: user story 33
"""
def US_33(self):
        """List all orphaned children (both parents dead and child < 18 years old) in a GEDCOM file"""
        orphans = list()
        for fam in self.family.values():
            if fam.children != 'NA':
                for child in fam.children:
                    if fam.husband_id and fam.wife_id:
                        if self.individual[fam.husband_id].death != 'NA' and self.individual[fam.wife_id].death != 'NA' and \
                                self.individual[child].age != 'NA' and self.individual[child].age < 18 and self.individual[child].age >=0:
                            orphans.append(f"{self.individual[child].individual} {self.individual[child].name}"
                                           f"has age {self.individual[child].age} and is orphan")

        return orphans

