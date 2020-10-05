""" Base File"""
from typing import Iterator, IO, List, Dict
import datetime
import math
from prettytable import PrettyTable
import sys
from US_35 import recent_births
from US_25 import us_25
from US_28 import US_28
from US_29 import US_29
# from collections import defaultdict

class Logger(object):
    def __init__(self):
        self.terminal = sys.stdout
        self.log = open("output.txt", "w")

    def write(self, message):
        self.terminal.write(message)
        self.log.write(message)

    def flush(self):
        pass


class Individual:
    """
    This class stores information of individuals and returns the stored info in form of a list
    """
    PT_FIELD_NAMES = ['Id', 'Name', 'Gender', 'Birthday', 'Age', 'Alive', 'Deathdate', 'Child', 'Spouse']
    # Class attribute of class individual storing pretty table fields

    def __init__(self, individual) -> None:
        """
        init method of class individual
        """
        self._individual = individual
        self._name = ""
        self._gender = ""
        self._birth = ""
        self._age = 0
        self._alive = False
        self._death = "NA"
        self._famC = set()
        self._famS = set()

    def set_name(self, name):
        """ sets the name of individual"""
        self._name = name

    def get_name(self) -> str:
        """ returns the name of individual"""
        return self._name

    def set_gender(self, gender):
        """ sets the gender of individual"""
        self._gender = gender

    def set_birth_death_date(self, date):
        """ sets the birth-date and death-date of individual """
        if not self._alive:
            self._birth = datetime.datetime.strptime(date, '%d %b %Y').date()
            today = datetime.date.today()  # today's date
            self._age = today - self._birth  # current age
            self._age = math.floor(self._age.days / 365)
            self._alive = True
        else:
            self._death = datetime.datetime.strptime(date, '%d %b %Y').date()
            self._age = self._death - self._birth  # obtaining birthday for a deceased individual
            self._age = math.floor(self._age.days / 365)  # age at which individual died
            self._alive = False

    def set_child(self, child):
        """ sets the id of family in which the individual is child"""
        self._famC.add(child)

    def set_spouse(self, spouse):
        """ sets the id of family in which the individual is spouse"""
        self._famS.add(spouse)

    def info_individual(self):
        """ returns the information of individual in form of list"""
        if self._famC == set():
            self._famC = "NA"
        if self._famS == set():
            self._famS = "NA"
        return list((self._individual, self._name, self._gender, self._birth, self._age, self._alive, self._death,
                     self._famC, self._famS))


class Family:
    """ This class stores information of family"""
    PT_FIELD_NAMES = ['Id', 'Married', 'Divorced', 'Husband ID', 'Husband Name', 'Wife ID', 'Wife Name', 'Children']

    def __init__(self, family) -> None:
        """init function of family"""
        self._family = family
        self._married = "NA"
        self._divorced = "NA"
        self._husband_id = ""
        self._husband_name = ""
        self._wife_name = ""
        self._wife_id = ""
        self._is_divorced = False
        self._children = set()

    def set_husband_name(self, name):
        """sets the name of husband in family"""
        self._husband_name = name

    def set_wife_name(self, name):
        """sets the name of wife in family"""
        self._wife_name = name

    def set_husband_id(self, husband_id):
        """sets husband ID"""
        self._husband_id = husband_id

    def set_wife_id(self, wife_id):
        """sets wife ID"""
        self._wife_id = wife_id

    def set_marriage_divorce_date(self, date):
        """
        sets marriage and divorce date (if any)
        """
        if not self._is_divorced:
            self._married = datetime.datetime.strptime(date, '%d %b %Y').date()
            self._is_divorced = True
        else:
            self._divorced = datetime.datetime.strptime(date, '%d %b %Y').date()
            self._is_divorced = False

    def set_child(self, child):
        """sets child"""
        self._children.add(child)

    def info_family(self):
        """ returns family info in the form of list"""
        if self._children == set():
            self._children = "NA"
        return list((self._family, self._married, self._divorced, self._husband_id, self._husband_name, self._wife_id,
                     self._wife_name, self._children,))


class Repository:
    def __init__(self, path: str) -> None:
        # self._path: str = path
        self._path: str = path
        self._individual: Dict[str, Individual] = dict()
        self._family: Dict[str, Family] = dict()
        # self._family = defaultdict(str)
        self._read_ged()
        # self.individual_pretty_table()
        # self.family_pretty_table()

    def _validate_gedcom(self) -> Iterator[str]:
        """ Validates gedcom file
            Checks for valid tags and levels
            Checks individual should be less than or equal to 5000 and families should be less than or equal to 1000
        """
        # file_name: str = os.path.join(self._path, 'ssw555_input_file.ged')
        # current_directory = os.getcwd()
        # set_current_directory = os.chdir(current_directory)
        try:
            fp: IO = open(self._path, 'r')
        except FileNotFoundError:
            print(f"can't open {self._path}")
        else:
            with fp:  # closes the file properly and clean everything up.
                tag_dict: Dict = {"INDI": 0, 'NAME': 1, "SEX": 1, "BIRT": 1, "DEAT": 1, "FAMC": 1, "FAM": 0, "FAMS": 1,
                                  "MARR": 1,
                                  "HUSB": 1, "WIFE": 1, "CHIL": 1,
                                  "DIV": 1, "DATE": 2, "HEAD": 0, "TRLR": 0, "NOTE": 0}
                list_individual_count: int = 0
                list_family_count: int = 0
                for line in fp:
                    output_line_list: List = line.strip("\n").split(" ", 2)
                    list_individual = [item for item in output_line_list if
                                       item.startswith("@I") and item.endswith("@")]
                    list_family = [item for item in output_line_list if item.startswith("@F") and item.endswith("@")]
                    list_family_count += len(list_family)
                    list_individual_count += len(list_individual)
                    if list_individual_count < 5000 and list_family_count < 1000:
                        if any(item in output_line_list for item in list(tag_dict.keys())):
                            item = [item for item in output_line_list if item in list(tag_dict.keys())]
                            if output_line_list[1] not in tag_dict.keys():
                                index = output_line_list.index(item[0])
                                output_line_list[index], output_line_list[1] = output_line_list[1], output_line_list[index]

                                if len(output_line_list) > 2 and str(output_line_list[0]) == str(tag_dict[output_line_list[1]]):
                                    yield output_line_list[1], output_line_list[2]

                            else:
                                if len(output_line_list) > 2 and str(output_line_list[0]) == str(tag_dict[output_line_list[1]]):
                                    yield output_line_list[1], output_line_list[2]
                    else:
                        raise ValueError("Total 5000 individuals and 1000 families are allowed")

    def _read_ged(self) -> None:
        """
        set values after reading file
        """
        id = ""
        fam_id = ""
        indi_flag = False

        for tag, arg in self._validate_gedcom():
            if tag == "INDI" and not indi_flag:
                id = arg
                if arg not in self._individual.keys():
                    self._individual[arg] = Individual(arg)
            elif tag == "NAME" and not indi_flag:
                self._individual[id].set_name(arg)
            elif tag == "SEX" and not indi_flag:
                self._individual[id].set_gender(arg)
            elif tag == "DATE" and not indi_flag:
                self._individual[id].set_birth_death_date(arg)
            elif tag == "FAMC" and not indi_flag:
                self._individual[id].set_child(arg)
            elif tag == "FAMS" and not indi_flag:
                self._individual[id].set_spouse(arg)
            elif tag == "FAM":
                indi_flag = True
                fam_id = arg
                if arg not in self._family.keys():
                    self._family[fam_id] = Family(fam_id)
            elif tag == "HUSB":
                self._family[fam_id].set_husband_id(arg)
                self._family[fam_id].set_husband_name(self._individual[arg].get_name())
            elif tag == "WIFE":
                self._family[fam_id].set_wife_id(arg)
                self._family[fam_id].set_wife_name(self._individual[arg].get_name())
            elif tag == "CHIL":
                self._family[fam_id].set_child(arg)
            elif tag == "DATE":
                self._family[fam_id].set_marriage_divorce_date(arg)

    def individual_pretty_table(self):
        """ individual pretty table"""
        pt = PrettyTable(field_names=Individual.PT_FIELD_NAMES)
        for value in self._individual.values():
            pt.add_row(value.info_individual())
        print(pt)

    def family_pretty_table(self):
        """Family pretty table"""
        pt = PrettyTable(field_names=Family.PT_FIELD_NAMES)
        for value in self._family.values():
            pt.add_row(value.info_family())
        print(pt)


if __name__ == '__main__':
    """ main file """
    sys.stdout = Logger()
    indi_repo: Repository = Repository("ssw555_input_file.ged")# change path where you gedcomfile is present
    indi_repo.individual_pretty_table()
    indi_repo.family_pretty_table()

    indi_repo_us_35: Repository = Repository("US_35.ged")
    for item in recent_births(indi_repo_us_35._individual):
        print(f"US_35: {item}")

    indi_repo_us_25: Repository = Repository("US_25.ged")
    for item in us_25(indi_repo_us_25._individual, indi_repo_us_25._family):
        print(f"US_25: {item}")

    indi_repo_us_28: Repository = Repository("US_28.ged")
    for item in US_28(indi_repo_us_28):
        print(f"US_28: Age {item}")

    indi_repo_us_29: Repository = Repository("US_29.ged")
    for item in US_29(indi_repo_us_29):
        print(f"US_29: {item} is deceased individual")

