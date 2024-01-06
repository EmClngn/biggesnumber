# Ask user to input 3 numbers. Find and print the biggest number using only if-else statement


# pseudo code

# Do something to handle errors(Errors are decimals and characters besides numbers)
while True:
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
      
# Transform the code for tkinter