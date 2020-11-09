""" File that contains all the information of a family repository. """
from prettytable import PrettyTable
from typing import Iterator, IO, List, Dict

from Programs.Individual import Individual
from Programs.Family import Family

class Repository:
    """ Class that contains all the information of a family repository. """
    def __init__(self, path: str) -> None:
        """ Function that initializes variables path, individual, family and read_ged. """
        self._path: str = path
        self._individual: Dict[str, Individual] = dict()
        self._family: Dict[str, Family] = dict()
        self._read_ged()

    def get_individual(self):
        return self._individual

    def get_family(self):
        return self._family

    def _validate_gedcom(self) -> Iterator[str]:
        """ Function that validates GEDCOM file, checks if it conform to all the given constraints. """
        try:
            fp: IO = open(self._path, 'r')
        except FileNotFoundError:
            # Prints an error message in case GEDCOM file can't be found/opened.
            print(f"can't open {self._path}")
        else:
            # Closes the file properly and clears everything up.
            with fp:
                tag_dict: Dict = {"INDI": 0, 'NAME': 1, "SEX": 1, "BIRT": 1, "DEAT": 1, "FAMC": 1, "FAM": 0, "FAMS": 1,
                                  "MARR": 1,
                                  "HUSB": 1, "WIFE": 1, "CHIL": 1,
                                  "DIV": 1, "DATE": 2, "HEAD": 0, "TRLR": 0, "NOTE": 0}

                for line_number, line in enumerate(fp, 1):
                    output_line_list: List = line.strip("\n").split(" ", 2)
                    if any(item in output_line_list for item in list(tag_dict.keys())):
                        item = [item for item in output_line_list if item in list(tag_dict.keys())]
                        if output_line_list[1] not in tag_dict.keys():
                            index = output_line_list.index(item[0])
                            output_line_list[index], output_line_list[1] = output_line_list[1], output_line_list[index]
                            if len(output_line_list) > 2 and str(output_line_list[0]) == str(tag_dict[output_line_list[1]]):
                                yield output_line_list[1], output_line_list[2], line_number
                        else:
                            if len(output_line_list) > 2 and str(output_line_list[0]) == str(tag_dict[output_line_list[1]]):
                                yield output_line_list[1], output_line_list[2], line_number

    def _read_ged(self) -> None:
        """ Funciton that stores values after reading the GEDCOM file. """
        id = ""
        fam_id = ""
        indi_flag = False

        for tag, arg, line_number in self._validate_gedcom():
            if tag == "INDI" and not indi_flag:
                id = arg
                if arg not in self._individual.keys():
                    self._individual[arg] = Individual(arg, line_number)
                else:
                    print(f" US_22: Line number:{line_number} Id already exists")
            elif tag == "NAME" and not indi_flag:
                self._individual[id].set_name(arg, line_number)
            elif tag == "SEX" and not indi_flag:
                self._individual[id].set_gender(arg, line_number)
            elif tag == "DATE" and not indi_flag:
                self._individual[id].set_birth_death_date(arg, line_number)
            elif tag == "FAMC" and not indi_flag:
                self._individual[id].set_child(arg)
            elif tag == "FAMS" and not indi_flag:
                self._individual[id].set_spouse(arg)
            elif tag == "FAM":
                indi_flag = True
                fam_id = arg
                if arg not in self._family.keys():
                    self._family[fam_id] = Family(fam_id, line_number)
                else:
                    print(f" US_22: Line number:{line_number} Family Id already exists")
            elif tag == "HUSB":
                self._family[fam_id].set_husband_id(arg, line_number)
                self._family[fam_id].set_husband_name(self._individual[arg].get_name())
            elif tag == "WIFE":
                self._family[fam_id].set_wife_id(arg, line_number)
                self._family[fam_id].set_wife_name(self._individual[arg].get_name())
            elif tag == "CHIL":
                self._family[fam_id].set_child(arg)
            elif tag == "DATE":
                self._family[fam_id].set_marriage_divorce_date(arg, line_number)

    def individual_pretty_table(self):
        """ Function that prints individual pretty table. """
        pt = PrettyTable(field_names=Individual.PT_FIELD_NAMES)
        for value in self._individual.values():
            pt.add_row(value.info_individual())
        print(pt)

    def family_pretty_table(self):
        """ Function that prints family pretty table. """
        pt = PrettyTable(field_names=Family.PT_FIELD_NAMES)
        for value in self._family.values():
            pt.add_row(value.info_family())
        print(pt)

    def add_individual(self, i):
        """ must pass in individual
        US22: checks if the individual ids are unique
        """
        if i.iid in self._individual.keys():
            print(f'US22 - {i.iid} id has a duplicate in line number ')
        self._individual[i.iid] = i
        return Individual()