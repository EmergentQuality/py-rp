set_1 = {'apples', 'bananas', 'pears'}
set_2 = {'bananas', 'apples', 'pears'}
set_3 = {'kiwi', 'bananas', 'apples'}
set_4 = {'kiwi', 'bananas', 'apples', 'steak', 'potato'}


def set_equality(a, b):
    return bool(b <= a and a <= b)


print(set_equality(set_1, set_2))
print(set_equality(set_1, set_3))
print(set_equality(set_1, set_4))
print(set_equality(set_4, set_3))
print(set_equality(set_3, set_4))
