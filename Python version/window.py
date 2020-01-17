from tkinter import*
import PIL
from PIL import ImageTk
from PIL import Image
# import bet

'''
python3 window.py
To quit is control-c
'''
# Variables used are decleared here
playersBet = 0

# 1- Create a window with title and background image
root = Tk()
root.title("BlackJack 1.0 : Click anywhere to start the game")
root.configure(bg = "green")

# Blackjack background image
im = Image.open("download.jpg")
resized_im = im.resize((400, 350))
ph = ImageTk.PhotoImage(resized_im)

def close_window(): 
    root.destroy()

startButton = Button(root, text = "Click anywhere to start game",image = ph, command = close_window)
startButton.pack()

root.mainloop()


# -----------------------------------------------------------------------------------------------------------------------
# Creating a bet window
betWindow = Tk()
betWindow.title("Bet Window")

# Creates the first frame with text
topFrame = LabelFrame(betWindow, padx = 10, pady = 10)
topLabel = Label(topFrame, text= "Place your bet here.", font = "Times 20 bold")
topLabel.pack()
topFrame.pack(padx=50, pady = (20,0))

# Creates middle frame with casino chips
midFrame = LabelFrame(betWindow, padx = 10, pady = 10)

# Creates bottom frame with total amount and a button
bottomFrame = LabelFrame(betWindow, padx = 10, pady = 10, bg ="green")
bottomSum = Label(bottomFrame, text = "Amount : " + str(playersBet) )
bottomSum.pack()

# Updates total amount
def updateAmt():
    global playersBet
    bottomSum.config(text =  "Amount : " + str(playersBet))
    bottomSum.pack()
    
# Method called when one of the casino chips are clicked
def buttonClicked(color):
    global playersBet
    if color == "red": playersBet += 20
    elif color == "purple" : playersBet +=500
    elif color == "green" : playersBet += 25
    elif color =="white" : playersBet += 1    
    else  : playersBet += 100
    updateAmt()


# White chip : $1
white_chip = Image.open("Casino Chips/one.png")
resized_im = white_chip.resize((50,50))
white = ImageTk.PhotoImage(resized_im)
one = Button(midFrame, text = "white", image=white, command = lambda:buttonClicked("white"))

# Red chip : $5
red_chip = Image.open("Casino Chips/five.png")
resized_im = red_chip.resize((50,50))
red = ImageTk.PhotoImage(resized_im)
five = Button(midFrame, text = "red", image = red, command = lambda:buttonClicked("red"))

# Green chip : $25
green_chip = Image.open("Casino Chips/twenty-five.jpg")
resized_im = green_chip.resize((50,50))
green = ImageTk.PhotoImage(resized_im)
twenty_five = Button(midFrame, text = "green", image=green, command = lambda:buttonClicked("green"))

# Black chip : $100
black_chip = Image.open("Casino Chips/hundred.jpg")
resized_im = black_chip.resize((50,50))
black = ImageTk.PhotoImage(resized_im)
hundred = Button(midFrame, text = "black", image=black, command = lambda:buttonClicked("black"))

# Purple chip : $500
purple_chip = Image.open("Casino Chips/five-hundred.png")
resized_im = purple_chip.resize((50,50))
purple = ImageTk.PhotoImage(resized_im)
five_hundred = Button(midFrame, text = "purple", image=purple, command = lambda:buttonClicked("purple"))

# Done Button
doneButton = Button(bottomFrame, text = "I've made my bet.", command = betWindow.destroy)


# Displaying all the casino chips and all the frames
midFrame.pack()
bottomFrame.pack()
one.grid(row=0, column=0)
five.grid( row = 0, column=1)
twenty_five.grid( row=0, column=2)
hundred.grid(row=0, column=3)
five_hundred.grid( row=0, column=4)
doneButton.pack(pady = 10)

betWindow.mainloop()

# -----------------------------------------------------------------------------------------------------------------------
gameWindow =  Tk()
botWindow = Tk()

# Titles for the windows
gameWindow.title("Blackjack 1.0")
botWindow.title("Helper Bot")

playingSpace = LabelFrame(bg = "green")
playingSpace.grid(row-range: 4, column = 0)

bottomSpace = playingSpace = LabelFrame(bg = "grey")
playingSpace.grid(row: 1, column = 0)

# Sets the size and color of the windows
gameWindow.geometry("800x600")
# gameWindow.config(bg = "green")
botWindow.geometry("200x300")


c = Canvas(gameWindow, height=500, width=1000)


gameWindow.mainloop()
botWindow.mainloop()