from tkinter import *


root = Tk()
root.geometry("500x300")
root.title("Tic-Tac-Toe")
Label(root, text="TIC-TAC-TOE", font="arial 20 bold").pack()

# Variable that show what turns is for the game
turn = 1

# One of the button to put the X or O
def onebtnclick():
    if(onebtn['text']=='   ' and(turn == 1)):
        onebtn['text']='X'
    elif(onebtn['text']=='   ' and(turn== 2)):
        onebtn['text']='O'

# One of the button to put the X or O
def twobtnclick():
    if(twobtn['text']=='   ' and(turn == 1)):
        twobtn['text']='X'
    elif(twobtn['text']=='   ' and (turn== 2)):
        twobtn['text']='O'

# One of the button to put the X or O
def threebtnclick():
    if(threebtn['text']=='   ' and(turn == 1)):
        threebtn['text']='X'
    elif(threebtn['text']=='   ' and (turn== 2)):
        threebtn['text']='O'

# One of the button to put the X or O
def fourbtnclick():
    if(fourbtn['text']=='   ' and(turn == 1)):
        fourbtn['text']='X'
    elif(fourbtn['text']=='   ' and (turn== 2)):
        fourbtn['text']='O'

# One of the button to put the X or O
def fivebtnclick():
    if(fivebtn['text']=='   ' and(turn == 1)):
        fivebtn['text']='X'
    elif(fivebtn['text']=='   ' and (turn == 2)):
        fivebtn['text']='O'

# One of the button to put the X or O
def sixbtnclick():
    if(sixbtn['text']=='   ' and(turn == 1)):
        sixbtn['text']='X'
    elif(sixbtn['text']=='   ' and (turn == 2)):
        sixbtn['text']='O'

# One of the button to put the X or O
def septbtnclick():
    if(septbtn['text']=='   ' and(turn == 1)):
        septbtn['text']='X'
    elif(septbtn['text']=='   ' and (turn == 2)):
        septbtn['text']='O'

# One of the button to put the X or O
def eightbtnclick():
    if(eightbtn['text']=='   ' and(turn == 1)):
        eightbtn['text']='X'
    elif(eightbtn['text']=='   ' and (turn == 2)):
        eightbtn['text']='O'


# One of the button to put the X or O
def ninebtnclick():
    if(ninebtn['text']=='   ' and(turn == 1)):
        ninebtn['text']='X'
    elif(ninebtn['text']=='   ' and (turn == 2)):
        ninebtn['text']='O'

# This function add or remove one number to the turn
def nextturnclick():
    global turn
    if(turn ==1):
        TurnText['text'] = 'Is the turn of the 0'
        turn = turn + 1

    else:
        TurnText['text'] = 'Is the turn of the X'
        turn = turn - 1

# This function detect if the differents buttons have and X or O to demonitate a victory
def windetec():
    if(onebtn['text']=='X' and twobtn['text']=='X') and (threebtn['text']=='X'):
        TurnText['text'] = 'The Winner is X!!!!!'
    elif(onebtn['text']=='O' and twobtn['text']=='O') and(threebtn['text']=='O'):
        TurnText['text'] = 'The Winner is O!!!!'
    elif(fourbtn['text']=='X' and fivebtn['text']=='X') and(sixbtn['text']=='X'):
        TurnText['text'] = 'The Winner is X!!!!!'
    elif(fourbtn['text']=='O' and fivebtn['text']=='O') and(sixbtn['text']=='O'):
        TurnText['text'] = 'The Winner is O!!!!!'
    elif(septbtn['text']=='O' and eightbtn['text']=='O') and(ninebtn['text']=='O'):
        TurnText['text'] = 'The Winner is O!!!!!'
    elif(septbtn['text']=='X' and eightbtn['text']=='X') and(ninebtn['text']=='X'):
        TurnText['text'] = 'The Winner is X!!!!!'
    elif(threebtn['text']=='O' and fivebtn['text']=='O') and(septbtn['text']=='O'):
        TurnText['text'] = 'The Winner is O!!!!!'
    elif(threebtn['text']=='X' and fivebtn['text']=='X') and(septbtn['text']=='X'):
        TurnText['text'] = 'The Winner is X!!!!!'
    elif(onebtn['text']=='O' and fivebtn['text']=='O') and(ninebtn['text']=='O'):
        TurnText['text'] = 'The Winner is O!!!!!'
    elif(onebtn['text']=='X' and fivebtn['text']=='X') and(ninebtn['text']=='X'):
        TurnText['text'] = 'The Winner is X!!!!!'
    elif(ninebtn['text']=='O' and sixbtn['text']=='O') and (threebtn['text']=='O'):
        TurnText['text'] = 'The Winner is O!!!!!'
    elif(ninebtn['text']=='X' and sixbtn['text']=='X') and (threebtn['text']=='X'):
        TurnText['text'] = 'The Winner is X!!!!!'
    elif(eightbtn['text']=='O' and fivebtn['text']=='O') and (twobtn['text']=='O'):
        TurnText['text'] = 'The Winner is O'
    elif(eightbtn['text']=='X' and fivebtn['text']=='X') and (twobtn['text']=='X'):
        TurnText['text'] = 'The Winner is X'
    elif(septbtn['text']=='O' and fourbtn['text']=='O') and (onebtn['text']=='O'):
        TurnText['text'] = 'The Winner is O'
    elif(septbtn['text']=='X' and fourbtn['text']=='X') and (onebtn['text']=='X'):
        TurnText['text'] = 'The Winner is X'

# Resets all the variables and text to their first state
def ResetClick():
    global turn
    onebtn['text']='   '
    twobtn['text']='   '
    threebtn['text']='   '
    fourbtn['text']='   '
    fivebtn['text']='   '
    sixbtn['text']='   '
    septbtn['text']='   '
    eightbtn['text']='   '
    ninebtn['text']='   '
    TurnText['text']='Is the turn of the X'
    turn = 1

# Definitions of the UI
TurnText = Label(root, text="Is the turn of the X", font="airal 15")
onebtn = Button(root, text="   ", command= onebtnclick)
twobtn = Button(root, text='   ', command= twobtnclick)
threebtn = Button(root, text='   ', command = threebtnclick)
fourbtn = Button(root, text='   ', command=fourbtnclick)
fivebtn = Button(root, text='   ', command= fivebtnclick)
sixbtn = Button(root, text='   ', command= sixbtnclick)
septbtn = Button(root, text='   ', command= septbtnclick)
eightbtn = Button(root, text='   ', command= eightbtnclick)
ninebtn = Button(root, text='   ', command= ninebtnclick)
nextturn = Button(root, text='Next Turn', command= nextturnclick)
checkwin = Button(root, text='Check Win', command=windetec)
resetbtn = Button(root, text='Reset', command=ResetClick)

# Where is the position of all the buttons
ninebtn.place(x=200, y=100)
eightbtn.place(x=225, y=100)
septbtn.place(x=250, y=100)
sixbtn.place(x=200, y=125)
fivebtn.place(x=225, y=125)
fourbtn.place(x=250, y=125)
threebtn.place(x=200, y=150)
twobtn.place(x=225, y=150)
onebtn.place(x=250, y=150)
nextturn.place(x=400, y=200)
checkwin.place(x=400, y=250)
resetbtn.place(x=200, y=250)
TurnText.pack()


root.mainloop()