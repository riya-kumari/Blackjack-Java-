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

values = ['2','3','4','5','6','7','8','9','10','Jack','Queen','King','Ace']
suites = ['Hearts', 'Clubs', 'Diamonds', 'Spades']
deck = [[v + ' of ' + s,v] for s in suites for v in values] 
bet = 0
sum = 0

    

    
class Card:
    # def__init__(self, number, suit):
    #     self.number = number
    #     self.suit = suit

    def __init__(self, number, suit, ):
        self.number = number
        self.suit = suit

    def getValue(self):
        if self.number>15 and self.number<23: return 10
        else: pass
        return self.number

    def getSuit(self):
        return self.suit

    def __str__(self):
        return str(self.number) + " of " + self.suit


class Game:
    def line(self):
        return  "----------------------------------------------"

    
# Consider this as my main

print("Blackjack Console Version 1.0")
myCard = Card(5,'Diamonds')


users_input = input("To start - enter in the amount you are betting. (Please do not enter without putting a value down)    ")
while users_input <5 :
    users_input = input("Minimum amount you can bet is 5.")

print("Your cards : ")
index = random.randint(1,52)
print(deck[index]) ; del deck[index]
sum = deck[index]

index = random.randint(1,51)
print(deck[index]) ; del deck[index]
sum = deck[index]
print(sum)





