# we have a tic-tac-toe game to play
# Two players play this game
# Board is 3X3 

# Lets import tkinter to create board GUI
from tkinter import *
import random


def check_box():

# Class for custom button
class cButton(Button):

    def __init__(self, master, canvas, hloc, vloc, cwidth=5, cheight=2, cbg='red',ctext='check', **kwargs):
        super().__init__(master, text=ctext, bg=cbg, **kwargs)
        self.button1_window = canvas.create_window(hloc, vloc, anchor=NW, window=self)
        self.config( height = cheight, width = cwidth )

if __name__ == '__main__':
    # Lets start by creating a board
    root = Tk()
    root.geometry('600x650')
    root.resizable(0,0)
    root.title('Tic-Tac-Toe Game')
    root.config(bg ='seashell3')


    canvas = Canvas(root,bg='grey', height=600, width=600)
    hline1 = canvas.create_line(200, 0, 200, 600, fill='black', width = 2) #, ..., xn, yn, options)
    hline2 = canvas.create_line(400, 0, 400, 600, fill='black', width = 2) #, ..., xn, yn, options)
    vline1 = canvas.create_line(0, 200, 600, 200, fill='black', width = 2) #, ..., xn, yn, options)
    vline2 = canvas.create_line(0, 400, 600, 400, fill='black', width = 2) #, ..., xn, yn, options)

    button1 = cButton(root,canvas,hloc=80,vloc=80, command=check_box)
    button2 = cButton(root,canvas,hloc=280,vloc=80)
    button3 = cButton(root,canvas,hloc=480,vloc=80)
    button4 = cButton(root,canvas,hloc=80,vloc=280)
    button5 = cButton(root,canvas,hloc=280,vloc=280)
    button6 = cButton(root,canvas,hloc=480,vloc=280)
    button7 = cButton(root,canvas,hloc=80,vloc=480)
    button8 = cButton(root,canvas,hloc=280,vloc=480)
    button9 = cButton(root,canvas,hloc=480,vloc=480)
    exit_button = cButton(root,canvas,ctext="Exit", command=root.destroy, hloc=650, vloc=600, cbg='grey')
    exit_button.pack(side=BOTTOM)


    canvas.pack()
    root.mainloop()