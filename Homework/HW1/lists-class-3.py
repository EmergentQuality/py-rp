family = ['Jeff', 'Zina', 'Ben', 'Owen', 'Myra', 'Emma', 'Fionna']

#for name in people:
#    print(f"Hello, {name}!")

for index in range(len(family)):
    family[index] = "passenger-{}".format(index)

print(family)

for name in range(len(family)):
    print(name)
