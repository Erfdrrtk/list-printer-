# this will print all the results onto a file called out.txt
# needs the rest of the code in order to work
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
        amount_of_numbers_not_in_theRange = 0
        amount_of_numbers_in_theRange = 0
        for number in the_list:
            if number in range(what_is_range):
                amount_of_numbers_in_theRange = amount_of_numbers_in_theRange + 1
                print(f'Is within 0-{what_is_range}: {number}')
            else:
                amount_of_numbers_not_in_theRange = amount_of_numbers_not_in_theRange + 1
                print(f"Is not within 0-{what_is_range}: {number} ")
        print(' ')
        print(f'Amount of numbers within 0-{what_is_range}: {amount_of_numbers_in_theRange}')
        print(f'Amount of numbers not within 0-{what_is_range}: {amount_of_numbers_not_in_theRange}')