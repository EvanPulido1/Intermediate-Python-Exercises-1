# Evan Pulido
# ITSC 3155-151

# A link that helped me understand lists: https://www.programiz.com/python-programming/list
# A link that helped me understand functions: https://www.w3schools.com/python/python_functions.asp

# Function that creates a list with user inputted integers and makes a new list with unique elements
# from the other list
def get_unique_list(given_number_list):
    # Make a new list
    new_list = []

    # A loop that will add unique elements into the new list
    for y in given_number_list:
        # If the element is not in the new list then it will be added to it
        # if not then if will not be added, making the list only contain unique integers
        if y not in new_list:
            new_list.append(y)
    
    # return the new_list that holds only unique elements
    # A link about the return statement:https://realpython.com/python-return-statement/
    return new_list



# Create an empty list to hold integers
number_list = []

# A link that helped me: https://www.geeksforgeeks.org/taking-input-in-python/
# Ask the user how many numbers should the list contain
number_of_ints = int(input("Enter how many integers should be on the list: "))

# A link that helped me with this: https://www.w3schools.com/python/ref_func_range.asp
# A for loop that will ask the user to input integers and it will add the integers into the list
for x in range(0, number_of_ints):
    print('Enter an integer: ')
    number = int(input())

    # Adds each integer into the list
    number_list.append(number)

# Print the list
print()
print('number_list = ' + str(number_list))

# Call the get_unique_list function and add it to a variable
unique_number_list = get_unique_list(number_list)

# Print the unique_number_list
print('unique_number_list = ' + str(unique_number_list))