# Written Tim Bray
from cmd import Cmd


# noinspection PyUnusedLocal
class CmdView(Cmd):

    def __init__(self):
        Cmd.__init__(self)
        self.prompt = ">>> "
        self.__con = None

    def set_controller(self, controller):
        self.__con = controller

    # Configure save input
    def do_save(self, line):
        self.__con._save(line)

    @staticmethod
    def help_save():
        print('\n'.join(['save', 'Save the imported data']))

    # Configure load input
    def do_load(self, location):
        self.__con._load(location)

    @staticmethod
    def help_load():
        print('\n'.join(['load [location] (file, database)', 'Load from the database or file']))

    # Configure validate input
    def do_validate(self, line):
        self.__con._validate(line)

    @staticmethod
    def help_validate():
        print('\n'.join(['validate', 'Validates all loaded data']))

    # Configure display input
    def do_display(self, line):
        self.__con._display(line)

    @staticmethod
    def help_display():
        print('\n'.join(['display [type] (unchecked, stored, graph)', 'Display all the stored data']))

    # Configure exit input
    @staticmethod
    def do_exit(line):
        print("Exiting.....")
        return True

    @staticmethod
    def help_exit():
        print('\n'.join(['exit', 'Exits the command line']))

    # Configure welcome input
    def do_welcome(self, line):
        self.__con._welcome(line)

    @staticmethod
    def help_welcome():
        print('\n'.join(['welcome', 'Welcomes the user to the program']))
