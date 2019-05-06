import math

# Have the function DivisionStringified(num1,num2) take both parameters being passed, divide num1 by num2, and return the result as a 
# string with properly formatted commas. If an answer is only 3 digits long, return the number with no commas (ie. 2 / 3 should output "1"). 
# For example: if num1 is 123456789 and num2 is 10000 the output should be "12,346". 


def DivisionStringified(num1, num2):

	num_to_string = ''

	whole = math.ceil(num1 / num2)
	rest = num1 % num2

	if len(str(whole))<4:
		return int(whole)
	else:
		whole = str((whole))
		rest = str(rest)
		if rest[0]:
			num_to_string = whole + "," + rest[0]
		if rest[1]:
			num_to_string += rest[1]
		try:
			num_to_string += rest[2]
		except:
			pass

		return num_to_string


print(DivisionStringified(6874,67))