#  current version 1/15 8.03pm

import statistics
the_list = []

print('''--- welcome to list printer ---
you will be allowed to fill the list, and then the program will make calculations for the list. Enjoy :D
''')
# This is the code that fills the list.
# This try and except part will quit the program if the user enters something that causes an error in the program.
try:
    times_asked = 0
    how_many_numbers = int(input('Enter the amount of numbers you want there to be in your list: '))
    for x in range(how_many_numbers):
        times_asked = 1 + times_asked
        enter_number_in_list = int(input(f'{times_asked}. Enter a number: '))
        the_list.append(enter_number_in_list)
except:
    print("Only numbers please. Manually restart the code because I don't know how to make it restart itself. ")
    quit()

print(f'''
The list: {the_list} ''')

count = 0
print('''---------------------------
 count | number ''')
# this adds 1 to count for each number in the list
for number in the_list:
    count = 1 + count
    print(f'{count}          {number}')


# the calculations
print('''---------------------------
the calculations:
''')
sum = sum(the_list)
average = sum / count
biggest = max(the_list)
smallest = min(the_list)
median = statistics.median(the_list)
print(f'sum: {sum}')
print(f'average: {int(average)}')
print(f'biggest: {biggest}')
print(f'smallest: {smallest}')
print(f'median: {median}')

# this part checks how many numbers are within a certain range(that the user inputs)
print('''
--- range checker ---''')

amount_of_numbers_in_theRange = 0
amount_of_numbers_not_in_theRange = 0
check_range = input('''
Do you want me to check how many numbers from the list are in a certain range? If so, enter 'yes':  ''')
try:
    if check_range == 'yes':
        print(f'Here is your list: {the_list}')
        what_is_range = int(input('Enter the range 0-'))
        print(' ')
        for number in the_list:
            if number in range(what_is_range + 1):
                amount_of_numbers_in_theRange = amount_of_numbers_in_theRange + 1
                print(f'Is within 0-{what_is_range}: {number}')
            else:
                amount_of_numbers_not_in_theRange = amount_of_numbers_not_in_theRange + 1
                print(f"Is not within 0-{what_is_range}: {number} ")
        print(' ')
        print(f'Amount of numbers within 0-{what_is_range}: {amount_of_numbers_in_theRange}')
        print(f'Amount of numbers not within 0-{what_is_range}: {amount_of_numbers_not_in_theRange}')

    else:
        print('Ok. thank you for using list printer :).')
        quit()
except:
    quit()


# this will print all the results onto a file called out.txt
from contextlib import redirect_stdout

with open('out.txt', 'w') as f:
    with redirect_stdout(f):
        print(f'The list: {the_list} ')
        count = 0
        print('---------------------------')
        print(' count | number ')
        # this adds 1 to count for each number in the list
        for number in the_list:
            count = 1 + count
            print(f'{count}          {number}')
        print('---------------------------')
        print('the calculations:')
        print(' ')
        print(f'sum: {sum}')
        print(f'average: {int(average)}')
        print(f'biggest: {biggest}')
        print(f'smallest: {smallest}')
        print(f'median: {median}')

        print(' ')
        print('--- range checker ---')
        print(f'Here is your list: {the_list}')
        for number in the_list:
            if number in range(what_is_range + 1):
                amount_of_numbers_in_theRange = amount_of_numbers_in_theRange + 1
                print(f'Is within 0-{what_is_range}: {number}')
            else:
                amount_of_numbers_not_in_theRange = amount_of_numbers_not_in_theRange + 1
                print(f"Is not within 0-{what_is_range}: {number} ")
        print(' ')
        print(f'Amount of numbers within 0-{what_is_range}: {amount_of_numbers_in_theRange}')
        print(f'Amount of numbers not within 0-{what_is_range}: {amount_of_numbers_not_in_theRange}')

