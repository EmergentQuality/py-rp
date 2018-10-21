""" Jeffrey Liss
"""
def get_offense():
    offense = True
    return offense


def get_defense():
    defense = True

    def get_rule_changes():
        return True

    if offense and defense:
        return defense, get_rule_changes()


offense = get_offense()
defense, rule_changes = get_defense()

print("How are the Jags doing?\n")
print("We have offense:", offense)
print("We have defense:", defense)
print("We have some rule changes:", rule_changes)

if offense and defense and rule_changes:
    print("🏈🏈🏈We're going to the superbowl!🏈🏈🏈")
else:
    print(
        "I can't predict the future, but no, the Jaguars will never win the \
        superbowl")
