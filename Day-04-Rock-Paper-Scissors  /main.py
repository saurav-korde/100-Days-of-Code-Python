import random
rock = '''
    _______
---'   ____)
      (_____)
      (_____)
      (____)
---.__(___)
'''

paper = '''
    _______
---'   ____)____
          ______)
          _______)
         _______)
---.__________)
'''

scissors = '''
    _______
---'   ____)____
          ______)
       __________)
      (____)
---.__(___)
'''

player = int(input("What do you choose? Type 0 for Rock, 1 dor Paper or 2 for scissors\n"))
if player >= 3 or player < 0:
    print("You typed an invalid number, you lose!")
else:
    if player == 0:
        print(rock)
    elif player == 1:
        print(paper)
    else:
        print(scissors)


print("Computer Chose:")

computer = random.randint(0,2)
# print(computer)
if computer == 0:
    print(rock)
elif computer == 1:
    print(paper)
else:
    print(scissors)

#result
if (player == 0 and computer == 2) or (player == 1 and computer == 0) or (player == 2 and computer == 1):
    print("You win!")
elif computer == player:
    print("It's a draw!")
else:
    print("You lose!")