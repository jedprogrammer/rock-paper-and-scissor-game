import random

gamer_choice = input("What do you choose? Type 0 for Rock, 1 for Paper or 2 for Scissors\n ")
if gamer_choice == "0":
    #Rock
    print('''

      _______
        ---'   ____)
              (_____)
              (_____)
              (____)
        ---.__(___)
    ''')
    #Paper
elif gamer_choice == "1":
    print("""
     _______
---'    ____)____
           ______)
          _______)
         _______)
---.__________)
""")
    #Scissor
elif gamer_choice == "2":

    print("""
    _______
---'   ____)____
          ______)
       __________)
      (____)
---.__(___)
""")









computer_choice = random.randint(0,2)
if computer_choice == 0:
    print("Computer choose:")
    # Rock
    print('''

         _______
           ---'   ____)
                 (_____)
                 (_____)
                 (____)
           ---.__(___)
       ''')
    #Paper
elif computer_choice== 1:
    print("Computer choose:")
    print("""
     _______
---'    ____)____
           ______)
          _______)
         _______)
---.__________)
""")
    #Scissor
elif computer_choice == 2:
    print("Computer choose:")
    print("""
    _______
---'   ____)____
          ______)
       __________)
      (____)
---.__(___)
""")

if computer_choice == 0 and gamer_choice == "2":
    print("Computer won")
elif computer_choice == 1 and gamer_choice == "0":
    print("Computer won")
elif computer_choice == 2 and gamer_choice == "1":
    print("Computer won")
elif gamer_choice == "0" and computer_choice == 2:
    print("You won")
elif gamer_choice == "1" and computer_choice == 0:
    print("You won")
elif gamer_choice == "2" and computer_choice == 1:
    print("You won")
else:
    print("Draw")