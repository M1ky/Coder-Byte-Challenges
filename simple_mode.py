'''
Have the function SimpleMode(arr) take the array of numbers stored in arr and return the number that appears most frequently (the mode). 
For example: if arr contains [10, 4, 5, 2, 4] the output should be 4. If there is more than one mode return the one 
that appeared in the array first (ie. [5, 10, 10, 6, 5] should return 5 because it appeared first). 
If there is no mode return -1. The array will not be empty. 
'''

def SimpleMode(arr):
	# dictionary that will store values from input array
	counter = {}

	# loop to count occurences of numbers in array 
	for i in range(len(arr)):
		nr = arr[i]

		if nr in counter:
			counter[nr] += 1
		else:
			counter[nr] = 1

	# dictionary that will store mode of input array
	ans = {"number": '', "count": 1}

	# loop through counter dictionary to find first mode of input array
	for x in counter:
		if (counter[x] > ans["count"]):
			ans["count"] = counter[x]
			ans["number"] = x

	# if there are no duplicates return -1, else return first mode that appeard in input array
	if ans["count"] == 1:
		return -1
	else:
		return ans["number"]





test = [2,5,10,10,6,5]
print(SimpleMode(test))