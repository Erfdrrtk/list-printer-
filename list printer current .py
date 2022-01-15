#  current version 1/14 8.03pm

import statistics
the_list = []

# This function contains the code that fills the list.
def list_printer():
    times_asked = 0
    how_many_numbers = int(input('Enter the amount of numbers you want there to be in your list: '))
    for x in range(how_many_numbers):
        times_asked = 1 + times_asked
        enter_number_in_list = int(input(f'{times_asked}. Enter a number: '))
        the_list.append(enter_number_in_list)


print('''--- welcome to list printer ---
you will be allowed to fill the list, and then the program will make calculations for the list. Enjoy :D
''')

# This try and except part will quit the program if the user enters something that causes an error in the program.
try:
    list_printer()
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



check_range = input('''
Do you want me to check if a certain number is in a list? If so, enter 'yes':  ''')
try:
    if check_range == 'yes':
        print(f'Here is your list: {the_list}')
        what_is_range = int(input('Enter the range: '))
        for number in the_list:
            if number in range(what_is_range):
                print(f'Is within 0-{what_is_range}: {number}')
            else:
                print(f"Is not within 0-{what_is_range}: {number} ")
    else:
        print('Ok. thank you for using list printer :).')
        quit()
except:
    quit(print('pls dont breAK the code'))