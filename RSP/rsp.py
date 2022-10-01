#!/usr/bin/python3

from tkinter import *
from PIL import Image,ImageTk
import random

# main window
root = Tk()
root.title("Rock Scissor Paper")
root.configure(background="#9b59b6")

#picture
rock_img = ImageTk.PhotoImage(Image.open("Rock.png"))
paper_img = ImageTk.PhotoImage(Image.open("Paper.png"))
scissor_img = ImageTk.PhotoImage(Image.open("Scissor.png"))

# the same for BOT
bot_rock_img = ImageTk.PhotoImage(Image.open("Bot-Rock.png"))
bot_paper_img = ImageTk.PhotoImage(Image.open("Bot-Paper.png"))
bot_scissor_img = ImageTk.PhotoImage(Image.open("Bot-Scissor.png"))

# insert picture
user_label = Label(root,image=scissor_img,bg="#9b59b6")
comp_label = Label(root,image=bot_scissor_img,bg="#9b59b6")

comp_label.grid(row=1,column=0)
user_label.grid(row=1,column=4)

# scores
playerScore = Label(root,text=0,font=100,bg="#9b59b6",fg="white")
computerScore = Label(root,text=0,font=100,bg="#9b59b6",fg="white")

computerScore.grid(row=1,column=1)
playerScore.grid(row=1,column=3)

#indicators
user_indicator = Label(root,font=50,text="USER",bg="#9b59b6",fg="white")
comp_indicator = Label(root,font=50,text="COMPUTER",bg="#9b59b6",fg="white")

user_indicator.grid(row=0,column=3)
comp_indicator.grid(row=0,column=1)

# messages
msg = Label(root,font=50,bg="#9b59b6",fg="white")
msg.grid(row=3,column=2)

# update Message
def updateMessage(x):
	msg['text'] = x

# update user score
def updateUserScore():
	score = int(playerScore["text"])
	score += 1
	playerScore["text"] = str(score)

#update computer score
def updateCompScore():
	score = int(computerScore["text"])
	score += 1
	computerScore["text"] = str(score)


# check winner
def CheckWin(player,computer):
	if player == computer:
		updateMessage("It's a tied!!!")
	elif player == "rock":
		if computer == "paper":
			updateMessage("You Loose!!!")
			updateCompScore()
		else:
			updateMessage("You Win")
			updateUserScore()

	elif player == "paper":
		if computer == "scissor":
			updateMessage("You Loose!!!")
			updateCompScore()
		else:
			updateMessage("You Win")
			updateUserScore()
	elif player == "scissor":
		if computer == "rock":
			updateMessage("You Loose!!!")
			updateCompScore()
		else:
			updateMessage("You Win")
			updateUserScore()
	else:
		pass

choices = ["rock","paper","scissor"]

# update choices
def updateChoice(x):
	# computer
	compChoice = choices[random.randint(0,2)]
	if compChoice == "rock":
		comp_label.configure(image=bot_rock_img)
	elif compChoice == "paper":
		comp_label.configure(image=bot_paper_img)
	else:
		comp_label.configure(image=bot_scissor_img)

	#user
	if x == "rock":
		user_label.configure(image=rock_img)
	elif x == "paper":
		user_label.configure(image=paper_img)
	else:
		user_label.configure(image=scissor_img)

	CheckWin(x,compChoice)



# buttons
rock = Button(root,width=20,height=2,text="ROCK",bg="#FF3E4D",fg="white",command= lambda:updateChoice("rock")).grid(row=2,column=1)
paper = Button(root,width=20,height=2,text="PAPER",bg="#FAD02E",fg="white",command=lambda:updateChoice("paper")).grid(row=2,column=2)
scissor = Button(root,width=20,height=2,text="SCISSOR",bg="#0ABDE3",fg="white",command=lambda:updateChoice("scissor")).grid(row=2,column=3)



root.mainloop()
