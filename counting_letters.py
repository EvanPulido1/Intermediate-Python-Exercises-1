# Evan Pulido
# ITSC 3155-151

# A function that counts the number of each letter from the string
def count_the_letters(provided_string):
    # Create an empty dictionary
    count_letter_dict = {}

    # A for loop that will go through every letter in the string
    for letter in provided_string:
        # This if else statement that will add keys to dictionaries
        # If the letter is a new element in the dictionary then its key value would be 1
        # If the letter is an old element in the dictionary then its key value increases by 1
        if letter in count_letter_dict:
            count_letter_dict[letter] = count_letter_dict[letter] + 1
        else:
            count_letter_dict[letter] = 1
    
    # Return the dictionary
    return count_letter_dict


# Ask the user to input a string
given_string = input('Enter a string: ')

# The link that helped me with the lower command: https://www.programiz.com/python-programming/methods/string/lower
# Makes the provided string into all lowercase letters
given_string = given_string.lower()

# The link that helped me remove spaces from a string: https://www.geeksforgeeks.org/python-remove-spaces-from-a-string/
# Remove the spaces of the string
given_string = given_string.replace(' ', '')

# Call the function and put the given dictionary into a variable
count_dict = count_the_letters(given_string)

# Print the dictionary
print(count_dict)