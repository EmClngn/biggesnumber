# Ask user to input 3 numbers. Find and print the biggest number using only if-else statement

# Transform the code for tkinter
from tkinter import *

    
window = Tk()
window.config(background = "navajowhite")
window.title("Biggest Number Finder")
window.geometry("450x300")

# Do something to handle errors(Errors are decimals and characters besides numbers)
def finding_the_biggest ():
# Error Handling
    try: 
        first_number = float(first_entry.get())
        second_number = float(second_entry.get())
        third_number = float(third_entry.get())
# Finding the largest number using if-then statement
        if first_number >= second_number and first_number >= third_number:
            biggest_number = first_number
        elif second_number >= third_number:
            biggest_number = second_number
        else:
            biggest_number = third_number

        the_biggest.config(text = "\n"f"The biggest number on your input is {biggest_number}",
                           fg = "brown4",
                           font = ("Times", 10))
    except ValueError:
        the_biggest.config(text = "\n" "Only input Numerical Values and fill up every entries.""\n" "Please try again...",
                           fg = "red3",
                           font = ("Times", 10))
   
# Ask user for 3 inputs of number
number_list = (Label(window, text = "\n""What are your chosen numbers?""\n",
                     font = ("Times", 15),
                     bg = "navajowhite",
                     fg = "gray1"))
number_list.pack()

for_blank_space_one = Label(window, bg = "navajowhite")
for_blank_space_two = Label(window, bg = "navajowhite")
for_blank_space_three = Label(window, bg = "navajowhite")

first_entry = Entry(window, bg = "burlywood2", justify = CENTER)
second_entry = Entry(window, bg = "burlywood2", justify = CENTER )
third_entry = Entry(window, bg = "burlywood2", justify = CENTER)

first_entry.pack()
for_blank_space_one.pack()
second_entry.pack()
for_blank_space_two.pack()
third_entry.pack()
for_blank_space_three.pack()

submit_button = Button(window, text = "Submit", 
                       command = finding_the_biggest, 
                       bg = "burlywood4",
                       fg = "ivory2")
submit_button.pack()

the_biggest = Label(window, text = "\n" "", bg = "navajowhite")
the_biggest.pack()

window.mainloop()
