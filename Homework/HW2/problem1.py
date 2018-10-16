import random as rnd

time = rnd.randint(0,23)
print("The time is:", time)

if time < 9:
	print("Good morning, time to wake up and smell the coffee!")
elif time >= 9 and time <= 16:
	print("Work work work... when will it end?")
elif time <20:
	print("How did it get so late so soon?")
elif time <22:
	print("A day without sunshine is like, you know, night.")
else:
	print("Burning the midnight oil!")