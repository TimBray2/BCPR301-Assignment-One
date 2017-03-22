"""
# Doctests for the load function

>>> __controller._load("database")
Opened database successfully
Finishing connection to database
Loaded from database

>>> __controller._load("database employee")
Please select to load from 'database' or 'file [location]'

>>> __controller._load("file")
Please select to load from 'database' or 'file [location]'

>>> __controller._load("file validInputData.txt")
Loaded from file

>>> __controller._load("file doesNotExist.txt")
Please select a valid file location

"""
from controller import Controller
import cmd_view


__controller = Controller(cmd_view.CmdView())
__controller._go(__controller)
if __name__ == "__main__":
    import doctest
    doctest.testmod(verbose=True)
