# Write your code here
import random
def check_winner(player, computer):
    score = 0
    combinations = {'rock':['paper', 'air', 'water', 'dragon', 'devil', 'lightning', 'gun'],
                    'fire':['rock', 'air', 'water', 'dragon', 'devil', 'lightning', 'gun'],
                    'scissors':['rock', 'fire', 'water', 'dragon', 'devil', 'lightning', 'gun'],
                    'snake':['rock', 'fire', 'scissors', 'dragon', 'devil', 'lightning', 'gun'],
                    'human':['rock', 'fire', 'scissors', 'snake', 'devil', 'lightning', 'gun'],
                    'tree':['rock', 'fire', 'scissors', 'snake', 'human', 'lightning', 'gun'],
                    'wolf':['rock', 'fire', 'scissors', 'snake', 'human', 'tree', 'gun'],
                    'sponge':['rock', 'fire', 'scissors', 'snake', 'human', 'tree', 'wolf'],
                    'paper':['sponge', 'fire', 'scissors', 'snake', 'human', 'tree', 'wolf'],
                    'air':['sponge', 'paper', 'scissors', 'snake', 'human', 'tree', 'wolf'],
                    'water':['sponge', 'paper', 'air', 'snake', 'human', 'tree', 'wolf'],
                    'dragon':['sponge', 'paper', 'air', 'water', 'human', 'tree', 'wolf'],
                    'devil':['sponge', 'paper', 'air', 'water', 'dragon', 'tree', 'wolf'],
                    'lightning':['sponge', 'paper', 'air', 'water', 'dragon', 'devil', 'wolf'],
                    'gun':['sponge', 'paper', 'air', 'water', 'dragon', 'devil', 'sponge'],
                    }
    if player == computer:
        print(f"There is a draw {player}")
        score += 50
    elif computer in combinations[player]:
        print(f'Sorry, but computer chose {computer}')
    else:
        print(f"Well done. Computer chose {computer} and failed")
        score += 100
    return score

 
name = input('Enter your name: ')
print('Hello,', name)  
score = 0
print("\nRock-Paper-Scissors")
print("Which game would you like to play ?")
print("1 for Classic")
print("2 for Extended\n")
while True:
    menu = input("Enter Option : ")
    if menu == '1':
        options = ['rock', 'paper', 'scissors']
        break
    elif menu == '2':
        options = ['rock', 'paper', 'scissors', 'fire', 'snake', 'human', 'tree', 'wolf',
                   'sponge', 'air', 'water', 'dragon', 'devil', 'lightning', 'gun']
        break
    else:
        print("Enter valid Option")

print("Okay, let's start\nHere is the options.\n")
print(options)
print("\nEnter your choice.\n'!rating' for rating,\n'!exit' for exit the game.\n")
while True:
    
    option = random.choice(options)
    choice = input("Enter your choice : ")
    if choice == '!exit':
        print('Bye!')
        break
    elif choice == '!rating':
        print("Your rating:", score)
    elif choice not in options:
        print("Invalid input")
    else:
        score += check_winner(choice, option)
    print()
