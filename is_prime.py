'''
Have the function PrimeTime(num) take the num parameter being passed and return the string true if the parameter is a prime number, 
otherwise return the string false. The range will be between 1 and 2^16. 
'''

import math

def PrimeTime(n):
	_sq = int(math.sqrt(n))
	for i in range(2, _sq):
		if n % i == 0:
			return False
	return True


print(PrimeTime(38047))
