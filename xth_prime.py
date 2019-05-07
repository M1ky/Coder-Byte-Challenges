'''
Have the function PrimeMover(num) return the numth prime number. The range will be from 1 to 10^4. 
For example: if num is 16 the output should be 53 as 53 is the 16th prime number. 
'''

import math
import time

def PrimeMover(n):

	primes = [2,3]
	if (0<n<3):
		return primes[n-1]
	elif (n>2):
		j=4
		isGo = True

		while isGo:
			isPrime = True
			_sq = math.ceil(math.sqrt(j)+1)
		
			for i in range(2, _sq):
				if j % i == 0:
					isPrime = False
					break

			if isPrime:
				if j not in primes:
						primes.append(j)
			
			if len(primes) == n:
				isGo = False
				return primes[n-1]

			j+=1
			# time.sleep(1)


print(PrimeMover(9))
