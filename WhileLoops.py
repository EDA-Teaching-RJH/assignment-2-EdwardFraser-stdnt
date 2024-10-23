import random
rand = random.randrange(1,10)
c = int(input("Enter your guess: "))
print(input)
while rand != c:
    if c != rand:
        print("Try again")
        c = int(input("Enter your guess: "))
    else:
      break
print("You guessed correctly!")
