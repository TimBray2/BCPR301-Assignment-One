# Written By Tim Bray
import datetime
import re
from Entry import FileEntry


class CheckInput:
    def __init__(self):
        self.regexChecklist = [
            "[A-Z][0-9]{3}", "(M|F)", "[0-9]{2}", "[0-9]{3}", "(Normal|Overweight|Obesity|Underweight)",
            "[0-9]{2,3}", "[1-31]-[1-12]-[0-9]{4}"]
        self.check = bool
        self.washed_data = []
        self.row_check = True

    @staticmethod
    def date_check(split_data):
        try:
            datetime.datetime(split_data[0], split_data[1], split_data[2])
            is_valid = True
        except ValueError:
            is_valid = False
        return is_valid

    @staticmethod
    def split_item(split_value, item):
        new_item = re.split(split_value, item)
        return new_item

    @staticmethod
    def reg_exp_checker(regexp, string):
        if re.search(regexp, string):
            return True
        else:
            return False

    def check_data(self, data):
        self.washed_data = [True]
        for row in data:
            count = 0
            for item in row:
                if count == 6:
                    split_data = self.split_item("-", item)
                    if len(split_data) < 2:
                        self.check = False
                else:
                    self.check = self.reg_exp_checker(self.regexChecklist[count], str(item))
                if not self.check:
                    print(str(item) + " = " + str(self.check))
                    print("Row: " + str(row) + " has invalid data. \nThis row will not be stored due to business policies")
                    self.row_check = False
                count += 1
            if self.row_check:
                self.washed_data.append(row)
            self.row_check = True
        return self.washed_data
