'''
Have the function ArrayRotation(arr) take the arr parameter being passed which will be an array of non-negative integers and 
circularly rotate the array starting from the Nth element where N is equal to the first integer in the array. 
For example: if arr is [2, 3, 4, 1, 6, 10] then your program should rotate the array starting from the 2nd position 
because the first element in the array is 2. The final array will therefore be [4, 1, 6, 10, 2, 3], and your program 
should return the new array as a string, so for this example your program would return 4161023. 
The first element in the array will always be an integer greater than or equal to 0 and less than the size of the array. 
'''

def JoinArrayIntoString(arr):
	# method returning string created from next elements of array
	return "".join(str(i) for i in arr)


def ArrayRotation(arr):
	if (arr[0] == 0) or (arr[0] == len(arr)):
		return JoinArrayIntoString(arr)
	else:
		n = arr[0]
		arr = arr[n:] + arr[:n]
		return JoinArrayIntoString(arr)



arr = [1,2,3,4]
print(ArrayRotation(arr))