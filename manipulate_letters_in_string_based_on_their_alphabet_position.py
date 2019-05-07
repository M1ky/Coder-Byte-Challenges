def LetterChanges(str): 
	alph = "abcdefghijklmnopqrstuvwxyz"
	out = ""


	for char in str:
		char = char.lower()
		if char in alph:
			indx = alph.index(char)+1
			char = alph[indx]

			if char in 'aeiou':
				char = char.upper()

			out+=char
		else:
			out+=char

	return out


test = "hello world"

print(LetterChanges(test))





