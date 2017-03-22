# Written Tim Bray
import cmd
from Db import Database
from Validate import ValidateData
from Entry import FileEntry
from CheckEntry import CheckInput


class DataController(cmd.Cmd):

    # Configure save input
    def do_save(self, line):
        print("Saved")

    def help_save(self):
        print('\n'.join(['save', 'Save the imported data']))

    # Configure load input
    def do_load(self, location):
        if location == "file":
            FileEntry.get_input(self)
            self.tempInput = FileEntry.get_data(self)
            print("Loaded from file")
            CheckInput.check_data(CheckInput, self.tempInput)
            print("Entry data is checked")
        elif location == "database":
            self.tempInput = db.load_database()
            print("Loaded from database")
            CheckInput.check_data(CheckInput, self.tempInput)
            print("Entry data is checked")
        else:
            print("Please select to load from 'database' or 'file'")

    def help_load(self):
        print('\n'.join(['load [location] (file, database)', 'Load from the database or file']))

    # Configure validate input
    def do_validate(self, line):
        ValidateData.check_input(self, )

    def help_validate(self):
        print('\n'.join(['validate', 'Validates all loaded data']))

    # Configure display input
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

    def help_display(self):
        print('\n'.join(['display [type] (file, database, stored)', 'Display all the stored data']))

    # Configure exit input
    def do_exit(self, line):
        return True

    def help_exit(self):
        print('\n'.join(['exit', 'Exits the command line']))

    # Configure create_database input
    def do_create_database(self, line):
        db.create_database()
        print("Database created")

    def help_create_database(self):
        print('\n'.join(['create_database', 'Creates the database']))

fileEntry = FileEntry()
db = Database()
DataController().cmdloop()