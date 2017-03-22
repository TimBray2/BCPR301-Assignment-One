# Written Tim Bray
from cmd import Cmd
from Db import Database
from Validate import ValidateData
from Entry import FileEntry
from CheckEntry import CheckInput


class CmdView(Cmd):

    def __init__(self):
        Cmd.__init__(self)
        self.prompt = ">>> "
        self.tempInput = [False, "No data has been loaded"]
        self.check_input = CheckInput()
        self.stored_data = "Data has not been stored yet"
        self.washedInput = []

    # Configure save input
    def do_save(self, line):
        if (self.washedInput[0]):
            self.stored_data = []
            print("The following data has been stored")
            for row in range(1, len(self.washedInput)):
                self.stored_data.append(self.washedInput[row])
                print(self.washedInput[row])
        else:
            print("Data needs to be loaded before saving")

    @staticmethod
    def help_save():
        print('\n'.join(['save', 'Save the imported data']))

    # Configure load input
    def do_load(self, location):
        if location == "file":
            file_entry = FileEntry()
            file_entry.get_input()
            self.tempInput = file_entry.get_data()
            print("Loaded from file")
            self.washedInput = self.check_input.check_data(self.tempInput)
            print("Entry data is checked")
        elif location == "database":
            self.tempInput = db.load_database()
            print("Loaded from database")
            self.washedInput = self.check_input.check_data(self.tempInput)
            print("Entry data is checked")
        else:
            print("Please select to load from 'database' or 'file'")

    @staticmethod
    def help_load():
        print('\n'.join(['load [location] (file, database)', 'Load from the database or file']))

    # Configure validate input
    def do_validate(self, line):
        ValidateData.validate_input()

    @staticmethod
    def help_validate():
        print('\n'.join(['validate', 'Validates all loaded data']))

    # Configure display input
    def do_display(self, type):
        if type == "unchecked":
            for row in self.tempInput:
                print(row)
            print("Unchecked data has been displayed")
        elif type == "stored":
            if not isinstance(self.stored_data, str):
                for row in range(len(self.stored_data)):
                    print(self.stored_data[row])
            else:
                print(self.stored_data)
            print("Stored data has been displayed")
        else:
            print("Please select to display the data that is 'unchecked', or 'stored'")

    @staticmethod
    def help_display():
        print('\n'.join(['display [type] (unchecked, stored)', 'Display all the stored data']))

    # Configure exit input
    @staticmethod
    def do_exit(self, line):
        print("Exiting.....")
        return True

    @staticmethod
    def help_exit():
        print('\n'.join(['exit', 'Exits the command line']))

    # Configure create_database input
    @staticmethod
    def do_create_database(self, line):
        db.create_database()
        print("Database created")

    @staticmethod
    def help_create_database():
        print('\n'.join(['create_database', 'Creates the database']))

fileEntry = FileEntry()
db = Database()
CmdView().cmdloop()
