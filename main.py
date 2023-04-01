# falta ainda:
# pesquisar sobre Tk() pra tentar entender o que é exatamente
# Tentar fazer o zero sumir quando clicar na entry boxe

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

def calculate (option):
    global answer, div_by_zero
    # answer is gonna save the operation answer
    # div_by_zero is gonna check if it has been made a division by zero

    div_by_zero = 0
    # Till now no divisions by zero :)

    if option == 5:
        # Resenting the answer and the entry boxes and the answer
        answer = 0
        num1.delete(0, END)
        num1.insert(END, 0)
        num2.delete(0, END)
        num2.insert(END, 0)
        return answer_field.config(text=answer)
    
    else:        

        # That is gonna try to do the math until some "not number" has been typed
        try:
            float(num1.get())
            float(num2.get())
            # Converts wich is typed on the num1 and num2 to float number

            # Options is gonna decide which operations is need
            if option == 1:
                answer = float(num1.get()) + float(num2.get())

            elif option == 2:
                answer = float(num1.get()) - float(num2.get())

            elif option == 3:
                # That is gonna try to divide until the denominator is zero
                try:
                    answer = float(num1.get()) / float(num2.get())
                except ZeroDivisionError:
                    div_by_zero = 1

            elif option == 4:
                answer = float(num1.get()) * float(num2.get())            

            # If a div by zero has not been made, there is a answer
            if div_by_zero == 0:
                # That remains the integers answers as integers, not floats
                if answer.is_integer():
                    answer = int(answer)

            # If the operation was not a div by zero, show the answer
            if div_by_zero == 0:
                return answer_field.config(text=round(answer, 4))
            # Else, inform that a div by zero has been made
            else:
                return answer_field.config(text="Division by zero")

        # If some "not number" has been typed, inform that only numbers are allowed   
        except ValueError:
            answer_field.config(text="Only numbers!")


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

bt1 = Button(master, text="+", font="Arial 30", command=lambda: calculate(1))
bt2 = Button(master, text="-", font="Arial 30", command=lambda: calculate(2))
bt3 = Button(master, text=":", font="Arial 30", command=lambda: calculate(3))
bt4 = Button(master, text="x", font="Arial 30", command=lambda: calculate(4))
bt5 = Button(master, text="C", font="Arial 30", command=lambda: calculate(5))
# one button for each operation, one function called for each operation

#--------------------------------------------------------------------------------------------------------------

# Placing Buttons

bt1.place(width=97, height=55, x=61, y=335)
bt2.place(width=97, height=55, x=197, y=335)
bt3.place(width=97, height=55, x=333, y=335)
bt4.place(width=97, height=55, x=469, y=335)
bt5.place(width=97, height=55, x=265, y=420)

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

master.mainloop()
# To open the window - that's going to open a window, in looping, watting an event to happen

#--------------------------------------------------------------------------------------------------------------
#--------------------------------------------------------------------------------------------------------------
