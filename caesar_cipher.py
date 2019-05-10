'''
Have the function CaesarCipher(str,num) take the str parameter and perform a Caesar Cipher shift on it using the num parameter 
as the shifting number. A Caesar Cipher works by shifting each letter in the string N places down in the alphabet (in this case N will be num). 
Punctuation, spaces, and capitalization should remain intact. For example if the string is "Caesar Cipher" and num is 2 the output should be 
"Ecguct Ekrjgt". 
'''

import string

def CaesarCipher(s,n):
	# case for lowercase letters
	alphabet_lower = string.ascii_lowercase

	# case for uppercase letters
	alphabet_upper = string.ascii_uppercase

	# shift both alphabets to the right by n 
	shifted_alphabet_lower = alphabet_lower[n:] + alphabet_lower[:n]
	shifted_alphabet_upper = alphabet_upper[n:] + alphabet_upper[:n]

	# transition all the letters from alphabet to shifted alphabet in plaintext input
	coded_string = str.maketrans(alphabet_lower, shifted_alphabet_lower)
	s = s.translate(coded_string)
	# print(s.translate(coded_string))
	coded_string = str.maketrans(alphabet_upper, shifted_alphabet_upper)
	s = s.translate(coded_string)

	return s

print(CaesarCipher('Ab cd', 2))