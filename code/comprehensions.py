nums = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]

my_list = [(letter, num) for letter in 'abcd' for num in range(4)]
print(f'\nList of tuples: {my_list}')

my_dict = {letter: num for letter in 'abcd' for num in range(4)}
print(f'\nDictionary: {my_dict}')

