# how to find prime numbers within a list:
# a prime number is a number that only has 2 factors such as 13. the only factors are 1 and 13 
# bc 13*1 = 13

#import sympy
#the_list = []
#print(sympy.isprime(90))
# Python program to check if
# given number is prime or not

num = 12

# If given number is greater than 1
if num > 1:

	# Iterate from 2 to n / 2
	for i in range(2, int(num/2)+1): # this is 12/ 2 = 6. 6 + 1 = 7
        # so if 12 % 

		# If num is divisible by any number between
		# 2 and n / 2, it is not prime
		if (num % i) == 0:
			print(num, "is not a prime number")
			break
	else:
		print(num, "is a prime number")

else:
	print(num, "is not a prime number")

