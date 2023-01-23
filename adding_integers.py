# Evan Pulido
# ITSC 3155-151

# Links that helped me with this exercise are: https://www.geeksforgeeks.org/how-to-use-while-true-in-python/
# https://docs.python.org/3/library/exceptions.html
# https://docs.python.org/3/tutorial/errors.html

# This is a while loop that will iterate infinitely and what stops
# it is when the user inputs an integer
while True:
    # A try block that tests if the code for errors
    # The except block handles and deals with errors
    # For this exercise we use the ValueError exception to check if what the use inputted is an integer
    try:
        # Ask the user to input an integer
        number_1 = int(input('Enter int #1: '))
        break
    # If the value inputted is not an integer, print a message telling the user
    except ValueError:
        print('Invalid input. Please enter an int.')

# This is repeated 4 more times, once for each number
while True:
    try:
        number_2 = int(input('Enter int #2: '))
        break
    except ValueError:
        print('Invalid input. Please enter an int.')

while True:
    try:
        number_3 = int(input('Enter int #3: '))
        break
    except ValueError:
        print('Invalid input. Please enter an int.')

while True:
    try:
        number_4 = int(input('Enter int #4: '))
        break
    except ValueError:
        print('Invalid input. Please enter an int.')

while True:
    try:
        number_5 = int(input('Enter int #5: '))
        break
    except ValueError:
        print('Invalid input. Please enter an int.')

# Add the numbers together
sum = (number_1) + (number_2) + (number_3) + (number_4) + (number_5)

# Print the sum of all the numbers
print('Your sum is ' + str(sum))