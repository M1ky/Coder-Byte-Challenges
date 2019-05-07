'''
Have the function StringScramble(str1,str2) take both parameters being passed and return the string true if a portion of str1 
characters can be rearranged to match str2, otherwise return the string false. For example: if str1 is "rkqodlw" and str2 is "world" 
the output should return true. Punctuation and symbols will not be entered with the parameters. 
'''

def StringScramble(s1, s2):

	# creating a list that will store characters of string 2
	_list = list(s2)

	# loop checking if characters from string 1 are in list o characters of string 2. If they are, remove character from list
	for char in s1:
		if char in _list:
			_list.remove(char)

	# if list is empty -> characters from string 1 fill string 2 completely return True
	if not _list:
		return True

	return False


print(StringScramble("cdore", "coderr"))