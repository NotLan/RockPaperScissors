import random
from time import sleep

print("Lets play a game of Rock Paper Scissor")

user_selection = input("Choose your weapon for battle!(Rock/Paper/Scissor):")

options = (
    "Rock",
    "Paper",
    "Scissor"
)

outcomes = {
    "Rock Paper": "You Lose",
    "Rock Rock": "You Tie",
    "Rock Scissor": "You Win",
    "Paper Rock": "You Win",
    "Paper Paper": "You Tie",
    "Paper Scissor": "You Lose",
    "Scissor Paper": "You Win",
    "Scissor Rock": "You Lose",
    "Scissor Scissor": "You Tie"
}

count = 0
while user_selection not in options and count != 5:
    user_selection = input("Wrong choice, Choose your weapon for battle!(Rock/Paper/Scissor):")
    count += 1
    if count == 5:
        print("You are so funny... \n -No one ever")
        exit()

computer_selection = random.choice(options)

dict_value = f"{user_selection + ' ' + computer_selection}"

fist = (""" 
       ,--.--._
------" _, \___)
        / _/____)
        \//(____)
------\     (__)
       `-----" 
       """)

boom = ("""
     _.-^^---....,,--       
 _--                  --_  
<                        >)
|                         | 
 \._                   _./  
    ```--. . , ; .--'''       
          | |   |             
       .-=||  | |=-.   
       `-=#$%&%$#=-'   
          | ;  :|     
 _____.,-#%&$@%#&#~,._____
""")

print("\n 3 . . ."
      f"\n {fist} ")
sleep(1)
print("\n 2 . . ."
      f"\n {fist} ")
sleep(1)
print("\n 1 . . ."
      f"\n {fist} ")
sleep(1)
print("\n GO!"
      f"\n {boom}")
sleep(1)
print(f"\n The computer chose {computer_selection}")
sleep(1)
print(f"\n {outcomes.get(f'{dict_value}')}")
