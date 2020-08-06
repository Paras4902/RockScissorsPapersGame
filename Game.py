"""A Program to Play rock, scissors, paper game with computer using random module """
from tkinter import Tk, Button, Label, Entry, END, StringVar, BOTTOM, RAISED, SE
from PIL import Image, ImageTk
import random

root = Tk()
root.geometry("1100x600")
root.title("Game")
root.resizable(0, 0)

# Functions


def rock():
    """Function to insert rock in the user's entry"""
    e1.delete(0, END)
    e1.insert(END, "rock")


def scissor():
    """Function to insert scissor in the user's entry"""
    e1.delete(0, END)
    e1.insert(END, "scissor")


def paper():
    """Function to insert paper in the user's entry"""
    e1.delete(0, END)
    e1.insert(END, "paper")


def playgame():
    txt.set("Computer's turn............")
    import time
    from tkinter import messagebox as msgbx
    root.update()
    time.sleep(1)
    txt.set("Play")
    user = e1.get()
    k = random.randint(1, 3)
    if k == 1:
        cmp = "rock"
    elif k == 2:
        cmp = "scissor"
    else:
        cmp = "paper"
    e2.delete(0, END)
    e2.insert(END, cmp)
    if e1.get() == "":
        msgbx.showwarning("Choose an option", "Please choose a option to continue")
        e2.delete(0, END)
    else:
        if e2.get() == "rock" and user == "scissor" or e2.get() == "scissor" and user == "paper" or e2.get() == "paper" and user == "rock":
            msgbx.showinfo("Result", "Computer Wins and you Lose!!")
        elif user == "paper" and e2.get() == "rock" or user == "scissor" and e2.get() == "paper" or user == "rock" and e2.get() == "scissor":
            msgbx.showinfo("Result", "You Win and Computer Lose!!")
        else:
            msgbx.showinfo("Result", "match tied")
    e1.delete(0, END)
    e2.delete(0, END)


# Labels
Label(root, text="Welcome to Rock Papers Scissors Game", font=("Times", 35, "bold underline")).pack()
Label(root, text="Your Choice", font=("Times", 30, "bold"), bd=10).place(x=450, y=70)
Label(root, text="Program@Paras4902", font=("Helvetica", 25, "italic"), fg="#EE82EE").pack(side=BOTTOM, anchor=SE)
Label(root, text="Computer's Choice", font=("Times", 30, "bold"), bd=10).place(x=380, y=330)
txt = StringVar()
txt.set("Play")
Label(root, textvariable=txt).place(x=10, y=570)

# Buttons
img = ImageTk.PhotoImage(Image.open("game.png"))
b1 = Button(root, text="Rock", font=("Helvetica", 25), relief=RAISED, bd=10, bg="blue", command=rock)
b1.place(x=270, y=150, width=200)
b2 = Button(root, text="Scissor", font=("Helvetica", 25), relief=RAISED, bd=10, bg="red", command=scissor)
b2.place(x=470, y=150, width=200)
b3 = Button(root, text="Paper", font=("Helvetica", 25), relief=RAISED, bd=10, bg="#7fff00", command=paper)
b3.place(x=670, y=150, width=200)
b1 = Button(root, image=img, bg="grey", fg="green", bd=10, command=playgame)
b1.place(x=750, y=260, width=220, height=220)

# Entries
e1 = Entry(root, font=("Helvetica", 25), bd=10)
e1.place(x=420, y=250, width=300)
e2 = Entry(root, font=("Helvetica", 25), bd=10)
e2.place(x=420, y=420, width=300)

root.mainloop()
