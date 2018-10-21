state_capitals = {
    'Maryland': 'Annapolis',
    'Massachusetts': 'Boston',
    'Montana': 'Helena',
    'New Hampshire': 'Concord'
}


def dict_flip(dict):
    for i in dict.items():
        yield {v: k for k, v in dict.items()}


def dict_lookup(dict):
    for k, v in dict.items():
        print('State: {}\nCapital: {}\n\n'.format(k, v))


print(dict_lookup(state_capitals))
reversed_states = next(dict_flip(state_capitals))

for k, v in reversed_states.items():
    print('Capital: {}\nState: {}\n\n'.format(k, v))
