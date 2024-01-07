# Ask user to input 3 numbers. Find and print the biggest number using only if-else statement

# Transform the code for tkinter
from tkinter import *

    
window = Tk()
# Do something to handle errors(Errors are decimals and characters besides numbers)
def finding_the_biggest ():
    try: 
        first_number = float(first_entry.get())
        second_number = float(second_entry.get())
        third_number = float(third_entry.get())

        if first_number >= second_number and first_number >= third_number:
            biggest_number = first_number
        elif second_number >= third_number:
            biggest_number = second_number
        else:
            biggest_number = third_number

        the_biggest.config(text = f"The biggest number on your input is{biggest_number}")
    except ValueError:
        the_biggest.config(text = "Please only input Numerical Values")
   

# Ask user for 3 inputs of number
number_list = (Label(window, text = "Give me your numbers"))
number_list.pack()

first_entry = Entry(window)
second_entry = Entry(window)
third_entry = Entry(window)

first_entry.pack()
second_entry.pack()
third_entry.pack()

submit_button = Button(window, text = "Submit", command = finding_the_biggest)
submit_button.pack()

the_biggest = Label(window, text = "")
the_biggest.pack()

window.mainloop()

# just to not forget
"""while True:
    try:
# Ask user for 3 inputs of number
        first_number = float(input("What is your first number: "))
        second_number = float(input("What is your second number: "))
        third_number = float(input("What is your third number: "))

# Make a way to find the biggest number among the 3 user inputs using if-else statement
        if first_number >= second_number and first_number >= third_number:
            biggest_number = first_number
        elif second_number >= third_number:
            biggest_number = second_number
        else:
            biggest_number = third_number
# Print the biggest number
        print("The biggest number on your input is", biggest_number)
        break
    except ValueError:
        print("Only input numerical values. Please try again...")
      
# Transform the code for tkinter"""