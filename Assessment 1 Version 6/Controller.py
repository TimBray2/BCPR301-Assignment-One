# Written By Tim Bray
import View
from Db import Database
from Entry import FileEntry
from validate import CheckInput
from pprint import pprint


class Controller:

    def __init__(self):
        self.database_flag = False
        self.tempInput = [False, "No data has been loaded"]
        self.check_input = CheckInput()
        self.stored_data = "Data has not been stored yet"
        self.washedInput = []
        self.db = Database()
        self.db.connect()
        self.myView = View.CmdView()
        self.file_entry = FileEntry()
        self.load_location = ""

    def save(self):
        if self.washedInput == []:
            print("No data has been loaded and validated.\nPlease load and validate data before saving")
        elif self.washedInput[0]:
            self.stored_data = []
            print("The following data has been stored")
            for row in range(1, len(self.washedInput)):
                self.stored_data.append(self.washedInput[row])
                print(self.washedInput[row])
        else:
            print("\nData needs to be loaded before saving")

    def load(self, location):
        if location == "file":
            self.load_location = "file"
            directory = input("Where is the directory of the file needed? ")
            self.file_entry.get_input(directory)
            self.loaded_input = self.file_entry.get_data()
            print("Loaded from file")
        elif location == "database":
            self.load_location = "database"
            if self.database_flag == False:
                self.db.create_database()
                self.database_flag = True
            self.loaded_input = self.db.load_database()
            print("Loaded from database")
        else:
            print("Please select to load from 'database' or 'file'")

    def display(self, type):
        if type == "unchecked":
            for row in self.loaded_input:
                pprint(row)
            print("Unchecked data has been displayed")
        elif type == "stored":
            if not isinstance(self.stored_data, str):
                for row in range(len(self.stored_data)):
                    pprint(self.stored_data[row])
            else:
                pprint(self.stored_data)
            print("Stored data has been displayed")
        else:
            print("Please select to display the data that is 'unchecked', or 'stored'")

    def validate(self):
        self.washedInput = self.check_input.check_data(self.loaded_input, self.load_location)
        print("Entry data is checked")

    def close_database(self):
        Database.close_database(Database)

    def create_database(self):
        Database.create_database(Database)
