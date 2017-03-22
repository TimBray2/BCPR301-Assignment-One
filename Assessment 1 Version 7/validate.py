# Written By Tim Bray

"""
>>> check = CheckInput()
>>> check.date_check([35, 10, 2020])
False
>>> check = CheckInput()
>>> check.split_item("18-10-1996", "-")
[18, 10, 1996]

>>> check = CheckInput()
>>> check.check_age(32, "18-10-1996")
False

>>> check = CheckInput()
>>> check.check_data()
No data has been loaded and validated.\nPlease load and validate data before saving


"""
import datetime
import re


class CheckInput:
    def __init__(self):
        self.regexChecklist = [
            "[A-Z][0-9]{3}", "(M|F)", "[0-9]{2}", "[0-9]{3}", "(Normal|Overweight|Obesity|Underweight)",
            "[0-9]{2,3}"]
        self.check = bool
        self.washed_data = []
        self.row_check = True

    @staticmethod
    def date_check(split_data):
        try:
            datetime.datetime(split_data[2], split_data[1], split_data[0])
            today = datetime.date.today()
            if split_data[2] > int(today.year):
                is_valid = False
            else:
                is_valid = True
        except ValueError:
            is_valid = False
        return is_valid

    @staticmethod
    def split_item(split_value, item):
        try:
            new_item = re.split(split_value, item)
            return new_item
        except ValueError:
            return False

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

    @staticmethod
    def rearrange(split_data):
        return [split_data[2], split_data[1], split_data[0]]

    def check_data(self, data, location):
        self.washed_data = [True]
        for row in data:
            if len(row) == 7:
                self.checkAge = True
                count = 0
                for item in row:
                    if count == 6:
                        split_data = self.split_item("-", item)
                        if len(split_data) < 2:
                            self.check = False
                        else:
                            split_data = list(map(int, split_data))
                            if location == "database":
                                split_data = self.rearrange(split_data)
                            if self.date_check(split_data):
                                self.check = self.check_age(row[2], split_data)
                                self.checkAge = False
                            else:
                                self.check = False
                    else:
                        self.check = self.reg_exp_checker(self.regexChecklist[count], str(item))
                    if not self.checkAge:
                        print("The date of birth and age do not match up --> " + str(self.check))
                        print("Row: " + str(row) + " has invalid data. "
                                                   "\nThis row will not be stored due to business policies\n")
                    elif not self.check:
                        print(str(item) + " is invalid --> " + str(self.check))
                        print("Row: " + str(row) + " has invalid data. "
                                                     "\nThis row will not be stored due to business policies\n")
                        self.row_check = False
                    count += 1
                if self.row_check:
                    self.washed_data.append(row)
                self.row_check = True
            else:
                print("Row: " + str(row) + " does not have the correct number of fields filled out. "
                                             "\nThis row will not be stored due to business policies\n")
        return self.washed_data
