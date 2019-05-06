# Have the function SecondGreatLow(arr) take the array of numbers stored in arr and return the second lowest and second greatest numbers, 
# respectively, separated by a space. For example: if arr contains [7, 7, 12, 98, 106] the output should be 12 98. 
# The array will not be empty and will contain at least 2 numbers. It can get tricky if there's just two numbers! 


def SecondGreatLow(arr):
	arr.sort()

	if len(arr) == 2:
		return ("{} {}".format(arr[1], arr[0]))
	else:
		lowest = arr[0]
		highest = arr[-1]
		
		no_duplicate_arr = [x for x in arr if x != lowest and x != highest]
		no_duplicate_arr.append(lowest)
		no_duplicate_arr.append(highest)
		no_duplicate_arr.sort()

		return ("{} {}".format(no_duplicate_arr[1], no_duplicate_arr[-2]))





test = [42,42,1,198,198]
test = [1,2,2,3]
print(SecondGreatLow(test))