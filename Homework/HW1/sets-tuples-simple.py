set_1 = {'apples', 'bananas', 'pears'}
set_2 = {'bananas', 'apples', 'pears'}
set_3 = {'kiwi', 'bananas', 'apples'}
set_4 = {'kiwi', 'bananas', 'apples', 'steak'}

# all = [set_1, set_2, set_3, set_4]

def set_equality(a, b):
    for item in a:
        if item in b:
            return True
        else:
            return False
