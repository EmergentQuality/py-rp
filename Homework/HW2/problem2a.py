# Jeffrey Liss
# v1.1 - a little cleaner
import pdb
import random

rexmoods = dict()

for mood in ['a','b','h','t']:
	mood = random.choice([True,False])

# is rex a(ngry), b(ored), h(ungry), t(ired)?
print("Angry={}, Bored={}, Hungry={}, Tired={}".format(a,b,h,t)) # for debugging / testing purposes.

def eat(meal):
	print("T-Rex: Yummy",meal +"!")

# if a and b and h:
# 	eat("Triceratops")
# elif t and h:
# 	eat("Iguanadon")
# elif h and b:
# 	eat("Stegasaurus")
# elif a and b:
# 	print("T-Rex versus Velociraptor... FIGHT!!")
# elif a or b:
# 	print("T-Rex roars: Rawr!")
# elif t:
# 	print("T-rex: Zzzzzz...")
# else:
# 	print("T-Rex: *grins*")

if a or b:
	if a and b and h:
		eat("Triceratops")
	elif a and b:
		print("T-Rex versus Velociraptor... FIGHT!!")
	elif h and b:
		eat("Stegasaurus")
	else:
		print("T-Rex roars: Rawr!")
elif t:
	if t and h:
		eat("Iguanadon")
	else:
		print("T-Rex: Zzzzzz...")
