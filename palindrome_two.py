'''
Have the function PalindromeTwo(str) take the str parameter being passed and return the string true if the parameter is a palindrome, 
(the string is the same forward as it is backward) otherwise return the string false. The parameter entered may have punctuation
and symbols but they should not affect whether the string is in fact a palindrome. For example: "Anne, I vote more cars race Rome-to-Vienna" 
should return true. 
'''

def PalindromeTwo(s):
	# Write all characters from passed string to a new variable without special characters and make all letters lowercase
	# For python 2.6 you will need to use char.lower() instead of char.casefold()
	s="".join([char.casefold() for char in s if char.isalpha()])

	# check if string forwards is equal to string backwards
	if s == s[::-1]:
		return True
	else:
		return False


test="Anne, I vote more cars race Rome-to-Vienna"
print(PalindromeTwo(test))