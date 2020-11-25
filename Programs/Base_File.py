""" File that runs all the user stories and prints their results. """
import sys

from Programs.Logger import Logger
from Programs.Repository import Repository

# Importing all the user stories.
from UserStories.US_01 import US_01
from UserStories.US_2_3 import US_2, US_3
from UserStories.US_04 import US_04
from UserStories.US_05 import US_05
from UserStories.US_06 import US_06
from UserStories.US_07 import US_07
from UserStories.US_08 import US_08
from UserStories.US_11 import US_11
from UserStories.US_13 import US_13
from UserStories.US_17 import US_17
from UserStories.US_18 import US_18
from UserStories.US_20 import US_20
from UserStories.US_23 import US_23
from UserStories.US_24 import US_24
from UserStories.US_25 import US_25
from UserStories.US_28 import US_28
from UserStories.US_29 import US_29
from UserStories.US_33 import US_33
from UserStories.US_35 import US_35
from UserStories.US_15 import US_15
from UserStories.US_16 import US_16
from UserStories.US_21 import US_21
from UserStories.US_22 import US_22
from UserStories.US_43 import US_43
from UserStories.US_44 import US_44



def main():
    """ Function that runs all the user stories and prints their results. """
    sys.stdout = Logger()
    # Creating an object of class Repository that will contains both individual and family dictionaries.
    # Pass the path of your GEDCOM file as a parameter below.
    repository = Repository("../GedcomFiles/SSW_555_updatedwithUS_2_3.ged")
    individual = repository.get_individual()
    family = repository.get_family()

    # Prints individual pretty table.
    repository.individual_pretty_table()
    # Prints family pretty table.
    repository.family_pretty_table()

    for item in US_01(individual, family):
        print(item)

    for item in US_2(individual, family):
        print(item)

    for item in US_3(individual):
        print(item)

    for item in US_04(family):
        print(item)

    for item in US_06(individual, family):
        print(f"{item}")

    for item in US_07(individual):
        print(f"US_07: {item} age is greater than 150 years")

    for item in US_11(repository):
        print(f"US_11: {item}")

    for item in US_13(family, individual):
        print(f"US13: {item}")

    for key, value in US_17(family.values()).items():
        print(f"US_17: Parents married to their children: {key} and {value}.")

    for item in US_18(family, individual):
        print(f"US18: {item}")

    for item in US_20(family, individual):
        print(f"US_20: {item}")

    for key, value in US_23(individual).items():
        print(f"US_23: Multiple individuals with name {key} born on {value} exists.")

    for item in US_24(family):
        print(f"US_24: {item}")

    for item in US_25(individual, family):
        print(f"US_25: {item}")

    for item in US_28(repository):
        print(f"US_28: Age {item}")

    for item in US_29(repository):
        print(f"US_29: {item} is deceased individual")

    for item in US_33(repository):
        print(f"US_33: {item}")

    for item in US_35(individual):
        print(f"US_35: {item}")

    for item in US_15(family):
        print(f"{item} ")

    for item in US_16(individual, family):
        print(f"{item}")

    for item in US_21(individual, family):
        print(item)

    for item in US_22(individual, family):
        print(item)

    for item in US_43(individual, family):
        print("US_43:", item)

    for item in US_44(individual):
        print("US_44:", item)

    """
    for individual_id, individual_information in individual.items():
        print(individual_id, individual_information.get_line_numbers())

    for family_id, family_information in family.items():
        print(family_id, family_information.get_line_numbers())
    """


if __name__ == '__main__':
    """ Calls main method. """
    main()
