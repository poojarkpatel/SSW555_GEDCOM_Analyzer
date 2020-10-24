""" File that logs the results of all the user stories in 'Output.txt' file. """
import sys

class Logger(object):
    """ Class that logs the results of all the user stories in 'Output.txt' file. """
    def __init__(self):
        """ Function that opens/creates the file 'Output.txt' in current working directory. """
        self.terminal = sys.stdout
        self.log = open("Output.txt", "w")

    def write(self, message):
        """ Function that updates 'Output.txt' file. """
        self.terminal.write(message)
        self.log.write(message)

    def flush(self):
        """ Function that flushes the logging stream. """
        pass
