# Written By Tim Bray
import datetime
import cmd_view
import graph_maker
from database_view import Database
from file_entry_view import FileEntry
from validate import CheckInput
from sys import argv


class Controller:
    def __init__(self, view):
        self.__database_flag = False
        self.__temp_input = [False, "No data has been loaded"]
        self.__check_input = CheckInput()
        self.__stored_data = "Data has not been stored yet"
        self.__washed_input = []
        self.__load_location = ""
        self.__file_entry = FileEntry()
        self.__db = Database()
        self.__cmd_view = view
        self.__loaded_input = None

    def _go(self, controller):
        self.__cmd_view.set_controller(controller)
        if len(argv) > 1:
            self.__cmd_view.onecmd(' '.join(argv[1:]))
        self.__cmd_view.cmdloop()

    def _save(self, line):
        try:
            if len(line) == 0:
                if not self.__washed_input:
                    print("No data has been loaded and validated.\nPlease load and validate data before saving")
                elif self.__washed_input[0]:
                    self.__stored_data = []
                    print("The following data has been stored")
                    for row in range(1, len(self.__washed_input)):
                        self.__stored_data.append(self.__washed_input[row])
                else:
                    print("\nData needs to be loaded before saving")
            else:
                print("Please do not enter any extra input after 'save'")
        except AttributeError:
            print("Please load data before saving")

    def _load(self, location):
        try:
            destination = location.split(" ")
            if destination[0] == "file":
                self.__load_location = "file"
                directory = destination[1]
                self.__file_entry.get_input(directory)
                self.__loaded_input = self.__file_entry.get_data()
                print("Loaded from file")
            elif len(destination) == 1 and destination[0] != "file":
                if destination[0] == "database":
                    self.__load_location = "database"
                    if not self.__database_flag:
                        self.__db._create_database()
                        self.__database_flag = True
                    self.__loaded_input = self.__db._load_database()
                    print("Loaded from database")
                else:
                    print("Please select to load from 'database' or 'file [location]'")
            else:
                print("Please select to load from 'database' or 'file [location]'")
        except IndexError:
            print("Please select to load from 'database' or 'file [location]'")
        except FileNotFoundError:
            print("Please select a valid file location")

    def _display(self, format):
        if format == "unchecked":
            for row in self.__loaded_input:
                print(row)
            print("Unchecked data has been displayed")
        elif format == "stored":
            if not isinstance(self.__stored_data, str):
                for row in range(len(self.__stored_data)):
                    print(self.__stored_data[row])
            else:
                print(self.__stored_data)
            print("Stored data has been displayed")
        elif format == "graph":
            if not isinstance(self.__stored_data, str):
                graph_maker.create_graph(self.__stored_data)
                print("Graph has been created in the browser.")
            else:
                print("Please validate and saved data before creating a graph.")
        else:
            print("Please select to display the data that is 'unchecked', or 'stored'")

    def _validate(self, line):
        try:
            if len(line) == 0:
                self.__washed_input = self.__check_input._check_data(self.__loaded_input, self.__load_location)
                print("Entry data is checked")
            else:
                print("Please do not enter any extra input after 'validate'")
        except TypeError:
            print("Please load data before validating")

    @staticmethod
    def _welcome(line):
        if len(line) == 0:
            today = datetime.date.today()
            print("Welcome to the program.\nThe date is " + str(today))
        else:
            print("Please do not enter any extra input after 'welcome'")


if __name__ == "__main__":
    control = Controller(cmd_view.CmdView())
    control._go(control)
