""" Jeffrey Liss
"""

def set_offense():
    offense = True

def get_offense():
    return offense

def set_defense():
    defense = True

    def set_rule_changes():
        return True

    def get_rule_changes():
        return rule_changes

    if offense and defense:
        set_rule_changes()
        return defense, get_rule_changes()

def get_defense():
    return defense

set_offense()
set_defense()

offense = get_offense()
defense, rule_changes = set_defense()

print("\nHow are the Jags doing?\n")
print("We have offense:", offense)
print("We have defense:", defense)
print("We have some rule changes:", rule_changes)

if offense and defense and rule_changes:
    print("🏈🏈🏈We're going to the superbowl!🏈🏈🏈")
else:
    print(
        "I can't predict the future, but no, the Jaguars will never win the \
        superbowl")
