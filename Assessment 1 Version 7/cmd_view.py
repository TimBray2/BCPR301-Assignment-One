# Written Tim Bray
from cmd import Cmd
from controller import Controller


class CmdView(Cmd):

    def __init__(self):
        Cmd.__init__(self)
        self.prompt = ">>> "

    # Configure save input
    def do_save(self, line):
        con.save()

    @staticmethod
    def help_save():
        print('\n'.join(['save', 'Save the imported data']))

    # Configure load input
    def do_load(self, location):
        con.load(location)

    @staticmethod
    def help_load():
        print('\n'.join(['load [location] (file, database)', 'Load from the database or file']))

    # Configure validate input
    def do_validate(self, line):
        con.validate()

    @staticmethod
    def help_validate():
        print('\n'.join(['validate', 'Validates all loaded data']))

    # Configure display input
    def do_display(self, type):
        con.display(type)

    @staticmethod
    def help_display():
        print('\n'.join(['display [type] (unchecked, stored)', 'Display all the stored data']))

    # Configure exit input
    def do_exit(self, line):
        print("Exiting.....")
        return True

    @staticmethod
    def help_exit():
        print('\n'.join(['exit', 'Exits the command line']))

    # Configure create_database input
    def do_create_database(self, line):
        con.create_database()
        print("Database created")

    @staticmethod
    def help_create_database():
        print('\n'.join(['create_database', 'Creates the database']))

con = Controller()
CmdView().cmdloop()
