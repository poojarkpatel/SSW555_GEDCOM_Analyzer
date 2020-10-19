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
from US_11 import US_11
from US_33 import US_33
from US_06 import US_06
from US_07 import US_07
from US01 import us01
from US04 import us04
from US_17 import US_17
from US_23 import US_23
from US_13 import US_13
from US_18 import US_18
from us_32_36 import us_36, us_32
# from us_42 import validate_date



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
        self.individual = individual
        self.name = ""
        self.gender = ""
        self.birth = "NA"
        self.age = 0
        self.alive = False
        self.death = "NA"
        self.famC = set()
        self.famS = set()
        self.line_num = 1

    def set_name(self, name, line_num):
        """ sets the name of individual"""
        self.name = name
        self.line_num = line_num

    def get_name(self) -> str:
        """ returns the name of individual"""
        return self.name

    def set_gender(self, gender):
        """ sets the gender of individual"""
        self.gender = gender

    def set_birth_death_date(self, date):
        """ sets the birth-date and death-date of individual """
        # date = validate_date(date)
        if not self.alive:
            self.birth = datetime.datetime.strptime(date, '%d %b %Y').date()
            today = datetime.date.today()  # today's date
            self.age = today - self.birth  # current age
            self.age = math.floor(self.age.days / 365)
            if self.age < 0:
                self.age = 0
            self.alive = True
        else:
            self.death = datetime.datetime.strptime(date, '%d %b %Y').date()
            self.age = self.death - self.birth  # obtaining birthday for a deceased individual

            self.age = math.floor(self.age.days / 365)  # age at which individual died
            self.alive = False

    def set_child(self, child):
        """ sets the id of family in which the individual is child"""
        self.famC.add(child)

    def set_spouse(self, spouse):
        """ sets the id of family in which the individual is spouse"""
        self.famS.add(spouse)

    def info_individual(self):
        """ returns the information of individual in form of list"""
        if self.famC == set():
            self.famC = "NA"
        if self.famS == set():
            self.famS = "NA"
        return list((self.individual, self.name, self.gender, self.birth, self.age, self.alive, self.death,
                     self.famC, self.famS))


class Family:
    """ This class stores information of family"""
    PT_FIELD_NAMES = ['Id', 'Married', 'Divorced', 'Husband ID', 'Husband Name', 'Wife ID', 'Wife Name', 'Children']

    def __init__(self, family) -> None:
        """init function of family"""
        self.family = family
        self.married = "NA"
        self.divorced = "NA"
        self.husband_id = ""
        self.husband_name = ""
        self.wife_name = ""
        self.wife_id = ""
        self.is_divorced = False
        self.children = set()

    def set_husband_name(self, name):
        """sets the name of husband in family"""
        self.husband_name = name

    def set_wife_name(self, name):
        """sets the name of wife in family"""
        self.wife_name = name

    def set_husband_id(self, husband_id):
        """sets husband ID"""
        self.husband_id = husband_id

    def set_wife_id(self, wife_id):
        """sets wife ID"""
        self.wife_id = wife_id

    def set_marriage_divorce_date(self, date):
        """
        sets marriage and divorce date (if any)
        """
        if not self.is_divorced:
            self.married = datetime.datetime.strptime(date, '%d %b %Y').date()
            self.is_divorced = True
        else:
            self.divorced = datetime.datetime.strptime(date, '%d %b %Y').date()
            self.is_divorced = False

    def set_child(self, child):
        """sets child"""
        self.children.add(child)

    def info_family(self):
        """ returns family info in the form of list"""
        if self.children == set():
            self.children = "NA"
        return list((self.family, self.married, self.divorced, self.husband_id, self.husband_name, self.wife_id,
                     self.wife_name, self.children,))


class Repository:
    def __init__(self, path: str) -> None:
        # self._path: str = path
        self._path: str = path
        self.individual: Dict[str, Individual] = dict()
        self.family: Dict[str, Family] = dict()
        # self.family = defaultdict(str)
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
                for num, line in enumerate(fp, 1):
                    output_line_list: List = line.strip("\n").split(" ", 2)
                    if any(item in output_line_list for item in list(tag_dict.keys())):
                        item = [item for item in output_line_list if item in list(tag_dict.keys())]
                        if output_line_list[1] not in tag_dict.keys():
                            index = output_line_list.index(item[0])
                            output_line_list[index], output_line_list[1] = output_line_list[1], output_line_list[index]
                            if len(output_line_list) > 2 and str(output_line_list[0]) == str(tag_dict[output_line_list[1]]):
                                yield output_line_list[1], output_line_list[2], num
                        else:
                            if len(output_line_list) > 2 and str(output_line_list[0]) == str(tag_dict[output_line_list[1]]):
                                yield output_line_list[1], output_line_list[2], num

    def _read_ged(self) -> None:
        """
        set values after reading file
        """
        id = ""
        fam_id = ""
        indi_flag = False

        for tag, arg, line_num in self._validate_gedcom():
            if tag == "INDI" and not indi_flag:
                id = arg
                if arg not in self.individual.keys():
                    self.individual[arg] = Individual(arg)
            elif tag == "NAME" and not indi_flag:
                self.individual[id].set_name(arg, line_num)
            elif tag == "SEX" and not indi_flag:
                self.individual[id].set_gender(arg)
            elif tag == "DATE" and not indi_flag:
                self.individual[id].set_birth_death_date(arg)
            elif tag == "FAMC" and not indi_flag:
                self.individual[id].set_child(arg)
            elif tag == "FAMS" and not indi_flag:
                self.individual[id].set_spouse(arg)
            elif tag == "FAM":
                indi_flag = True
                fam_id = arg
                if arg not in self.family.keys():
                    self.family[fam_id] = Family(fam_id)
            elif tag == "HUSB":
                self.family[fam_id].set_husband_id(arg)
                self.family[fam_id].set_husband_name(self.individual[arg].get_name())
            elif tag == "WIFE":
                self.family[fam_id].set_wife_id(arg)
                self.family[fam_id].set_wife_name(self.individual[arg].get_name())
            elif tag == "CHIL":
                self.family[fam_id].set_child(arg)
            elif tag == "DATE":
                self.family[fam_id].set_marriage_divorce_date(arg)

    def individual_pretty_table(self):
        """ individual pretty table"""
        pt = PrettyTable(field_names=Individual.PT_FIELD_NAMES)
        for value in self.individual.values():
            pt.add_row(value.info_individual())
        print(pt)

    def family_pretty_table(self):
        """Family pretty table"""
        pt = PrettyTable(field_names=Family.PT_FIELD_NAMES)
        for value in self.family.values():
            pt.add_row(value.info_family())
        print(pt)


if __name__ == '__main__':
    """ main file """
    sys.stdout = Logger()
    indi_repo: Repository = Repository("ssw555_input_file.ged")# change path where you gedcomfile is present
    indi_repo.individual_pretty_table()
    indi_repo.family_pretty_table()

    for item in recent_births(indi_repo.individual):
        print(f"US_35: {item}")

    for item in us_25(indi_repo.individual, indi_repo.family):
        print(f"US_25: {item}")

    for item in US_28(indi_repo):
        print(f"US_28: Age {item}")

    for item in US_29(indi_repo):
        print(f"US_29: {item} is deceased individual")

    for item in US_11(indi_repo):
        print(f"US_11: {item}")

    for item in US_33(indi_repo):
        print(f"US_33: {item}")

    for item in US_07(indi_repo.individual):
        print(f"US_07: {item} age is greater than 150 years")

    for item in US_06(indi_repo.individual, indi_repo.family):
        print(f"{item}")

    for item in us01(indi_repo.individual, indi_repo.family):
        print(item)

    for item in us04(indi_repo.family):
        print(item)

    for key, value in US_17(indi_repo.family.values()).items():
        print(f"US_17: Parents married to their children: {key} and {value}.")

    for key, value in US_23(indi_repo.individual).items():
        print(f"US_23: Multiple individuals with name {key} born on {value} exists.")

    for item in US_13(indi_repo.family, indi_repo.individual):
        print(f"US13: {item}")

    for item in US_18(indi_repo.family, indi_repo.individual):
        print(f"US18: {item}")

    for item in us_36(indi_repo.individual):
        print(f"US36: {item}")

    print(f"US32: {us_32(indi_repo.individual)}")
