import collections

'''
Have the function LetterCountI(str) take the str parameter being passed and return the first word with the greatest number of repeated letters. 
For example: "Today, is the greatest day ever!" should return greatest because it has 2 e's (and 2 t's) and it comes before ever which also has 2 e's. 
If there are no words with repeating letters return -1. Words will be separated by spaces. 

'''

def LetterCountI(str):

	max_occurences = 0
	word_with_max_occurences = ''

	for word in str.split():
		cnt = collections.Counter(word)

		if cnt.most_common()[0][1] > max_occurences:
			max_occurences = cnt.most_common()[0][1]
			word_with_max_occurences = word

	if max_occurences < 2:
		return -1
	return word_with_max_occurences






test = "Hello worlld apple"
test2 = 'Argument goes here'

print(LetterCountI(test2))