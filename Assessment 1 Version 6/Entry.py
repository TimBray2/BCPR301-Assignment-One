# Written by Tim Bray
import csv


class FileEntry:
    def __init__(self):
        self.results = []

    def get_input(self, directory):
        with open(directory, newline='') as input_file:
            for row in csv.reader(input_file):
                self.results.append(row)

    def set_types(self):
        for element in self.results:
            count = 0
            for item in element:
                if count in [2, 3, 5]:
                    element[count] = int(item)
                count += 1

    def display_file_entry(self):
        for i in self.results:
            print(i)

    def get_data(self):
        return self.results

entry = FileEntry()
