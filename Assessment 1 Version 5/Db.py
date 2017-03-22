# Written By Tim Bray
import sqlite3


class Database:
    def __init__(self):
        self.rows = []
        self.con = self.connect()
        self.con.close()
        # self.create_database()

    def connect(self):
        # Connecting to the database file
        sqlite_file = 'employeeDb'  # name of the sqlite database file
        return sqlite3.connect(sqlite_file)

    def create_database(self):
        c = self.con.cursor()
        c.execute('''CREATE TABLE IF NOT EXISTS Employee(
            EMPID    	VarChar(4) primary key,
            Gender	 	VarChar(1),
            Age      	int(2),
            Sales 		int(3),
            BMI         VarChar(11),
            Salary      int(3),
            Birthday    date);''')
        c.execute('''INSERT INTO Employee VALUES ('T123', 'M', 20, 654, 'Normal', 56, '1996-10-18');''')
        c.execute('''INSERT INTO Employee VALUES ('G834', 'M', 54, 213, 'Overweight', 566, '1990/12/4');''')
        c.execute('''INSERT INTO Employee VALUES ('S931', 'F', 80, 986, 'Obesity', 852, '2001-5-1');''')
        c.execute('''INSERT INTO Employee VALUES ('P912', 'M', 34, 483, 'Underweight', 135, '1998-7-26');''')
        c.execute('''INSERT INTO Employee VALUES ('B720', 'F', 67, 867, 'Normal', 741, '1993-1-6');''')

    def load_database(self):
        c = self.con.cursor()
        c.execute("SELECT * FROM Employee")
        self.rows = c.fetchall()
        self.con.close()
        return self.rows

    def close_database(self):
        self.con.close()

    def display_database_entry(self):
        for row in self.rows:
            print(row)

    def get_database_input(self):
        return self.rows
