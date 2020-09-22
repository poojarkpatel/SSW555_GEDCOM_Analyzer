import datetime
import math
from prettytable import PrettyTable


def gedcomReader():
    """Function reads a GEDCOM file and provides an output with validity of each line"""
    filename = "C:\\Users\\varun\\Classwork\\3.Fall_2020\\SSW 555\\Project_Submissions\\ssw555_input_file.GED"  # User input for file name
    try:
        fp = open(filename, "r")  # to read file
    except FileNotFoundError:
        raise FileNotFoundError
    with fp:
        indexGedcom = {'0': ["INDI", "FAM", "HEAD", "TRLR", "NOTE"],
                       '1': ["NAME", "SEX", "BIRT", "DEAT", "FAMC", "FAMS", "MARR", "HUSB", "WIFE", "CHIL",
                             "DIV"], '2': ["DATE"]}  # dictionary to story the rules for the level with respect to tag
        for line in fp:
            refBlock = line.strip("\n").split(" ",
                                              2)  # Splitting each line into three and creating a list of three values
            if refBlock[0] == '0':
                """For level 0 values"""
                if len(refBlock) == 3 and refBlock[2] in indexGedcom['0']:
                    """to check for line with tag on the end"""
                    refBlock[2], refBlock[1] = refBlock[1], refBlock[
                        2]  # swaps arguments and tags for the given condition
                if refBlock[1] in indexGedcom['0']:
                    """For valid code"""
                    refBlock.insert(2, "Y")
                else:
                    """for invalid code"""
                    refBlock.insert(2, "N")

            elif refBlock[0] == '1':
                """For level 1 values"""
                if refBlock[1] in indexGedcom['1']:
                    """For valid code"""
                    refBlock.insert(2, "Y")
                else:
                    """for invalid code"""
                    refBlock.insert(2, "N")

            elif refBlock[0] == '2':
                """For level 2 values"""
                if refBlock[1] in indexGedcom['2']:
                    """For valid code"""
                    refBlock.insert(2, "Y")
                else:
                    """for invalid code"""
                    refBlock.insert(2, "N")

            yield '|'.join(refBlock)  # represent the output in the required format


checklist = dict()


def gedcomFileAnalyser():
    indiID = ""
    indiName = ""
    indiGender = ""
    indiAge = ""
    indiBirth = ""
    indiDeath = ""
    alivedeath = False  # indicator for dead individual
    famC = set()
    famS = set()
    for value in gedcomReader():
        line = value.split("|")

        if line[2] == 'Y':

            if line[1] == 'INDI':
                indiID = line[3]  # for individual code
                alivedeath = False  # indicator reset for individual
                indiDeath = ""  # reset indiDeath value
                famS = set()  # reset the FAMS value
                famC = set()  # reset the FAMC value
            elif line[1] == 'NAME':
                indiName = line[3]  # adds the name for individual code
            elif line[1] == 'SEX':
                indiGender = line[3]  # adds the gender for individual code
            elif line[1] == 'DATE':
                if not alivedeath:  # for birthdate
                    indiBirth = datetime.datetime.strptime(line[3], '%d %b %Y').date()
                    today = datetime.date.today()  # todays date
                    indiAge = today - indiBirth  # age today
                    indiAge = math.floor(indiAge.days / 365)  # final age
                    indiDeath = 'NA'  # Add not applicable to death value
                    alivedeath = True  # setting the alivedeath as true to check for another date which is deathdate
                else:
                    indiDeath = datetime.datetime.strptime(line[3], '%d %b %Y').date()  # death date for the individual
                    indiAge = indiDeath - indiBirth  # obtaining birthday for a deceased individual
                    indiAge = math.floor(indiAge.days / 365)  # final age
                    alivedeath = False  # resetting code to default value
            elif line[1] == 'FAMC':
                famC.add(line[3])  # adding FAMC value to its set
            elif line[1] == 'FAMS':
                famS.add(line[3])  # adding FAMS value to its set

            if len(famC) == 0:
                # for no child
                checklist[indiID] = [indiName, indiGender, indiBirth, indiAge, alivedeath, indiDeath, 'NA', famS]
            elif len(famS) == 0:
                # for no spouse
                checklist[indiID] = [indiName, indiGender, indiBirth, indiAge, alivedeath, indiDeath, famC, 'NA']
            elif len(famC) == 0 and len(famS) == 0:
                # for no child and spouse
                checklist[indiID] = [indiName, indiGender, indiBirth, indiAge, alivedeath, indiDeath, "NA", "NA"]
            else:
                # for child and spouse
                checklist[indiID] = [indiName, indiGender, indiBirth, indiAge, alivedeath, indiDeath, famC, famS]

    pt = PrettyTable(['Id', 'Name', 'Gender', 'Birthday', 'Age', 'Alive', 'Deathdate', 'Child', 'Spouse'])
    for key, val in checklist.items():
        #  for the individual pretty table
        if key != "":
            pt.add_row([key, val[0], val[1], val[2], val[3], val[4], val[5], val[6], val[7]])
    yield pt


def gedcomFamilies():
    famID = ''
    famMar = 'NA'  # default mmarriage date
    famDiv = 'NA'  # default divorce date
    husbID = ''
    husbName = ''
    wifeID = ''
    wifeName = ''
    familyList = dict()
    famChild = set()
    ifDiv = False  # tag to check if divorce in family code
    for value in gedcomReader():
        line = value.split("|")  # adding the value read to a list

        if line[1] == 'FAM':
            famID = line[3]  # for family code
            famChild = set() # set family child code as default
            famMar = 'NA'  # resetting marriage date to default
            famDiv = 'NA'  # resetting divorce date to default
            wifeID = 'NA'  # resetting wifeID to default
            wifeName = 'NA'  # resetting wife name value to default
            husbID = 'NA'  # resetting husbID to default
            husbName = 'NA'  # resetting husband name value to default
            ifDiv = False
        elif line[1] == 'DATE':
            if not ifDiv:
                famMar = datetime.datetime.strptime(line[3], '%d %b %Y').date()  # for marriage date
                ifDiv = True  # convert div tag to true to check for divorce date if present
            else:
                famDiv = datetime.datetime.strptime(line[3], '%d %b %Y').date()  # for divorce date
                ifDiv = False  # resetting the tag to check for divorce for the next familyID
        elif line[1] == 'HUSB':
            husbID = line[3]  # getting husband ID
            husbName = checklist[husbID][0]  # getting husband name from the individual table via husbID
        elif line[1] == 'WIFE':
            wifeID = line[3]  # getting wife ID
            wifeName = checklist[wifeID][0]  # getting wife name from the individual table via wifeID
        elif line[1] == 'CHIL':
            famChild.add(line[3])  # adding the child to the children set

        if (len(famChild) != 0):
            # for family with no children
            familyList[famID] = [famMar, famDiv, husbID, husbName, wifeID, wifeName, famChild]
        else:
            # for family with children
            familyList[famID] = [famMar, famDiv, husbID, husbName, wifeID, wifeName, 'NA']

    pt = PrettyTable(['ID', 'Married', 'Divorced', 'Husband ID', 'Husband Name', 'Wife ID', 'Wife Name', 'Children'])
    for key, val in familyList.items():
        # for family pretty table
        if key != "":
            pt.add_row([key, val[0], val[1], val[2], val[3], val[4], val[5], val[6]])
    yield pt


for i in gedcomFileAnalyser():
    print(i)
for j in gedcomFamilies():
    print(j)
