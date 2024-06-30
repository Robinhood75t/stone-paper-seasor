'''
1 for rock
-1 for paper
0 for seasor
'''
import random
computer  = random.choice([-1,0,1])
youstr = input("enter your choice : ")

youdict = {"rock" : 1,"paper" : -1,"seasor" : 0}
reversedict = {1 : "rock",-1: "paper",0 : "seasor"}
you = youdict[youstr]

print(f"you chose {reversedict[you]}\ncomputer chose {reversedict[computer]}")
if(computer == you):
    print("draw")
else:
    if(computer == -1 and you == 1):
        print("YOU lose! ")
    elif(computer == -1 and you == 0):
        print("YOU win! ")
    elif(computer == 1 and you == -1):
        print("YOU win! ")
    elif(computer == 1 and you == 0):
        print("YOU lose! ")
    elif(computer == 0 and you == -1):
        print("YOU lose! ")
    elif(computer == 0 and you == 1):
        print("YOU win! ")
    else: 
        print("sahi khelo yar")



