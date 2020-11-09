""" File that contains all the information related to a particular family. """
import datetime

class Family:
    """ Class that contains all the information related to a particular family. """
    PT_FIELD_NAMES = ['Id', 'Married', 'Divorced', 'Husband ID', 'Husband Name', 'Wife ID', 'Wife Name', 'Children']

    def __init__(self, family, line_number) -> None:
        """ Function that initializes class variables family_id, marriage_date, divorce_date, husband_id, husband_name, wife_name, wife_id, is_divorced, children and line_number. """
        self._family_id = family
        self._marriage_date = "NA"
        self._divorce_date = "NA"
        self._husband_id = ""
        self._husband_name = ""
        self._wife_name = ""
        self._wife_id = ""
        self._is_divorced = False
        self._children = set()
        self._line_numbers = {'date': {'marriage': 'NA', 'divorce': 'NA'}, 'family_id': line_number}

    def set_husband_name(self, husband_name):
        """ Function that sets the name of husband in family. """
        self._husband_name = husband_name

    def set_wife_name(self, wife_name):
        """ Function that sets the name of wife in family. """
        self._wife_name = wife_name

    def set_husband_id(self, husband_id, line_number):
        """ Function that sets husband ID. """
        self._husband_id = husband_id
        self._line_numbers['husband_id'] = line_number

    def set_wife_id(self, wife_id, line_number):
        """ Function that sets wife ID. """
        self._wife_id = wife_id
        self._line_numbers['wife_id'] = line_number

    def set_marriage_divorce_date(self, date, line_number):
        """ Function that sets marriage and divorce dates (if any). """
        words = date.split()

        if not self._is_divorced:
            if len(words) < 3:
                self._marriage_date = datetime.datetime.strptime(words[len(words) - 1], '%Y').date()
            else:
                self._marriage_date = datetime.datetime.strptime(date, '%d %b %Y').date()

            self._is_divorced = True
            self._line_numbers['date']['marriage'] = line_number
        else:
            if len(words) < 3:
                self._divorce_date = datetime.datetime.strptime(words[len(words) - 1], '%Y').date()
            else:
                self._divorce_date = datetime.datetime.strptime(date, '%d %b %Y').date()

            self._is_divorced = False
            self._line_numbers['date']['divorce'] = line_number

    def set_child(self, child):
        """ Function that adds child in the children set. """
        self._children.add(child)

    def get_line_numbers(self):
        return self._line_numbers

    def info_family(self):
        """ Function that returns family info in the form of list. """
        if self._children == set():
            self._children = "NA"
        return list((self._family_id, self._marriage_date, self._divorce_date, self._husband_id, self._husband_name, self._wife_id, self._wife_name, self._children,))
