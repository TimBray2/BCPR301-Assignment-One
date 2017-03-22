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
            datetime.datetime(split_data[2], split_data[1], split_data[0])
            is_valid = True
        except ValueError:
            is_valid = False
        return is_valid

    @staticmethod
    def split_item(split_value, item):
        new_item = re.split(split_value, item)
        return new_item

    @staticmethod
    def check_age(age, dob):
        today = datetime.date.today()
        birthday = today.year - int(dob[2]) - ((today.month, today.day) < (int(dob[1]), int(dob[0])))
        if int(birthday) == int(age):
            return True
        else:
            return False

    @staticmethod
    def reg_exp_checker(regexp, string):
        if re.search(regexp, string):
            return True
        else:
            return False

    def check_data(self, data):
        self.washed_data = [True]
        for row in data:
            if len(row) == 7:
                count = 0
                for item in row:
                    if count == 6:
                        split_data = self.split_item("-", item)
                        split_data = list(map(int, split_data))
                        if len(split_data) < 2:
                            self.check = False
                        else:
                            if self.date_check(split_data):
                                self.check = self.check_age(row[2], split_data)
                    else:
                        self.check = self.reg_exp_checker(self.regexChecklist[count], str(item))
                    if not self.check:
                        print(str(item) + " = " + str(self.check))
                        print("\nRow: " + str(row) + " has invalid data. "
                                                     "\nThis row will not be stored due to business policies")
                        self.row_check = False
                    count += 1
                if self.row_check:
                    self.washed_data.append(row)
                self.row_check = True
            else:
                print("\nRow: " + str(row) + " does not have all 7 fields filled out. "
                                             "\nThis row will not be stored due to business policies")
        return self.washed_data
