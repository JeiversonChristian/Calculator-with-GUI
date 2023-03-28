from tkinter import *

# "tkinter" provides a robust, platform-independent windowing toolkit that is available to Python programmers
# read to learn more about tkinter library: https://docs.python.org/pt-br/3/library/tk.html

# "*" is used to import everything from the library

#--------------------------------------------------------------------------------------------------------------

master = Tk()
# Instantiating the class to the variable "master"
# So we can use all the functions of the class through the variable "master"

master.title(" Calculator ")
# Application title

master.iconbitmap(default="icons/calculator.ico")
# To add (replacing) an icon on the window

master.geometry("300x500+0+0")
# To position the window
# width x height + dist from left + dist from top
# Unit of measurement: pixel

master.mainloop()
# To open the window - that's going to open a window, in a randon place, in looping watting an event to happen
