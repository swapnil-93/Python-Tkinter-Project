# Import Tkinter Library
from tkinter import *

# Create a Frame for calculator
def calc(source, side):
    store = Frame(source, borderwidth=4, bd=4, bg="powder blue")
    store.pack(side=side, expand =YES, fill =BOTH)
    return store

# Create buttons
def button(source, side, text, command=None):
    store = Button(source, text=text, command=command)
    store.pack(side=side, expand = YES, fill=BOTH)
    return store

# Create a class to create the application
class app(Frame):
    def __init__(self):
        Frame.__init__(self)
        self.option_add('*Font', 'arial 20 bold')
        self.pack(expand = YES, fill =BOTH)
        self.master.title('Calculator')

        # add display widget
        display = StringVar()
        Entry(self, relief=RIDGE, textvariable=display, justify='right', bd=30, bg="powder blue").pack(side=TOP, expand=YES, fill=BOTH)

        # Add Clear button
        for clearButton in (["C"]):
            erase = calc(self, TOP)
            for ichar in clearButton:
                button(erase, LEFT, ichar, lambda store=display, q=ichar: store.set(''))

        # Adding Numbers an Operators
        for numButton in ("789/", "456*", "123-", "0.+"):
         FunctionNum = calc(self, TOP)
         for iEquals in numButton:
            button(FunctionNum, LEFT, iEquals, lambda store=display, q=iEquals: store.set(store.get() + q))

        # Equal Button
        EqualButton = calc(self, TOP)
        for iEquals in "=":
            if iEquals == '=':
                btniEquals = button(EqualButton, LEFT, iEquals)
                btniEquals.bind('<ButtonRelease-1>', lambda e,s=self, store=display: s.calc(store), '+')

            else:
                btniEquals = button(EqualButton, LEFT, iEquals, lambda store=display, s=' %s ' % iEquals: store.set(store.get() + s))

    # get output or error
    def calc(self, display):
            try:
                display.set(eval(display.get()))
            except:
                display.set("ERROR")


# Program starts here
if __name__=='__main__':
 app().mainloop()