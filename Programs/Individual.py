""" File that stores all the information related to a particular of individual. """
import datetime
import math

class Individual:
    """ Class that stores all the information related to a particular of individual. """
    PT_FIELD_NAMES = ['Id', 'Name', 'Gender', 'Birthday', 'Age', 'Alive', 'Deathdate', 'Child', 'Spouse']

    def __init__(self, individual_id, line_number) -> None:
        """ Function that initializes variables individual_id, name, gender, birth_date, age, is_alive, death_date, famC and famS. """
        self._individual_id = individual_id
        self._name = ""
        self._gender = ""
        self._birth_date = "NA"
        self._age = 0
        self._is_alive = False
        self._death_date = "NA"
        self._famC = set()
        self._famS = set()
        self._line_numbers = {'date': {'birth': 'NA', 'death': 'NA'}, 'individual_id': line_number}

    def set_name(self, name, line_number):
        """ Function that sets the name of individual. """
        self._name = name
        self._line_numbers['individual_name'] = line_number

    def get_name(self) -> str:
        """ Function that returns the name of individual. """
        return self._name

    def set_gender(self, gender, line_number):
        """ Function that sets the gender of individual. """
        self._gender = gender
        self._line_numbers['gender'] = line_number

    def set_birth_death_date(self, date, line_number):
        """ Function that sets the birth-date and death-date of individual. """
        words = date.split()

        if not self._is_alive:
            if len(words) < 3:
                self._birth_date = datetime.datetime.strptime(words[len(words) - 1], '%Y').date()
            else:
                self._birth_date = datetime.datetime.strptime(date, '%d %b %Y').date()
            # Today's date.
            today = datetime.date.today()
            # Current age.
            self._age = today - self._birth_date
            self._age = math.floor(self._age.days / 365)

            if self._age < 0:
                self._age = 0

            self._is_alive = True
            self._line_numbers['date']['birth'] = line_number
        else:
            if len(words) < 3:
                self._death_date = datetime.datetime.strptime(words[len(words) - 1], '%Y').date()
            else:
                self._death_date = datetime.datetime.strptime(date, '%d %b %Y').date()

            # Obtaining birthday for a deceased individual.
            self._age = self._death_date - self._birth_date
            # Setting age at which individual died.
            self._age = math.floor(self._age.days / 365)
            self._is_alive = False
            self._line_numbers['date']['death'] = line_number

    def set_child(self, child):
        """ Function that sets the id of family in which the individual is a child. """
        self._famC.add(child)

    def set_spouse(self, spouse):
        """ Function that sets the id of family in which the individual is a spouse. """
        self._famS.add(spouse)

    def get_line_numbers(self):
        return self._line_numbers

    def info_individual(self):
        """ Function that returns information of an individual in the form of list. """
        if self._famC == set():
            self._famC = "NA"

        if self._famS == set():
            self._famS = "NA"

        return list((self._individual_id, self._name, self._gender, self._birth_date, self._age, self._is_alive, self._death_date, self._famC, self._famS))
