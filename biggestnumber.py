# Ask user to input 3 numbers. Find and print the biggest number using only if-else statement


# pseudo code


# Ask user for 3 inputs of number
first_number = input("What is your first number: ")
second_number = input("What is your second number: ")
third_number = input("What is your third number: ")


# Make a way to find the biggest number among the 3 user inputs using if-else statement
if first_number >= second_number and first_number >= third_number:
    biggest_number = first_number
elif second_number >= third_number:
    biggest_number = second_number
else:
    biggest_number = third_number

# Print the biggest number
print(biggest_number)
# Do something to handle errors
# Transform the code for tkinter