from tkinter import *
from random import choice
from PIL import ImageTk, Image

root = Tk()
root.resizable(width=False, height=False)
root.title('The Rock, Paper, Scissors')
cpu = ['Rock', 'Paper', 'Scissors']

rock1 = Image.open('R.jpg')
rock1 = rock1.resize((375, 250))
rock_pic = ImageTk.PhotoImage(rock1)

paper1 = Image.open('P.jpg')
paper1 = paper1.resize((375, 250))
paper_pic = ImageTk.PhotoImage(paper1)

scissors1 = Image.open('S.jpg')
scissors1 = scissors1.resize((375, 250))
scissors_pic = ImageTk.PhotoImage(scissors1)

win = Label(root, text='You Win')
lose = Label(root, text='You Lose')
draw = Label(root, text='Draw')

cpu_choiceR = Label(root, text='Cpu chose Rock')
cpu_choiceP = Label(root, text='Cpu chose Paper')
cpu_choiceS = Label(root, text='Cpu chose Scissors')
player_ChoiceR = Label(root, text='You chose Rock')
player_ChoiceP = Label(root, text='You chose Paper')
player_ChoiceS = Label(root, text='You chose Scissors')

def r():
    y = choice(cpu)
    if y == 'Rock':
        win.grid_forget()
        draw.grid_forget()
        lose.grid_forget()
        cpu_choiceS.grid_forget()
        cpu_choiceP.grid_forget()
        cpu_choiceS.grid_forget()
        player_ChoiceR.grid_forget()
        player_ChoiceP.grid_forget()
        player_ChoiceS.grid_forget()
        player_ChoiceR.grid(row=2, column=1)
        draw.grid(row=4, column=1)
        cpu_choiceR.grid(row=3, column=1)
        return
    elif y == 'Paper':
        win.grid_forget()
        draw.grid_forget()
        lose.grid_forget()
        cpu_choiceS.grid_forget()
        cpu_choiceP.grid_forget()
        cpu_choiceS.grid_forget()
        player_ChoiceR.grid_forget()
        player_ChoiceP.grid_forget()
        player_ChoiceS.grid_forget()
        player_ChoiceR.grid(row=2, column=1)
        lose.grid(row=4, column=1)
        cpu_choiceP.grid(row=3, column=1)
        return
    elif y == 'Scissors':
        win.grid_forget()
        draw.grid_forget()
        lose.grid_forget()
        cpu_choiceS.grid_forget()
        cpu_choiceP.grid_forget()
        cpu_choiceS.grid_forget()
        player_ChoiceR.grid_forget()
        player_ChoiceP.grid_forget()
        player_ChoiceS.grid_forget()
        player_ChoiceR.grid(row=2, column=1)
        win.grid(row=4, column=1)
        cpu_choiceS.grid(row=3, column=1)
        return

def p():
    y = choice(cpu)
    if y == 'Rock':
        win.grid_forget()
        draw.grid_forget()
        lose.grid_forget()
        cpu_choiceS.grid_forget()
        cpu_choiceP.grid_forget()
        cpu_choiceS.grid_forget()
        player_ChoiceR.grid_forget()
        player_ChoiceP.grid_forget()
        player_ChoiceS.grid_forget()
        player_ChoiceP.grid(row=2, column=1)
        win.grid(row=4, column=1)
        cpu_choiceR.grid(row=3, column=1)
        return
    elif y == 'Paper':
        win.grid_forget()
        draw.grid_forget()
        lose.grid_forget()
        cpu_choiceS.grid_forget()
        cpu_choiceP.grid_forget()
        cpu_choiceS.grid_forget()
        player_ChoiceP.grid_forget()
        player_ChoiceS.grid_forget()
        player_ChoiceP.grid(row=2, column=1)
        draw.grid(row=4, column=1)
        cpu_choiceP.grid(row=3, column=1)
        return
    elif y == 'Scissors':
        win.grid_forget()
        draw.grid_forget()
        lose.grid_forget()
        cpu_choiceS.grid_forget()
        cpu_choiceP.grid_forget()
        cpu_choiceS.grid_forget()
        player_ChoiceP.grid_forget()
        player_ChoiceS.grid_forget()
        player_ChoiceP.grid(row=2, column=1)
        lose.grid(row=4, column=1)
        cpu_choiceS.grid(row=3, column=1)
        return

def s():
    y = choice(cpu)
    if y == 'Rock':
        win.grid_forget()
        draw.grid_forget()
        lose.grid_forget()
        cpu_choiceS.grid_forget()
        cpu_choiceP.grid_forget()
        cpu_choiceS.grid_forget()
        player_ChoiceP.grid_forget()
        player_ChoiceS.grid_forget()
        player_ChoiceS.grid(row=2, column=1)
        lose.grid(row=4, column=1)
        cpu_choiceR.grid(row=3, column=1)
        return
    elif y == 'Paper':
        win.grid_forget()
        draw.grid_forget()
        lose.grid_forget()
        cpu_choiceS.grid_forget()
        cpu_choiceP.grid_forget()
        cpu_choiceS.grid_forget()
        player_ChoiceP.grid_forget()
        player_ChoiceS.grid_forget()
        player_ChoiceS.grid(row=2, column=1)
        win.grid(row=4, column=1)
        cpu_choiceP.grid(row=3, column=1)
        return
    elif y == 'Scissors':
        win.grid_forget()
        draw.grid_forget()
        lose.grid_forget()
        cpu_choiceS.grid_forget()
        cpu_choiceP.grid_forget()
        cpu_choiceS.grid_forget()
        player_ChoiceP.grid_forget()
        player_ChoiceS.grid_forget()
        player_ChoiceS.grid(row=2, column=1)
        draw.grid(row=4, column=1)
        cpu_choiceS.grid(row=3, column=1)
        return

rock_Button = Button(root, image=rock_pic, command=r)
paper_Button = Button(root, image=paper_pic, command=p)
scissor_Button = Button(root, image=scissors_pic, command=s)
welcome_Label = Label(root, text='Click On Your Move')

welcome_Label.grid(row=0, column=1)
rock_Button.grid(row=1, column=0)
paper_Button.grid(row=1, column=1)
scissor_Button.grid(row=1, column=2)

root.mainloop()