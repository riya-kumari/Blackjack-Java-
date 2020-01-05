""" Created by Riya Kumari """
import random
import inspect



#     The deck of cards is a list with the values and suites of each card
#     Example : [2 of Hearts] 
values = ['2','3','4','5','6','7','8','9','10','Jack','Queen','King','Ace']
suites = ['Hearts', 'Clubs', 'Diamonds', 'Spades']
deck = [[v + ' of ' + s,v] for s in suites for v in values] 

# All other necessary variables are initialized here
bet = 0
playersSum = 0
playersDeck = []
dealersSum = 0
dealersDeck = []

cardsLeft = 52
 


def reinitializeVariables():
    global deck
    deck = [[v + ' of ' + s,v] for s in suites for v in values] 
    global bet
    bet = 0
    global playersSum 
    playersSum = 0
    global dealersSum
    dealersSum = 0
    global playersDeck
    playersDeck = []
    global dealersDeck
    dealersDeck = []
    global cardsLeft
    cardsLeft = 52
    


#Starting message which shows up the first time the player plays the game
def gameLoop():
    global bet
    print("********************************")
    print("\n"+"Blackjack Console Version 1.0")
    users_input = input("To start - enter in the amount you are betting. (Please do not enter without putting a value down)    " + "\n" )
    bet = users_input
    while users_input <5 :
        users_input = input("Minimum amount you can bet is 5. Bet again.")

# Takes a card from the deck(list) and returns the value of it
def getValue(card):
    val = "int"
    try:
        val = int(card[1]) 
        return val
    except ValueError: 
        return 10

# All cards picked pass through this method. They keep their value if they aren't an Ace. If it is an Ace then it can either be a 10 or 1 depending on whichever situation benefits the player. 
def checkIfAce(card, currentValue):
    if 'Ace' in card:
        if(playersSum + 10) < 21:
            return 10
        if playersSum + 1 < 21:
            return 10
        else:
            return 10   
    else:
        return currentValue



# Updates PlayerSum, draws a card from the deck and adds it to playersDeck
def drawCardPlayer():
    global playersSum
    global cardsLeft
    index = random.randint(1,cardsLeft)
    cardsLeft -=1
    c = deck[index]
    playersDeck.append(c)
    value = getValue(deck[index])
    value = checkIfAce(c, value)
    playersSum += value
    del deck[index]

    
# Updates dealersSum, draws a card from the deck and adds it to dealersDeck
def drawCardDealer():
    global dealersSum
    global cardsLeft
    index = random.randint(1,cardsLeft)
    cardsLeft -=1
    c = deck[index]
    dealersDeck.append(c)
    value = getValue(deck[index])
    dealersSum += value
    del deck[index]

def endOfGameScene():
    users_input = raw_input("Would you like to play again?")
    if users_input == "yes":
        runSequence()
    else:
        print("Thanks for playing.")
        exit()

# Player wins if they are closer to 21 than the dealer, or if the dealer is above 21 and they aren't or player is 21 exact
# It's a tie if player has same as dealer or both are above 21
def computeScore():
    global playersSum
    if (playersSum < 21 and dealersSum < 21 and playersSum>dealersSum) or (playersSum<21 and dealersSum>21) or (playersSum ==21 and dealersSum!=21 ) :
        print("Congratulations you have won!!!")
    elif (playersSum ==  dealersSum) or (playersSum > 21 and dealersSum > 21) :
        print("Well its a tie.")          
    else :
        print("You lost $"+str(bet)+"You can play again to win all your money back or even more.")
    endOfGameScene()


# Displays dealers cards when the player chooses to stand or loses
def displayDealersCards():
    print("\n" + "Dealers cards : ")
    for x in range(len(dealersDeck)):
        print (dealersDeck[x])
        print("Dealers total : " + str(dealersSum))

# Displays Players cards as they keep drawing cards
def displayPlayersCards():
    print("\n" + "Your cards : ")
    for x in range(len(playersDeck)):
        print (str(playersDeck[x]))
        print ('Your total : ' + str(playersSum))

# Asks player if they choose to hit or stand. 
# If hit : draws another card for player and one for dealer
def hitOrStand():
    
    global playersSum, dealersSum
    i = ""
    while(i!="stand" and playersSum<21):
        print("********************************")
        i = raw_input("Would you like to hit or stand? (Hit means to draw another card; Stand means to not.)" + "\n")
        if i == "hit":
            drawCardPlayer()
            drawCardDealer()
            displayPlayersCards()
        else: 
            break
    displayDealersCards()
    print("\n")
    computeScore()

    

# The sequence that is run when player starts playing the game.   
def runSequence():
    reinitializeVariables()
    gameLoop()
    drawCardPlayer()
    drawCardDealer()
    displayPlayersCards()
    hitOrStand()
    endOfGameScene()

# This method gets the game started the first time. 
runSequence()



# To run : python main.py





