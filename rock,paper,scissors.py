import random
computer = random.choice([-1,0,1])
youstr = input("enter a choice: ")
youdict = {"r" : 1 ,"p" : -1 , "s" : 0}
reversedict = {1 : "rock" , -1 : "paper" , 0 : "scissors"} 
you = youdict[youstr] 
print(f"you choice {reversedict[you]} and computer choice is {reversedict[computer]}")
if computer == you:
    print("match draw")
elif (you == 1 and computer == 0) or (you == -1 and computer == 1) or (you == 0 and computer == -1):
    print("you win")
else:
    print("you lose")
