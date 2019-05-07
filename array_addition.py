import itertools

# Have the function ArrayAdditionI(arr) take the array of numbers stored in arr and return the string true if any combination of numbers in the array 
# (excluding the largest number) can be added up to equal the largest number in the array, otherwise return the string false. 
# For example: if arr contains [4, 6, 23, 10, 1, 3] the output should return true because 4 + 6 + 10 + 3 = 23. 
# The array will not be empty, will not contain all the same elements, and may contain negative numbers. 


def ArrayAdditionI(arr):

	_max = max(arr)
	arr.remove(_max)
	_comb = []

	for i in range(len(arr)+1):
		for cb in itertools.combinations(arr, i):
			_comb.append(cb)

	for i in _comb:
			if sum(int(x) for x in i) == _max:
				return True
	
	return False

test = [3,5,-1,8,12]

print(ArrayAdditionI(test))
