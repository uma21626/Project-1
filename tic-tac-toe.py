from tkinter import *
import tkinter.messagebox
tk= Tk()
tk.title("Tic-Tac-Toe")

pa = StringVar()
playerb = StringVar()
p1= StringVar()
p2= StringVar()
tk.configure(bg='#cb464e')

player1_name = Entry(tk, textvariable=p1,bd=5,bg='#fcfcec', width=40)
player1_name.grid(row=1, column=1, columnspan=8)
player2_name = Entry(tk, textvariable=p2, bd=5,bg='#fcfcec',width=40)
player2_name.grid(row=2, column=1, columnspan=8)

bclick = True
flag =0

def disableButton():
    button1.configure(state=DISABLED)
    button2.configure(state=DISABLED)
    button3.configure(state=DISABLED)
    button4.configure(state=DISABLED)
    button5.configure(state=DISABLED)
    button6.configure(state=DISABLED)
    button7.configure(state=DISABLED)
    button8.configure(state=DISABLED)
    button9.configure(state=DISABLED)

def btnClick(buttons):
    global bclick, flag, player2_name, player1_name, playerb, pa
    if buttons["text"]==" " and bclick == True:
        buttons["text"]= "X"
        bclick = False
        playerb = p2.get()+ "Wins!"
        pa= p1.get()+ "Wins!"
        checkForWin()
        flag+=1

    elif buttons["text"]== " " and bclick == False:
        buttons["text"]= "0"
        bclick = True
        checkForWin()
        flag+=1
    else:
        tkinter.messagebox.showinfo("Tic-Tac-Toe", "Button already Clicked!")

def checkForWin():
    if (button1['text']== 'X' and button2['text'] == 'X' and button3['text']== 'X' or
        button4['text']== 'X' and button5['text'] == 'X' and button6['text']== 'X' or
        button7['text']== 'X' and button8['text'] == 'X' and button9['text']== 'X' or
        button1['text']== 'X' and button5['text'] == 'X' and button9['text']== 'X' or
        button3['text']== 'X' and button5['text'] == 'X' and button7['text']== 'X' or
        button1['text']== 'X' and button2['text'] == 'X' and button3['text']== 'X' or
        button1['text']== 'X' and button4['text'] == 'X' and button7['text']== 'X' or
        button2['text']== 'X' and button5['text'] == 'X' and button8['text']== 'X' or
        button7['text']== 'X' and button6['text'] == 'X' and button9['text']== 'X' ):
        disableButton()
        tkinter.messagebox.showinfo("Tic-Tac-Toe",pa)
    elif(flag==8):
        tkinter.messagebox.showinfo("Tic-Tac-Toe", "It is a tie")
def checkForWin():
    if(button1['text']=='X' and button2['text']=='X' and button3['text']=='X'or
       button4['text']=='X' and button5['text']=='X' and button6['text']=='X'or
       button7['text']=='X' and button8['text']=='X' and button9['text']=='X'or
       button1['text']=='X' and button5['text']=='X' and button9['text']=='X'or
       button3['text']=='X' and button5['text']=='X' and button7['text']=='X'or
       button1['text']=='X' and button2['text']=='X' and button3['text']=='X'or
       button1['text']=='X' and button4['text']=='X' and button7['text']=='X'or
       button2['text']=='X' and button5['text']=='X' and button8['text']=='X'or
       button7['text']=='X' and button6['text']=='X' and button9['text']=='X'):
        disableButton()
        tkinter.messagebox.showinfo("Tic-Tac-Toe", pa)
    elif(flag==8):
        tkinter.messagebox.showinfo("Tic-Tac-Toe", "It is a tie")
    elif (button1['text']=='0' and button2['text']=='0' and button3['text'] == '0'or
          button4['text']=='0' and button5['text']=='0' and button6['text'] == '0'or
          button7['text']=='0' and button8['text']=='0' and button9['text'] == '0'or
          button1['text']=='0' and button5['text']=='0' and button9['text'] == '0'or
          button3['text']=='0' and button5['text']=='0' and button7['text'] == '0'or
          button1['text']=='0' and button2['text']=='0' and button3['text'] == '0'or
          button1['text']=='0' and button4['text']=='0' and button7['text'] == '0'or
          button2['text']=='0' and button5['text']=='0' and button8['text'] == '0'or
          button7['text']=='0' and button6['text']=='0' and button9['text'] == '0'):
        disableButton()
        tkinter.messagebox.showinfo("Tic-Tac-Toe", playerb)
buttons = StringVar()
label = Label(tk, text="Player 1:", font='Times 20 bold', bg='#cb464e', fg='#fcfcec', height=1, width=8)
label.grid(row=1, column=0)
label = Label(tk, text="Player 2:", font='Times 20 bold', bg='#cb464e', fg='#fcfcec', height=1, width=8)
label.grid(row=2, column=0)
button1 = Button(tk, text=" ", font= "Times 20 bold", bg='#4b7fa4', fg='#fcfcec', height=4, width=8, command=lambda:
btnClick(button1))
button1.grid(row=3, column=0)
button2 = Button(tk, text=" ", font= "Times 20 bold", bg='#4b7fa4', fg='#fcfcec', height=4, width=8, command=lambda:
btnClick(button2))
button1.grid(row=3, column=1)
button3 = Button(tk, text=" ", font= "Times 20 bold", bg='#4b7fa4', fg='#fcfcec', height=4, width=8, command=lambda:
btnClick(button3))
button1.grid(row=3, column=2)
button4 = Button(tk, text=" ", font= "Times 20 bold", bg='#4b7fa4', fg='#fcfcec', height=4, width=8, command=lambda:
btnClick(button4))
button1.grid(row=4, column=0)
label = Label(tk, text="Player 2:", font='Times 20 bold', bg='#cb464e', fg='#fcfcec', height=1, width=8)
label.grid(row=2, column=0)
button1 = Button(tk, text=" ", font= "Times 20 bold", bg='#4b7fa4', fg='#fcfcec', height=4, width=8, command=lambda:
btnClick(button1))
button1.grid(row=3, column=0)
button2 = Button(tk, text=" ", font= "Times 20 bold", bg='#4b7fa4', fg='#fcfcec', height=4, width=8, command=lambda:
btnClick(button2))
button1.grid(row=3, column=1)
button3 = Button(tk, text=" ", font= "Times 20 bold", bg='#4b7fa4', fg='#fcfcec', height=4, width=8, command=lambda:
btnClick(button3))
button1.grid(row=3, column=2)
button4 = Button(tk, text=" ", font= "Times 20 bold", bg='#4b7fa4', fg='#fcfcec', height=4, width=8, command=lambda:
btnClick(button4))
button1.grid(row=4, column=0)













