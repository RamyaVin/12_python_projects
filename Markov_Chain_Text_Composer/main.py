import random 
import math
def play():
    user=input("what is you choise 'r' for rock , 'p' for paper, 's' for scissor ")
    user=user.lower()
    while user not in (['r','p','s']):
        print("input is incorrect re enter")
        user=input("what is you choise 'r' for rock , 'p' for paper, 's' for scissor ")
        
    user=user.lower() 
    computer=random.choice(['r','p','s'])
    if user==computer:
        return(0,user,computer) 
    #r>s,p>r,s>p
    if is_win(user,computer):
        return(1,user,computer) 
    return (-1,user,computer) 

def is_win(player,opponent):
    if((player== 'r'and opponent== 's') or (player== 'p' and opponent== 'r') or (player== 's' and opponent== 'p')):
        return True
    return False

def play_best_of(n):
    player_wins = 0 
    opponent_wins = 0
    wins_necessary = math.ceil(n/2)
    while player_wins < wins_necessary and opponent_wins < wins_necessary:
        result,user,computer = play()
        if result == 0:
            print("It is a tie")
        elif result == 1:
            player_wins += 1
            print("You choose {}, computer choose {} You won!!! \n".format(user, computer))
        else:
            opponent_wins += 1
            print("You choose {}, computer choose {} You lost \n".format(user, computer))
    if player_wins>opponent_wins:
        print("You won best of {} matches \n".format(n))
    else:
        print("You lost best of {} matches \n".format(n))

if __name__ == '__main__':
    play_best_of(3) 
