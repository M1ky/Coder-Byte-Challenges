'''
Have the function CountingMinutesI(str) take the str parameter being passed which will be two times 
(each properly formatted with a colon and am or pm) separated by a hyphen and return the total number of minutes between the two times. 
The time will be in a 12 hour clock format. For example: if str is 9:00am-10:00am then the output should be 60. 
If str is 1:00pm-11:00am the output should be 1320. 
'''

import datetime

def CountingMinutesI(str):

	first_hour, second_hour = str.split('-')

	first_time = datetime.datetime.strptime(first_hour, "%I:%M%p")
	second_time = datetime.datetime.strptime(second_hour, "%I:%M%p")

	if second_time < first_time:
		second_time += datetime.timedelta(days=1)

	timediff = second_time - first_time

	return int(timediff.total_seconds()/60)

test = "9:00am-10:00am"
test = "12:30pm-12:00am"
print(CountingMinutesI(test))