import sympy
for number in the_list:
	prime_checker = (sympy.isprime(the_list))
	if prime_checker == False:
		print(f'{number} is not a prime')
	elif prime_checker:
		print(f'{number} is a prime')



