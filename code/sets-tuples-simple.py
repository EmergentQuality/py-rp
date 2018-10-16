set_1 = {'apples', 'bananas', 'pears'}
set_2 = {'bananas', 'apples', 'pears'}
set_3 = {'kiwi', 'bananas', 'apples'}
set_4 = {'kiwi', 'bananas', 'apples', 'steak'}

# all = [set_1, set_2, set_3, set_4]


def set_equality(a, b):
    if len(a) != len(b):
        return False
    for item in a, b:
        return bool(a in b)


print(set_equality(set_1, set_2))
print(set_equality(set_1, set_3))
print(set_equality(set_1, set_4))
print(set_equality(set_2, set_3))

musician = {'guitar': 'robby', 'harmonica': 'john lennon', 'bass': 'john paul \
            jones'}

for instrument, musician in musician.items():
    print(f'{instrument}, played by {musician}')
