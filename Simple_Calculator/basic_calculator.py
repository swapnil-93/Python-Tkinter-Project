# Python program to  create a simple GUI  calculator using Tkinter

# import everything from tkinter module
from tkinter import *

# globally declare the expression variable
expression = ""


# Function to update expression in the text entry box
def press(num):
    # point out the global expression variable
    global expression

    # concatenation of string
    expression = expression + str(num)

    # update the expression by using set method
    equation.set(expression)


# Function to evaluate the final expression
def equalpress():

    try:

        global expression

        # eval function evaluate the expression and str function convert the result into string
        total = str(eval(expression))

        equation.set(total)

        # initialze the expression variable by empty string
        expression = ""

        # if error is generate then handle
    # by the except block
    except:

        equation.set(" error ")
        expression = ""

    # Function to clear the contents


# of text entry box
def clear():
    global expression
    expression = ""
    equation.set("")


# Driver code
if __name__ == "__main__":
    # create a GUI window
    root = Tk()

    # set the background colour of GUI window
    root.configure(background="light blue")

    # set the title of GUI window
    root.title("Simple Calculator")

    # set the configuration of GUI window
    root.geometry("200x150")

    # StringVar() is the variable class
    equation = StringVar()

    # create the text entry box for showing the expression .
    expression_field = Entry(root, textvariable=equation)

    # grid method is used for placing  the widgets at respective positions in table like structure .
    expression_field.grid(columnspan=4, ipadx=70)

    equation.set('enter your expression')

    # create a Buttons and place at a particular location inside the root window .
    button1 = Button(root, text=' 1 ', fg='black', bg='white', command=lambda: press(1), height=1, width=5)
    button1.grid(row=2, column=0)

    button2 = Button(root, text=' 2 ', fg='black', bg='white', command=lambda: press(2), height=1, width=5)
    button2.grid(row=2, column=1)

    button3 = Button(root, text=' 3 ', fg='black', bg='white', command=lambda: press(3), height=1, width=5)
    button3.grid(row=2, column=2)

    button4 = Button(root, text=' 4 ', fg='black', bg='white', command=lambda: press(4), height=1, width=5)
    button4.grid(row=3, column=0)

    button5 = Button(root, text=' 5 ', fg='black', bg='white', command=lambda: press(5), height=1, width=5)
    button5.grid(row=3, column=1)

    button6 = Button(root, text=' 6 ', fg='black', bg='white', command=lambda: press(6), height=1, width=5)
    button6.grid(row=3, column=2)

    button7 = Button(root, text=' 7 ', fg='black', bg='white', command=lambda: press(7), height=1, width=5)
    button7.grid(row=4, column=0)

    button8 = Button(root, text=' 8 ', fg='black', bg='white', command=lambda: press(8), height=1, width=5)
    button8.grid(row=4, column=1)

    button9 = Button(root, text=' 9 ', fg='black', bg='white', command=lambda: press(9), height=1, width=5)
    button9.grid(row=4, column=2)

    button0 = Button(root, text=' 0 ', fg='black', bg='white', command=lambda: press(0), height=1, width=5)
    button0.grid(row=5, column=0)

    plus = Button(root, text=' + ', fg='black', bg='white', command=lambda: press("+"), height=1, width=5)
    plus.grid(row=2, column=3)

    minus = Button(root, text=' - ', fg='black', bg='white', command=lambda: press("-"), height=1, width=5)
    minus.grid(row=3, column=3)

    multiply = Button(root, text=' * ', fg='black', bg='white', command=lambda: press("*"), height=1, width=5)
    multiply.grid(row=4, column=3)

    divide = Button(root, text=' / ', fg='black', bg='white', command=lambda: press("/"), height=1, width=5)
    divide.grid(row=5, column=3)

    equal = Button(root, text=' = ', fg='black', bg='white', command=equalpress, height=1, width=5)
    equal.grid(row=5, column=2)

    clear = Button(root, text='Clear', fg='black', bg='white', command=clear, height=1, width=5)
    clear.grid(row=5, column='1')

    Decimal = Button(root, text='.', fg='black', bg='white', command=lambda: press('.'), height=1, width=5)
    Decimal.grid(row=6, column=0)


    # start the GUI
    root.mainloop()