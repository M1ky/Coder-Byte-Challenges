'''
Have the function Consecutive(arr) take the array of integers stored in arr and return the minimum number 
of integers needed to make the contents of arr consecutive from the lowest number to the highest number. 
For example: If arr contains [4, 8, 6] then the output should be 2 because two numbers need to be added 
to the array (5 and 7) to make it a consecutive array of numbers from 4 to 8. 
Negative numbers may be entered as parameters and no array will have less than 2 elements. 
'''

def Consecutive(arr):

	minimum = arr[0]
	maximum = arr[-1]
	new_arr = []

	for i in arr:
		if i < minimum:
			minimum = i
		if i > maximum:
			maximum = i


	for i in range(minimum, maximum+1):
		new_arr.append(i)

	print(new_arr)

	for i in arr:
		new_arr.remove(i)

	return len(new_arr)



test = [4, 8, 6]
test = [5,10,15]
test = [-2,10,4]
print(Consecutive(test))
