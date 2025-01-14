import random
taget = random.randint(1,30)
attempts = 0

while True:
    guess = int(input("Guess the number 1부터 30까지 숫자 중: "))
    attempts += 1
    if guess == taget:
        print(f"Correct! That was the number {attempts} attempts")
        break   
    elif guess < taget:
        print("The number is higher")
    else:
        print("The number is lower")    
        