# Written By Tim Bray
import sqlite3


class Database:
    def __init__(self):
        self.__rows = []
        self.__con = ""
        self.__conn = ""

    def _connect(self):
        sqlite_file = 'employeeDb'
        try:
            self.__conn = sqlite3.connect(sqlite_file)
        except Exception as e:
            print(e)
        else:
            print("Opened database successfully")
        finally:
            print("Finishing connection to database")
            return self.__conn

    def _create_database(self):
        self.__con = self._connect()
        c = self.__con.cursor()
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
        c.execute('''INSERT INTO Employee VALUES ('S931', 'F', 15, 986, 'Obesity', 852, '2001-5-1');''')
        c.execute('''INSERT INTO Employee VALUES ('P912', 'M', 18, 483, 'Underweight', 135, '1998-7-26');''')
        c.execute('''INSERT INTO Employee VALUES ('B720', 'F', 24, 867, 'Normal', 741, '1993-1-6');''')

    def _load_database(self):
        c = self.__con.cursor()
        c.execute("SELECT * FROM Employee")
        self.__rows = c.fetchall()
        return self.__rows

    def _display_database_entry(self):
        for row in self.__rows:
            print(row)
