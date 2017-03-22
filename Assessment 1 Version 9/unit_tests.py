import unittest
import cmd_view
from controller import Controller
from validate import CheckInput
from contextlib import contextmanager
from io import StringIO
import sys
import datetime


class MainTests(unittest.TestCase):

    def setUp(self):
        self.__con = Controller(cmd_view)
        self.__today = datetime.date.today()

    @contextmanager
    def captured_output(self):
        new_out, new_err = StringIO(), StringIO()
        old_out, old_err = sys.stdout, sys.stderr
        try:
            sys.stdout, sys.stderr = new_out, new_err
            yield sys.stdout, sys.stderr
        finally:
            sys.stdout, sys.stderr = old_out, old_err

    def test_invalid_data_file(self):
        with self.captured_output() as (out, err):
            self.__con._load("file TestFile1.txt")
            self.__con._validate("")
        output = out.getvalue().strip()
        expected = "Loaded from file" \
                   "\n2 is invalid" \
                   "\nRow: ['I123', 'M', '2', '13', 'OverWeight', '123', '31-12-1989'] has invalid data." \
                   "\nThis row will not be stored due to business policies" \
                   "\n" \
                   "\n123I is invalid" \
                   "\nRow: ['123I', 'm', '90', '40.5', 'Underweight', '000', '15-3-1927'] has invalid data." \
                   "\nThis row will not be stored due to business policies" \
                   "\n" \
                   "\nXXD4 is invalid" \
                   "\nRow: ['XXD4', ' F', '50', '001', '', '002', '29-02-1967'] has invalid data." \
                   "\nThis row will not be stored due to business policies" \
                   "\n" \
                   "\nu258 is invalid" \
                   "\nRow: ['u258', 'F', '50', '999', 'Obesity', '999', '31-02-1967'] has invalid data." \
                   "\nThis row will not be stored due to business policies" \
                   "\n" \
                   "\nX is invalid" \
                   "\nRow: ['Q258', 'X', '50', '999', 'Normal', '.99', '1967-02-01'] has invalid data." \
                   "\nThis row will not be stored due to business policies" \
                   "\n" \
                   "\nRow: ['Q258/F/50/123/Normal/123/01-01-1967'] does not have the correct number of " \
                   "fields filled out." \
                   "\nThis row will not be stored due to business policies" \
                   "\n" \
                   "\nRow: ['Q234  F  50  123  Normal  123  01-01-1967'] does not have the correct number of " \
                   "fields filled out." \
                   "\nThis row will not be stored due to business policies" \
                   "\n" \
                   "\n  is invalid" \
                   "\nRow: [' ', ' ', ' ', ' ', ' ', ' ', ''] has invalid data." \
                   "\nThis row will not be stored due to business policies" \
                   "\n" \
                   "\nEntry data is checked"
        self.assertEqual(expected, output)

    def test_valid_data_file(self):
        with self.captured_output() as (out, err):
            self.__con._load("file validInputData.txt")
            self.__con._validate("")
        output = out.getvalue().strip()
        expected = "Loaded from file" \
                   "\nEntry data is checked"
        self.assertEqual(expected, output)

    def test_validate_function_input_1(self):
        with self.captured_output() as (out, err):
            self.__con._load("file validInputData.txt")
            self.__con._validate("file")
        output = out.getvalue().strip()
        expected = "Loaded from file" \
                   "\nPlease do not enter any extra input after 'validate'"
        self.assertEqual(expected, output)

    def test_validate_function_input_2(self):
        with self.captured_output() as (out, err):
            self.__con._validate("")
        output = out.getvalue().strip()
        expected = "Please load data before validating"
        self.assertEqual(expected, output)

    def test_save_function_input_1(self):
        with self.captured_output() as (out, err):
            self.__con._load("file validInputData.txt")
            self.__con._validate("")
            self.__con._save("")
        output = out.getvalue().strip()
        expected = "Loaded from file" \
                   "\nEntry data is checked" \
                   "\nThe following data has been stored"
        self.assertEqual(expected, output)

    def test_save_function_input_2(self):
        with self.captured_output() as (out, err):
            self.__con._load("file validInputData.txt")
            self.__con._validate("")
            self.__con._save("file")
        output = out.getvalue().strip()
        expected = "Loaded from file" \
                   "\nEntry data is checked" \
                   "\nPlease do not enter any extra input after 'save'"
        self.assertEqual(expected, output)

    def test_display_function_input_1(self):
        self.__con._load("file inputData.txt")
        self.__con._validate("")
        self.__con._save("")
        with self.captured_output() as (out, err):
            self.__con._display("unchecked")
        output = out.getvalue().strip()
        expected = "['T123', 'M', '20', '654', 'Normal', '56', '18-10-1996']" \
                   "\n['G834', 'M', '26', '213', 'Overweight', '566', '4-12-1990']" \
                   "\n['S931', 'F', '15', '986', 'Obesity', '852', '1-5-2001']" \
                   "\n['P12', 'M', '18', '682', 'Underweight', '135', '26-7-1998']" \
                   "\n['P912', 'D', '18', '682', 'Underweight', '135', '26-7-1998']" \
                   "\n['P912', 'M', '78', '682', 'Underweight', '135', '26-7-1998']" \
                   "\n['P912', 'M', '18', '43', 'Underweight', '135', '26-7-1998']" \
                   "\n['P912', 'M', '18', '682', 'Fit', '135', '26-7-1998']" \
                   "\n['B720', 'F', '24', '867', 'Normal', '845864', '6-1-1993']" \
                   "\n['S987', 'F', '30', '867', 'Normal', '741', '6/1/1987']" \
                   "\n['S987', 'F', '30', '867', 'Normal', '741', '6-15-1987']" \
                   "\n['S987', 'F', '30', '867', 'Normal', '741', '90-1-1987']" \
                   "\n['S987', 'F', '30', '867', 'Normal', '741', '6-1-3000']" \
                   "\n['S987', 'F', '30', '867', 'Normal', '741', '6-1-3000', 'sad', '213', '23', 'asd']" \
                   "\nUnchecked data has been displayed"
        self.assertEqual(expected, output)

    def test_display_function_input_2(self):
        self.__con._load("file inputData.txt")
        self.__con._validate("")
        self.__con._save("")
        with self.captured_output() as (out, err):
            self.__con._display("stored")
        output = out.getvalue().strip()
        expected = "['T123', 'M', '20', '654', 'Normal', '56', '18-10-1996']" \
                   "\n['G834', 'M', '26', '213', 'Overweight', '566', '4-12-1990']" \
                   "\n['S931', 'F', '15', '986', 'Obesity', '852', '1-5-2001']" \
                   "\n['B720', 'F', '24', '867', 'Normal', '845864', '6-1-1993']"\
                   "\n['S987', 'F', '30', '867', 'Normal', '741', '6/1/1987']"\
                   "\nStored data has been displayed"
        self.assertEqual(expected, output)

    def test_display_function_input_3(self):
        self.__con._load("file inputData.txt")
        self.__con._validate("")
        self.__con._save("")
        with self.captured_output() as (out, err):
            self.__con._display("imported")
        output = out.getvalue().strip()
        expected = "Please select to display the data that is 'unchecked', or 'stored'"
        self.assertEqual(expected, output)

    def test_display_function_input_4(self):
        self.__con._load("file validInputData.txt")
        self.__con._validate("")
        self.__con._save("")
        with self.captured_output() as (out, err):
            self.__con._display("graph")
        output = out.getvalue().strip()
        expected = "Graph has been created in the browser."
        self.assertEqual(expected, output)

    def test_display_function_input_5(self):
        self.__con._load("file inputData.txt")
        self.__con._validate("")
        self.__con._save("")
        with self.captured_output() as (out, err):
            self.__con._display("graph pie")
        output = out.getvalue().strip()
        expected = "Please select to display the data that is 'unchecked', or 'stored'"
        self.assertEqual(expected, output)

    def test_welcome_function_input_1(self):
        with self.captured_output() as (out, err):
            self.__con._welcome("")
        output = out.getvalue().strip()
        expected = "Welcome to the program.\nThe date is " + str(self.__today)
        self.assertEqual(expected, output)

    def test_welcome_function_input_2(self):
        with self.captured_output() as (out, err):
            self.__con._welcome("message")
        output = out.getvalue().strip()
        expected = "Please do not enter any extra input after 'welcome'"
        self.assertEqual(expected, output)


if __name__ == '__main__':
    unittest.main(verbosity=2)
