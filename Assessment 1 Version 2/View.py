# Written Tim Bray
from cmd import Cmd
from Db import Database
from Validate import ValidateData
from Entry import FileEntry
from CheckEntry import CheckInput


class DataController(Cmd):

    def __init__(self):
        Cmd.__init__(self)
        self.prompt = ">>> "
        self.tempInput = ""
        self.check_input = CheckInput()
        # db = Database()

    # Configure save input
    @staticmethod
    def do_save(self, line):
        print("Saved")

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
            # check_input = CheckInput()
            self.check_input.check_data(self.tempInput)
            print("Entry data is checked")
        elif location == "database":
            self.tempInput = db.load_database()
            print("Loaded from database")
            # check_input = CheckInput()
            self.check_input.check_data(self.tempInput)
            print("Entry data is checked")
        else:
            print("Please select to load from 'database' or 'file'")

    # @staticmethod
    # def check_input(self):
    #     check_input = CheckInput()
    #     check_input.check_data(self.tempInput)

    @staticmethod
    def help_load():
        print('\n'.join(['load [location] (file, database)', 'Load from the database or file']))

    # Configure validate input
    def do_validate(self, line):
        ValidateData.check_input(self, )

    @staticmethod
    def help_validate():
        print('\n'.join(['validate', 'Validates all loaded data']))

    # Configure display input
    @staticmethod
    def do_display(self, type):
        if type == "file":
            fileEntry.display_file_entry()
            print("Loaded from file")
        elif type == "database":
            db.display_database_entry()
            print("Displayed data from database")
        elif type == "stored":
            print("stored")
        else:
            print("Please select to load from 'database', 'file' or 'stored'")

    @staticmethod
    def help_display():
        print('\n'.join(['display [type] (file, database, stored)', 'Display all the stored data']))

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

if __name__ == "__main__":
    fileEntry = FileEntry()
    db = Database()
    DataController().cmdloop()