"""
Name: Varun Mark Mullins
CWID: 10456027
Project Assignment 2

Assignment to check the validity of the lines on the GEDCOM file and assign validity codes to each line, and print them
along with the input line and the output line in the required validity checking format.

"""


def gedcomReader():
    """Function reads a GEDCOM file and provides an output with validity of each line"""
    filename = input("Enter you Filename/FilePath: ")  # User input for file name
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

            yield f"--> {line.strip()} \n<-- {'|'.join(refBlock)}"  # represent the output in the required format


def main():
    for value in gedcomReader():
        print(value)


main()

#C:\Users\varun\Classwork\3.Fall_2020\SSW 555\Project_Submissions\Project01_VarunMullins.GED