import time
import random

# Retrieves players
def getPlayers():
    listOfPlayersToSplit = input("Please enter the names of the player, each seperated by a space: ")
    arr = listOfPlayersToSplit.split()
    return arr

# The fake wheel motion in action
def choose_lucky_winner(players):
    count = 0
    delay = 0.01
    luckyWinner = random.choice(players)
    current_choice = luckyWinner
   
    def spin():
        print(delay)
        count +=1
        current_choice = players[count%len(players)]
        print(current_choice, end='\r')
        delay = delay + 0.02
        time.sleep(delay)
        
    while delay <= 0.41:
        spin()
        
    # Fakes wheel spinning until it gets to the winner
    while current_choice != luckyWinner:
        spin()

    print("The lucky winner value is{}".format(luckyWinner))
    
players = getPlayers()
choose_lucky_winner(players)
