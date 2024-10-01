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
print('Type 1 for Rock')
print('Type 2 for Paper')
print('Type 3 for Scissor')
choice = input('What do you choose ?')
user_choice = int(choice)
user_choice = user_choice - 1 
choice_list = [rock,paper,scissors]
user_input = choice_list[user_choice]
computer_choice = random.randint(0,len(choice_list)-1)
computer_input = choice_list[computer_choice]
print('User input : ')
print(user_input)
print('Computer input : ')
print(computer_input)
if user_choice>=3 or user_choice<0 :
    print('Invalid input')
if user_choice==2 and computer_choice==0:
    print('You lose XXX')
elif user_choice==0 and computer_choice==2:
    print('You Win !!!')
elif user_choice==computer_choice:
    print('Tie ---')
elif user_choice<computer_choice:
    print('You lose XXX')
else:
     print('You Win !!!!')