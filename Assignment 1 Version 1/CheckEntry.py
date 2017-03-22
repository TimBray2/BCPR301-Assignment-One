# Written By Tim Bray
import datetime
import re
from Entry import FileEntry


class CheckInput:
    def __init__(self, data):
        self.regexChecklist = [
            "[A-Z][0-9]{3}", "(M|F)", "[0-9]{2}", "[0-9]{3}", "(Normal|Overweight|Obesity|Underweight)",
            "[0-9]{2,3}", "[1-31]-[1-12]-[0-9]{4}"]
        # self.entry = FileEntry()
        # self.input = self.entry.get_data()
        # self.check_data(data)
        # print(date_check(12, 10, 2017))
        print(self.reg_exp_checker(self.regexChecklist[0], "A112"))
        print("^^Regex check^^")

    def date_check(self, split_data):
        try:
            new_date = datetime.datetime(split_data[0], split_data[1], split_data[2])
            is_valid = True
        except ValueError:
            is_valid = False
        return is_valid

    def split_item(self, split_value, item):
        new_item = re.split(split_value, item)
        return new_item

    def reg_exp_checker(self, regexp, string):
        if re.search(regexp, string):
            return True
        else:
            return False

    def check_data(self, data):
        for item in data:
            count = 0;
            for data in item:
                if count == 6:
                    split_data = self.split_item(self, "-", data)
                    print(split_data)
                    if len(split_data) < 2:
                        print("Invalid Data")
                    else:
                        split_data = list(map(int, split_data))
                        print(self.date_check(self, split_data))
                count += 1;