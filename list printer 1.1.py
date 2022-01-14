import statistics # This module is needed to find the median of the list.
the_list = [] # This list will be filled by user later when list_printer is called.

# This function contains the code that fills the list. The explanations are within it.
def list_printer():
    how_many_numbers = int(input('enter the amount of numbers for the list: '))  # for the number of things that will be in the list, the user will-
    for x in range(how_many_numbers):                                            # be asked to enter a number. each number the user inputs will be appended to the list
        enter_number_in_list = int(input('enter a number: '))
        the_list.append(enter_number_in_list)

# This is the title that is printed.
print('''--- welcome to list printer ---
you will be allowed to fill the list, and then the program will make calculations for the list. Enjoy :D
''')

# This try and except part will quit the program if the user enters something that causes an error in the code. Like a string.
# This is too prevent annoying red error text, and to make the program more clean. :)
try:
    list_printer() # If there is an error in this, then the code in the except block will run.
except:
    print("Only numbers please. Manually restart the code because I don't know how to make it restart itself. ")
    quit()



print('the list: ', the_list) # This prints the list after it is filled.

count = 0
print('''---------------------------
 count | number ''')
# For each number that is the list, "count" will go up by 1. Example: if there are 5 numbers, count will go up by 1 and stop at 5.
for number in the_list:            # Each number that is in the list will be printed along with "count".
    count = 1 + count
    print(f'{count}          {number}')


print('''---------------------------
the calculations:
''')
# Most of these are self explanatory
sum = sum(the_list)
average = sum / count  # Divides the sum of all the numbers in the list-
biggest = max(the_list)   # with the amount of numbers there are in the list.
smallest = min(the_list)
median = statistics.median(the_list)

print(f'sum: {sum}')
print(f'average: {int(average)}')
print(f'biggest: {biggest}')
print(f'smallest: {smallest}')
print(f'median: {median}')