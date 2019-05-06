def LetterChanges(str): 
	alph = "abcdefghijklmnopqrstuvwxyz"
	out = ""


	for char in str:
		char = char.lower()
		if char in alph:
			# print(alph.index(char))
			indx = alph.index(char)+1
			char = alph[indx]

			if char in 'aeiou':
				char = char.upper()

			out+=char
		else:
			out+=char

	return out


test = "hello world"

# test1 = "abcd3215"
# test2 = "abcd:/adf"
# test3 = "Helkj09123%234adsgasf"


print(LetterChanges(test))

# print(LetterChanges(test1))
# print(LetterChanges(test2))
# print(LetterChanges(test3))



