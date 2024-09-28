import random

n = random.randint(1, 100)
a = -1

attempts = 1
while (a != n):
    a = int(input("Guess the number (from 1 to 100): "))
    
    if (a < n):
        print ("Higher number please")
        attempts += 1

    elif (a > n):
        print ("Lower number please")
        attempts += 1

print (f"You guessed the number {n} correctly in {attempts} attempts.")

