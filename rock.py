from tkinter import *

t=Tk()
t.title("Rock Paper Scissor")
player_score=0
computer_score=0
lists=[("rock",0),("paper",1),("scissor",2)]
def computer_wins():
    global player_score, computer_score
    computer_score+=1
    l2.config(text="Computer Wins")
    c_score.config(text="Computer Score="+str (computer_score))
    p_score.config(text="Player Score="+str (player_score))

def player_wins():
    global player_score, computer_score
    player_score+= 1 
    l2.config(text="Player Wins")
    c_score.config(text="Computer Score="+str (computer_score))
    p_score.config(text="Player Score="+str (player_score))

def tie():
    global player_score, computer_score
    l2.config(text="Its A Tie")
    c_score.config(text="Computer Score"+str (computer_score))
    p_score.config(text="Player Score"+str (player_score))

l1=Label(t,
         text="Rock Paper Scissor",font=("New Times Roman",20))
l1.pack()

l2=Label(t,
         text="Ready? Start!",font=("New Times Roman",17),fg="dark blue")
l2.pack()
input_frame=Frame(t)
input_frame.pack()
p_score=Label(input_frame,
         text="your score=",font=("New Times Roman",20))
p_score.grid(row=1, column=0,padx=10)
p_selected=Label(input_frame,
         text="you selected=",font=("New Times Roman",20))
p_selected.grid(row=2, column=0,padx=10)
c_score=Label(input_frame,
         text="computer score=",font=("New Times Roman",20))
c_score.grid(row=1, column=2,pady=0)
c_selected=Label(input_frame,
         text="computer selected=",font=("New Times Roman",20))
c_selected.grid(row=2, column=2,pady=0)
options=Label(input_frame,
              text="your options",font=("New Times Roman",13))
options.grid(row=0,column=0,pady=8)
rock_btn=Button(input_frame,
                text="Rock",font=("New Times Roman",15),width=13,bg="red",bd=2)
rock_btn.grid(row=0,column=1,pady=8)

paper_btn=Button(input_frame,
                 text="Paper",font=("New Times Roman",15),width=13,bg="green",bd=2)
paper_btn.grid(row=0,column=2,pady=8)

scissor_btn=Button(input_frame,
                   text="Scissor",font=("New Times Roman",15),width=13,bg="blue",bd=2)
scissor_btn.grid(row=0,column=3,pady=8)

def player_choice(player_input):
    global player_score, computer_score
    print(player_input)
    computer_input=get_computer_choice()
    print(computer_input)

    p_selected.config(text="You selected="+player_input[0])
    c_selected.config(text="Computer Selected"+computer_input[0])

t.mainloop()

