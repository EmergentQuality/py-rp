# Jeffrey Liss
# v1.1 - a little cleaner
import pdb
import random
 
a, b, h, t = [random.choice([True, False]) for v in range(4)]

# is rex a(ngry), b(ored), h(ungry), t(ired)?
print(f"\nAngry={a}, Bored={b}, Hungry={h}, Tired={t}\n\n") # for debugging / testing purposes.

def eat(meal):
	print("T-Rex: Yummy",meal +"!\n")

if a or b:
	if a and b and h:
		eat("Triceratops")
	elif a and b:
		print("T-Rex versus Velociraptor... FIGHT!!\n")
	elif h and b:
		eat("Stegasaurus")
	else:
		print("T-Rex roars: Rawr!\n")
elif t:
	if t and h:
		eat("Iguanadon")
	else:
		print("T-Rex: Zzzzzz...\n")
else: 
	print("T-Rex *grins*\n")