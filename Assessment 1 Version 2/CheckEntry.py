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
        for row in data:
            count = 0
            for item in row:
                if count == 9:
                    split_data = self.split_item("-", item)
                    # print(split_data)
                    if len(split_data) < 2:
                        print(str(split_data) + "\nInvalid Data")
                    else:
                        split_data = list(map(int, split_data))
                        print(str(split_data) + " = " + str(self.date_check(split_data)))
                else:
                    self.check = self.reg_exp_checker(self.regexChecklist[count], str(item))
                if not self.check:
                    print(str(item) + " = " + str(self.check))
                count += 1
