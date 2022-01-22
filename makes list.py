#  current version 1/15 8.03pm

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
    