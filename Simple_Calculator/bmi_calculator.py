# import Library
from tkinter import *
from tkinter import messagebox

# Create an Object
root = Tk()

# Create shape
root.geometry("400x400")

# Give title
root.title("BMI Calculator")

# get height value from Entry field
def get_height():
     height = float(get_height.get())
     return height

#  get weight value from Entry field
def get_weight():
    weight = float(get_weight.get())
    return weight

# get the BMI Value
def calculate_bmi():
  
    try:
        height = get_height()
        weight = get_weight()
        height = height / 100.0  # to convert meters into centimeter
        bmi = weight / (height**2)

    except ZeroDivisionError:           # if divided by Zero
        messagebox.showinfo("Result", "Please enter positive height!!")

    except ValueError:          # if entered wrong value or negative value
        messagebox.showinfo("Result", "Please enter valid data!")
    else:
        if bmi <= 15.0:
            res = "Your BMI is " + str(bmi) + "\nRemarks: Very severely underweight!!"
            messagebox.showinfo("Result", res)
        elif bmi > 15.0 and bmi <= 16.0:
            res = "Your BMI is " + str(bmi) + "\nRemarks: Severely underweight!"
            messagebox.showinfo("Result", res)
        elif bmi > 16.0 and bmi < 18.5:
            res = "Your BMI is " + str(bmi) + "\nRemarks: Underweight!"
            messagebox.showinfo("Result", res)
        elif bmi >= 18.5 and bmi <= 25.0:
            res = "Your BMI is " + str(bmi) + "\nRemarks: Normal."
            messagebox.showinfo("Result", res)
        elif bmi > 25.0 and bmi <= 30:
            res = "Your BMI is " + str(bmi) + "\nRemarks: Overweight."
            messagebox.showinfo("Result", res)
        elif bmi > 30.0 and bmi <= 35.0:
            res = "Your BMI is " + str(bmi) + "\nRemarks: Moderately obese!"
            messagebox.showinfo("Result", res)
        elif bmi > 35.0 and bmi <= 40.0:
            res = "Your BMI is " + str(bmi) + "\nRemarks: Severely obese!"
            messagebox.showinfo("Result", res)
        else:
            res = "Your BMI is " + str(bmi) + "\nRemarks: Super obese!!"
            messagebox.showinfo("Result", res)

# Create a label to get height
height_label = Label(root, bg="light blue", text="Enter Weight (in kg):", bd=6,font=("Helvetica", 10, "bold"))
height_label.place(x=80, y=30)

# Crate entry for weight
get_weight = Entry(root, bd=7, width=6)
get_weight.place(x=230, y=30)

# Create an entry widget for weight
weight_label = Label(root, bg="light blue", text="Enter Height (in cm):", bd=6, font=("Helvetica", 10, "bold"))
weight_label.place(x=80, y=80)

# Create an entry widget for height
get_height = Entry(root, bd=7, width=6)
get_height.place(x=230, y=80)

# Create a button to calculate BMI
button = Button(bg="light green", bd=12, text="Calculate BMI", padx=33, pady=15, command=calculate_bmi, font=("Helvetica", 20, "bold"))
button.grid(row=1, column=0, sticky=W)
button.place(x=50, y=120)
root.mainloop()
