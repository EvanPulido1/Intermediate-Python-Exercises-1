# Evan Pulido
# ITSC 3155-151

# Here is a link that helped me learn about dictionaries: https://realpython.com/python-dicts/

# A function that will combine the two given dictionaries
def get_combined_dict(given_my_dict_1, given_my_dict_2):

    # Links that helped me understand the commands:
    # https://www.w3schools.com/python/ref_func_dict.asp
    # https://www.w3schools.com/python/ref_dictionary_items.asp
    # https://www.w3schools.com/python/ref_func_set.asp

    # Create an empty dictionary
    combine = {}

    # A for loop that will go through the keys in the first dictionary
    for b in given_my_dict_1:
        # If a key from the first dictionary is in the second dictionary then add the values 
        # together for common keys and add the common keys to the empty combine dictionary
        if b in given_my_dict_2:
            given_my_dict_2[b] = given_my_dict_2[b] + given_my_dict_1[b]
            combine[b] = given_my_dict_2[b]

    # Return the combine dictionary
    return combine


# Ask the user how much keys the dictionary should have
number_keys_1 = int(input('Enter the number of keys the dictionary should have: '))

# Create an empty dictionary
my_dict_1 = {}

# A for loop that will ask the user to enter keys and values
# This will create a user created dictionary
for x in range(number_keys_1):
    # Ask the user to enter a key (In this case it should be letters)
    print('Enter a key: ')
    key_1 = input()

    # Ask the user to enter values that correspond with the key
    print('Enter the value for the key: ')
    value_1 = int(input())

    # Have the value put into the key
    my_dict_1[key_1] = value_1

# Repeat everything again, making another dictionary
number_keys_2 = int(input('Enter the number of keys the second dictionary should have: '))

my_dict_2 = {}

for x in range(number_keys_2):
    print('Enter a key: ')
    key_2 = input()

    print('Enter the value for the key: ')
    value_2 = int(input())

    my_dict_2[key_2] = value_2

# Print out the first dictionary and the second dictionary
print()
print('my_dict_1 = ' + str(my_dict_1))
print('my_dict_2 = ' + str(my_dict_2))

# Call a function that combines the two dictionaries by summing the values for the common keys
combined_dicts = get_combined_dict(my_dict_1, my_dict_2)

# Print the combined dictionaries
print('combine_dicts = ' + str(combined_dicts))