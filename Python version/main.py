# BlackJack pseudocode
# Dealer Cards
# Player Cards
#to exit do control - option - m

# Methods
#     Deal Cards
#     Display Cards
#     Shuffle Cards

#     Sum of Dealer Cards
#     Sum of Player Cards
#     Compare the sums of card between the player and dealer
#     If the card is greater than 21 then BUST
#     If the card is less than 21 --> Option of Hit or Stay
#     If players sum <21 and greater than dealer, then player wins
#     If players sum < dealers sum then player loses

# Creating all the variables here
import random

#Deck of Cards
values = ['2','3','4','5','6','7','8','9','10','Jack','Queen','King','Ace']
suites = ['Hearts', 'Clubs', 'Diamonds', 'Spades']
deck = [[v + ' of ' + s,v] for s in suites for v in values] 
bet = 0
playersSum =0
playersDeck = [""],[""]
dealersSum = 0
dealersDeck = [""],[""]
p = [[]]
cardsLeft = 52


    
#Starting message
def gameLoop():
    print("********************************")
    print("Blackjack Console Version 1.0")
    users_input = input("To start - enter in the amount you are betting. (Please do not enter without putting a value down)    " + "\n" )
    while users_input <5 :
        users_input = input("Minimum amount you can bet is 5. Bet again.")

def getValue(card):
    val = "int"
    try:
        val = int(card[1]) 
        return val-1
    except ValueError: 
        return 10
    


def drawCardPlayer():
    global playersSum
    global cardsLeft
    index = random.randint(1,cardsLeft)
    cardsLeft -=1
    c = deck[index]
    playersDeck[0].append(c)
    value = getValue(deck[index])
    playersSum += value
    print(c) ; del deck[index]
    value = getValue(c)
    print("This is the sum",playersSum)
    print("********************************")

def drawCardDealer():
    global dealersSum
    global cardsLeft
    index = random.randint(1,cardsLeft)
    cardsLeft -=1
    c = deck[index]
    dealersDeck[0].append(c)
    value = getValue(deck[index])
    dealersSum += value
    del deck[index]
    print("This is the Dealers sum : ",dealersSum)
    print("********************************")

def computeScore():
    if(playerSum < 21 and dealersSum < 21) :
        if playersSum > dealersSum :
            print("Congratulations you have won!!!")
        elif playersSum < dealersSum :
            print("Awww. You lost. Thats sad. :()")
        else :
            print("Well its a tie.")
    
    elif(playerSum > 21 and dealersSum > 21):
            print("Awww. You lost. Thats sad. :()")

    else:
            print("Awww. You lost. Thats sad. :()")
    print("********************************")


        

    
    
def hitOrStand():
    global playersSum, dealersSum
    i = ""
    while(i!="stand" and playersSum<21 and dealersSum < 21):
        i = raw_input("Would you like to hit or stand? (Hit means to draw another card; Stand means to not.)" + "\n")
        if i == "hit":
            drawCardPlayer()
            drawCardDealer()
            displayCards()
        else: 
            computeScore()
    computeScore()

def displayCards():
    print("\n" + "Your cards : ")
    for x in range(len(playersDeck)):
        print (playersDeck[x])
        print "Your total : " , playersSum
    
    print("\n" + "Dealers cards : ")
    for x in range(len(dealersDeck)):
        print (dealersDeck[x])
        print("Dealers total : " ,dealersSum)



#Consider this as my main sequence : 

gameLoop()
drawCardPlayer()
drawCardDealer()
displayCards()
print("********************************")
hitOrStand()
   
    
    



# To run : python main.py





