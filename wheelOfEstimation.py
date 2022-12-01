import time
import random

spin_count = 0
spin_delay = 0.01

def increase_count():
    global spin_count 
    spin_count += 1

def increase_delay():
    global spin_delay
    spin_delay += 0.02    

# Retrieves players
def getPlayers():
    listOfPlayersToSplit = input("Please enter the names of the player, each seperated by a space: ")
    arr = listOfPlayersToSplit.split()
    return arr

# The fake wheel motion in action
def choose_lucky_winner(players):
    luckyWinner = random.choice(players)
    current_choice = luckyWinner
   
    def spin():
        current_choice = players[spin_count%len(players)]
        time.sleep(spin_delay)
        print(current_choice + "                    ", end='\r')
        increase_count()
        increase_delay()

    while spin_delay <= 0.41:
        spin()
        
    # Fakes wheel spinning until it gets to the winner
    while current_choice != luckyWinner:
        spin()
        time.sleep(1)

    print("The lucky winner is {}".format(luckyWinner))
    
players = getPlayers()
choose_lucky_winner(players)
