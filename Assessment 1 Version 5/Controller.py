# Written By Tim Bray
import View
from Db import Database
from Entry import FileEntry
from CheckEntry import CheckInput


class Controller:

    def __init__(self):
        self.tempInput = [False, "\nNo data has been loaded"]
        self.check_input = CheckInput()
        self.stored_data = "\nData has not been stored yet"
        self.washedInput = []
        self.myView = View.CmdView()
        self.db = Database()

    def save(self):
        if self.washedInput == []:
            print("\nNo data has been loaded.\nPlease load data before saving")
        elif self.washedInput[0]:
            self.stored_data = []
            print("\nThe following data has been stored")
            for row in range(1, len(self.washedInput)):
                self.stored_data.append(self.washedInput[row])
                print(self.washedInput[row])
        else:
            print("\nData needs to be loaded before saving")

    def load(self, location):
        if location == "file":
            file_entry = FileEntry()
            file_entry.get_input()
            self.tempInput = file_entry.get_data()
            print("Loaded from file")
            self.washedInput = self.check_input.check_data(self.tempInput)
            print("\nEntry data is checked")
        elif location == "database":
            self.tempInput = self.db.load_database()
            print("Loaded from database")
        else:
            print("\nPlease select to load from 'database' or 'file'")

    def display(self, type):
        if type == "unchecked":
            for row in self.tempInput:
                print(row)
            print("\nUnchecked data has been displayed")
        elif type == "stored":
            if not isinstance(self.stored_data, str):
                for row in range(len(self.stored_data)):
                    print(self.stored_data[row])
            else:
                print(self.stored_data)
            print("\nStored data has been displayed")
        else:
            print("\nPlease select to display the data that is 'unchecked', or 'stored'")

    def validate(self):
        self.washedInput = self.check_input.check_data(self.tempInput)
        print("\nEntry data is checked")

    def close_database(self):
        Database.close_database(Database)


if __name__ == "__main__":
    con = Controller()
    fileEntry = FileEntry()
    db = Database()
