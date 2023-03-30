#--------------------------------------------------------------------------------------------------------------
#--------------------------------------------------------------------------------------------------------------

# Libraries

from tkinter import *

# "tkinter" provides a robust, platform-independent windowing toolkit that is available to Python programmers
# read to learn more about tkinter library: https://docs.python.org/pt-br/3/library/tk.html

# "*" is used to import everything from the library

#--------------------------------------------------------------------------------------------------------------
#--------------------------------------------------------------------------------------------------------------

#--------------------------------------------------------------------------------------------------------------
#--------------------------------------------------------------------------------------------------------------

# Functions

#In case you want to discover the coordinates of your window and get the dimension you wish:
'''def left_mouse_click(retorno):
    print(f'x: {retorno.x} | y: {retorno.y} Geo: {master.geometry()}')'''

def left_mouse_click(arg):
    global flag, x1, y1
    # global variables - I don't know yet why they must to be global
    
    # Flag begin valuing 0 - which means False
    # So, "not flag" inverts the value to 1 - True
    flag = not flag

    if flag:
        x1 = arg.x
        y1 = arg.y

    else:
        print(f'width={arg.x-x1}, height={arg.y-y1}, x={x1}, y={y1}')


def calcular (x):
    print(x)

#--------------------------------------------------------------------------------------------------------------
#--------------------------------------------------------------------------------------------------------------

#--------------------------------------------------------------------------------------------------------------
#--------------------------------------------------------------------------------------------------------------

# Main

#--------------------------------------------------------------------------------------------------------------

# Creating the master window

master = Tk()
# Instantiating the class to the variable "master" - to our master window
# So we can use all the functions of the class through the variable "master"

master.title(" Calculator ")
# Application title

master.iconbitmap(default="icons/calculator.ico")
# To add (replacing) an icon on the window

master.geometry("630x510+385+84")
# To position the window
# width x height + dist from left + dist from top
# Unit of measurement: pixel

master.wm_resizable(width=False, height=False)
# Locking the dimensions of the window

#--------------------------------------------------------------------------------------------------------------

# Global Variables

flag = x1 = y1 = x = 0

#--------------------------------------------------------------------------------------------------------------

# Importing Images

calc_image = PhotoImage(file="images/calculator.png")
# calculator image

#--------------------------------------------------------------------------------------------------------------

# Creating Labels

calc_label = Label(master, image=calc_image)
# label where the image of the calculator is going to be binded

answer_field = Label(master, font="Arial 40", text = "0")
# label where is going to be showed the answer

#--------------------------------------------------------------------------------------------------------------

# Placing Labels

calc_label.place(x=-25, y=-80)
# calculator label

answer_field.place(width=460, height=69, x=84, y=73)
# answer_field label

#--------------------------------------------------------------------------------------------------------------

# Creating Buttons

bt1 = Button(master, text="+", font="Arial 30", command=lambda: calcular(1))
bt2 = Button(master, text="-", font="Arial 30", command=lambda: calcular(2))
bt3 = Button(master, text=":", font="Arial 30", command=lambda: calcular(3))
bt4 = Button(master, text="x", font="Arial 30", command=lambda: calcular(4))
# one button for each operation, one function called for each operation

#--------------------------------------------------------------------------------------------------------------

# Placing Buttons

bt1.place(width=97, height=55, x=61, y=335)
bt2.place(width=97, height=55, x=197, y=335)
bt3.place(width=97, height=55, x=333, y=335)
bt4.place(width=97, height=55, x=469, y=335)

#--------------------------------------------------------------------------------------------------------------

# Entry boxes

num1 = Entry(master, font="Arial 20", justify=CENTER)
num2 = Entry(master, font="Arial 20", justify=CENTER)
# "justify CENTER" makes the number appears on the middle when it is digited

#--------------------------------------------------------------------------------------------------------------

# Placing Entry Boxes

num1.place(width=185, height=40, x=84, y=220)
num2.place(width=185, height=40, x=359, y=220)

#--------------------------------------------------------------------------------------------------------------

# Setting Initial Entry values

num1.insert(END, 0)
num2.insert(END, 0)
# 0 will appear in the END of the place. If there was another number on it, 0 would appear after it

#--------------------------------------------------------------------------------------------------------------

# events
master.bind("<Button-1>", left_mouse_click)
# Button 1 is the left mouse button
# Button 2 is the middle mouse button
# Button 3 is the right mouse button
# "bind" literally bind the <Button-x> to the function used as parameter

master.mainloop()
# To open the window - that's going to open a window, in looping, watting an event to happen

#--------------------------------------------------------------------------------------------------------------
#--------------------------------------------------------------------------------------------------------------
