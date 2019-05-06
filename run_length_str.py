# Have the function RunLength(str) take the str parameter being passed and return a compressed version of the string using the Run-length
# encoding algorithm. This algorithm works by taking the occurrence of each repeating character and outputting that number 
# along with a single character of the repeating sequence. For example: "wwwggopp" would return 3w2g1o2p. 
# The string will not contain any numbers, punctuation, or symbols. 


def RunLength(s):

	encoding = ''
	i = 0

	while i < len(s):
		count = 1

		try:
			while(s[i] == s[i+1]):
				count+=1
				i+=1
		except:
			pass

		encoding += str(count) + s[i]
		i+=1

	return encoding


test = "aabbcde"

print(RunLength(test))

