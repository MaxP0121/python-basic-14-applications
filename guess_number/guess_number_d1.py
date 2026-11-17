import random
final_ans = random.randint(1,100)
print ("Guessing number game start")
selected = input("Choose a number")
current_range=[1,100]

while True:
    if selected > 100:
        print("This is too big")
        selected = input("Choose a number again")
        continue

    if selected < 1:
        print("This is too small")
        selected = input("Choose a number again")
        continue

    if selected == final_ans:       #=是賦值 要寫等於的話是用==
        print("you are a genius")
        break

    if selected < final_ans:


    if selected > final_ans:




