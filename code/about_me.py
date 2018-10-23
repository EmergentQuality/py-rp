
myname = input("What is your name? ")
myfood = input("What is your favorite food? ")

with open("about_me.txt", mode='w') as f:
    f.write(f"Hello, {myname}!  Would you like some {myfood}?")
    
