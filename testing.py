# working on new version 1/21/22

# this function creats and allows the user to fill the list
from __future__ import print_function
import sympy
import statistics

the_list = []

print('--- welcome to list printer ---')
print('you will be allowed to fill the list, and then the program will make calculations for the list. Enjoy :D')
print(' ')

# this part fills the list:
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
print(' ')
print(f'The list: {the_list}')


# this part creats count which will be needed for the calulations, then it neatly displays the list.

count = 0
print('---------------------------')
print('count | number ')
# this adds 1 to count for each number in the list
for number in the_list:
    count = 1 + count
    print(f'{count}          {number}')



# this asks the user for instructions:
amount_prime = 0
amount_not_prime = 0
amount_range = 0
amount_not_range = 0

make_program_run = True
while make_program_run:
    decision = input("what would you like me to do? type help to show the options ")

if decision == 'help':
    print('''
quit - quits the program
sum - finds the sum 
small - finds the smallest 
big - finds the biggest 
median - finds the median 
average - finds the average 
prime - checks which numbers are prime and not prime
range - checks how many numbers are within a certain range''')
elif decision == 'quit':
    quit(print('thank you for using list printer!'))
elif decision == 'sum':
    sum = sum(the_list)
    print(sum)

elif decision == 'small':
    small = min(the_list)
    print(small)

elif decision == 'big':
    biggest = max(the_list)
    print(biggest)

elif decision == 'median':
    median = statistics.median(the_list)
    print(median)

elif decision == 'average':
    average = average(the_list)
    print(average)

elif decision == 'prime':
    for number in the_list:
        prime_checker = (sympy.isprime(the_list))
        if prime_checker == False:
            print(f'{number} is not a prime')
        elif prime_checker:
            print(f'{number} is a prime')

elif decision == 'range':
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

                



    
