import re


def the_user_input():
	input_is = str(input("Please enter the word or sentence you would like to check:"))
	remove_special_char = re.sub('[^A-Za-z0-9]+','',input_is)
	user_input = remove_special_char.lower().replace(' ', '')
	return user_input

def reverse_inpute(inp1):
	reversed_inp =[]
	word_len = len(inp1)
	for letter in inp1:
		word_len -= 1
		reversed_inp.append(inp1[word_len])
	return reversed_inp


def user_inpute_list(userinput):
	palindrome = []
	for l in userinput:
		palindrome.append(l)
	return palindrome


v1 = the_user_input()
v2 = reverse_inpute(v1)
v3 = user_inpute_list(v1)

if v3 == v2:
	print(v1, "is a palindrome.")
else:
	print(v1, 'is not a palindrome')
