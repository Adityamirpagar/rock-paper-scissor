from tkinter import *
from typing import final
from PIL import Image, ImageTk
from random import randint

## Console with title
window = Tk()
window.title("Rock Paper scissor by Aditya Mirpagar")
window.configure(background = "#bf3671")


## images

## for computer
image_rock1 = ImageTk.PhotoImage(Image.open("images/rock_1.png"))
image_paper1 = ImageTk.PhotoImage(Image.open("images/paper_1.png"))
image_scissors1 = ImageTk.PhotoImage(Image.open("images/scissors_1.png"))

## for player
image_rock2 = ImageTk.PhotoImage(Image.open("images/rock_2.png"))
image_paper2 = ImageTk.PhotoImage(Image.open("images/paper_2.png"))
image_scissors2 = ImageTk.PhotoImage(Image.open("images/scissors_2.png"))

## default
image_z = ImageTk.PhotoImage(Image.open("images/z.png"))

## inserting default images
label_player = Label(window, image = image_z,)
label_computer = Label(window, image = image_z)
label_computer.grid(row = 1, column= 0)
label_player.grid(row = 1, column= 5)

label_player.configure(image = image_z, bg= "#bf3671")
label_computer.configure(image = image_z, bg= "#bf3671")

## scores
computer_score = Label(window, text= 0, font= ("arial", 60, "bold"), bg= "#bf3671", fg= "red")
player_score = Label(window, text= 0, font= ("arial", 60, "bold"),bg= "#bf3671", fg= "red")

computer_score.grid(row= 2, column= 0)
player_score.grid(row= 2, column= 5)


## indicator
player_inidiactor= Label(window, font=("arail",30,"bold"), text= "PLAYER", bg = "#bf3671", fg="red")
computer_indicator= Label(window, font=("arial",30,"bold"), text="COMPUTER", bg= "#bf3671", fg= "red")
player_inidiactor.grid(row= 0, column= 5)
computer_indicator.grid(row=0, column= 0)


## Messages
final_message= Label(window, font=("arial",30,"bold"),bg="#bf3671", fg= "red")
final_message.grid(row=3 , column= 3)


## Update messages
def updateMessage(X):
    final_message["text"] = X


## update user score
def player_update():
    final = int(player_score["text"])
    final += 1
    player_score["text"]= str(final)

## update computer score
def computer_update():
    final = int(computer_score["text"])
    final += 1
    computer_score["text"]= str(final)


## Winner check 
def winner_check(p,c):
    if p == c:
        updateMessage("Its a tie ")
    elif p == "rock":
        if c == "paper":
            updateMessage("Lou Loose")
            computer_update()
        else:
            updateMessage("You Win")
            player_update()
    elif p == "paper":
        if c == "scissor":
            updateMessage("You Loose")
            computer_update()
        else:
            updateMessage("you Win")
            player_update()
    elif p == "scissor":
        if c == "rock":
            updateMessage("You Loose")
            computer_update()
        else:
            updateMessage("You win")
            player_update()
    else:
        pass


## Update Choices
choices = ["rock", "paper", "scissor"]

def update_choice(x):

## computer choice
    computer_choice = choices[randint(0,2)]
    if computer_choice == "rock":
        label_computer.configure(image = image_rock1)
    elif computer_choice == "paper":
        label_computer.configure(image = image_paper1)
    else:
        label_computer.configure(image = image_scissors1)

## for palyer
    if x == "rock":
        label_player.configure(image= image_rock2, bg= "#bf3671")
    elif x == "paper":
        label_player.configure(image= image_paper2, bg= "#bf3671")
    else:
        label_player.configure(image= image_scissors2, bg= "#bf3671")


    winner_check (x, computer_choice)


## Buttons
button_rock = Button(window, width=16, height=3, text="ROCK",
                     font=("arial",20,"bold"), bg = "yellow", fg = "red", command=lambda:update_choice("rock")).grid(row = 2, column = 2)
button_paper = Button(window, width=16, height=3, text= "PAPER", 
                      font=("arial",20,"bold"), bg = "yellow", fg = "red", command=lambda:update_choice("paper")).grid(row= 2, column= 3)
button_scissor = Button(window, width=16, height=3, text= "SCISSORS", 
                      font=("arial",20,"bold"), bg = "yellow", fg = "red", command=lambda:update_choice("scissor")).grid(row= 2, column= 4)


window.mainloop()