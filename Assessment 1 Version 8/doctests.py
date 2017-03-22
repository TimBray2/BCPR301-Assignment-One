"""
# Doctests for the load function

>>> control.load("database")
Loaded from database

>>> control.load("database employee")
Please select to load from 'database' or 'file [location]'

>>> control.load("file")
Please select to load from 'database' or 'file [location]'

>>> control.load("file validInputData.txt")
Loaded from file

>>> control.load("file doesNotExist.txt")
Please select a valid file location

# Doctests for the validate function

# >>> control.load("file D:\Documents\CPIT\2017\Advanced Programming\Assessment 1\Assessment 1 Version 11\validInputData.txt"); control.validate()
Entry data is checked

# Doctests for save function



# Doctests for display function



# Doctests for exit function



# Doctests for create_database function
"""
from controller import Controller
import cmd_view


control = Controller(cmd_view.CmdView())
control.go(control)

if __name__ == "__main__":
    import doctest
    doctest.testmod(verbose=True)
