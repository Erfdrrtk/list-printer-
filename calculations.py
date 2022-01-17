# this needs the_list and count in order to work
# the calculations
import statistics

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
