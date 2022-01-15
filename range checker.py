# this checks if the number in a list is within a certain range
awdhj = []
how_many_numbers = int(input('enter the amount of numbers for the list: '))
for x in range(how_many_numbers):
    enter_number_in_list = int(input('enter a number: '))
    awdhj.append(enter_number_in_list)

what_is_range = int(input('Enter the range: '))
for number in awdhj:
    if number in range(what_is_range):
        print(f'This number is within {what_is_range}: {number}')
    else:
        print(f"This number is not within {what_is_range}: {number} ")