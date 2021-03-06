'''
Have the function SimpleSymbols(str) take the str parameter being passed and determine if it is an acceptable sequence by either returning the string true or false.
The str parameter will be composed of + and = symbols with several letters between them (ie. ++d+===+c++==a) 
and for the string to be true each letter must be surrounded by a + symbol. So the string to the left would be false. 
The string will not be empty and will have at least one letter. 
'''

def SimpleSymbols(str):


	alph = "abcdefghijklmnopqrstuvwxyz"
	x = True

	if (str[0] in alph) or (str[-1] in alph):
		return False

	for char in str:
		char = char.lower()

		if char in alph:
			indx_p = str.index(char)+1
			indx_m = str.index(char)-1

			if (str[indx_p] == '+') and (str[indx_m] == '+'):
				pass
			else:
				x = False

	return x

test = '"+d+=3=+s+"'
test2 = '+=+f++d'

print(SimpleSymbols(test2))

