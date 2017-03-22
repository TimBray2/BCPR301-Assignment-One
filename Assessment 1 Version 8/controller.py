# Written By Tim Bray
import cmd_view
from database_view import Database
from file_entry_view import FileEntry
from validate import CheckInput


class Controller:

    def __init__(self, cmd_view):
        self.database_flag = False
        self.tempInput = [False, "No data has been loaded"]
        self.check_input = CheckInput()
        self.stored_data = "Data has not been stored yet"
        self.washedInput = []
        self.load_location = ""
        self.file_entry = FileEntry()
        self.db = Database()
        self.__cmd_view = cmd_view

    def go(self, controller):
        self.__cmd_view.set_controller(controller)
        from sys import argv
        if len(argv) > 1:
            self.__cmd_view.onecmd(' '.join(argv[1:]))
        else:
            self.__cmd_view.cmdloop()


    def save(self, line):
        try:
            if len(line) == 0:
                if self.washedInput == []:
                    print("No data has been loaded and validated.\nPlease load and validate data before saving")
                elif self.washedInput[0]:
                    self.stored_data = []
                    print("The following data has been stored")
                    for row in range(1, len(self.washedInput)):
                        self.stored_data.append(self.washedInput[row])
                else:
                    print("\nData needs to be loaded before saving")
            else:
                print("Please do not enter any extra input after 'validate'")
        except AttributeError:
            print("Please load data before validating")

    def load(self, location):
        try:
            destination = location.split(" ")
            if destination[0] == "file":
                self.load_location = "file"
                directory = destination[1]
                self.file_entry.get_input(directory)
                self.loaded_input = self.file_entry.get_data()
                print("Loaded from file")
            elif len(destination) == 1 and destination[0] != "file":
                if destination[0] == "database":
                    self.load_location = "database"
                    if self.database_flag == False:
                        self.db.create_database()
                        self.database_flag = True
                    self.loaded_input = self.db.load_database()
                    print("Loaded from database")
                else:
                    print("Please select to load from 'database' or 'file [location]'")
            else:
                print("Please select to load from 'database' or 'file [location]'")
        except IndexError:
            print("Please select to load from 'database' or 'file [location]'")
        except FileNotFoundError:
            print("Please select a valid file location")

    def display(self, type):
        if type == "unchecked":
            for row in self.loaded_input:
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

    def validate(self, line):
        try:
            if len(line) == 0:
                self.washedInput = self.check_input.check_data(self.loaded_input, self.load_location)
                print("Entry data is checked")
            else:
                print("Please do not enter any extra input after 'validate'")
        except AttributeError:
            print("Please load data before validating")

    def close_database(self, line):
        Database.close_database(Database)

    def create_database(self, line):
        Database.create_database(Database)


if __name__ == "__main__":
    control = Controller(cmd_view.CmdView())
    control.go(control)