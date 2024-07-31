from tkinter import *
from PIL import ImageTk, Image
import random

def computer_move():
    rng = random.randint(1, 3)
    if rng == 1:
        cm = "rock"
    elif rng == 2:
        cm = "paper"
    else:
        cm = "scissors"    
    return cm

def game(move):
    cm = computer_move()
    pm = move
    if cm == pm:
        if cm == "rock":
            computer_message.config(text="\nComputer chose rock")
            match_result.config(text="It's a tie!")
        elif cm == "paper":
            computer_message.config(text="\nComputer chose paper")
            match_result.config(text="It's a tie!")
        else:
            computer_message.config(text="\nComputer chose scissors")
            match_result.config(text="It's a tie")
    elif cm == "rock" and pm == "paper":
        computer_message.config(text="\nComputer chose rock")
        match_result.config(text="You win!")
    elif cm == "rock" and pm == "scissors":
        computer_message.config(text="\nComputer chose rock")
        match_result.config(text="You lose")
    elif cm == "paper" and pm == "rock":
        computer_message.config(text="\nComputer chose paper")
        match_result.config(text="You lose")
    elif cm  == "paper" and pm == "scissors":
        computer_message.config(text="\nComputer chose paper")
        match_result.config(text="You win!")
    elif cm == "scissors" and pm == "rock":
        computer_message.config(text="\nComputer chose scissors")
        match_result.config(text="You win!")
    else:
        computer_message.config(text="\nComputer chose scissors")
        match_result.config(text="You lose")
    
root = Tk()
root.title("Rock, Paper, Scissors")
root.configure(background="#31393C")

title = Label(root,text="Rock, Paper, Scissors Game", font=("Sans Serif", 18), fg="white", bg="#31393C")
title.grid(row=0, column=1)

img = Image.open("rockpaperscissors.jpg")
img = img.resize((150, 150), Image.Resampling.NEAREST)
img = ImageTk.PhotoImage(img)
panel = Label(root, image = img, bg="#31393C")
panel.grid(row=1, column = 1)

prompt = Label(root, text="\nEnter your move by selecting the corresponding button\n", font=("Sans Serif", 12), fg="white", bg="#31393C")
prompt.grid(row=2, column=1)

playrc = Button(root, text="Rock", command = lambda: game("rock"), font=("Sans Serif", 10), bg="#CCC7BF")
playrc.grid(row=3, column=0)

playpr = Button(root, text="Paper", command = lambda: game("paper"), font=("Sans Serif", 10), bg="#CCC7BF")
playpr.grid(row=3, column=1)

playsc = Button(root, text="Scissors", command = lambda: game("scissors"), font=("Sans Serif", 10), bg="#CCC7BF")
playsc.grid(row=3, column=2)

computer_message = Label(root, font=("Sans Serif", 12), fg="white", bg="#31393C")
computer_message.grid(row=4, column=1)

match_result = Label(root, font=("Sans Serif", 12), fg="white", bg="#31393C")
match_result.grid(row=5, column=1)

root.mainloop()

