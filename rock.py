from tkinter import *

t=Tk()
t.title("Rock Paper Scissor")

l1=Label(t,
         text="Rock Paper Scissor",font=("New Times Roman",20))
l1.pack()

l2=Label(t,
         text="Ready? Start!",font=("New Times Roman",17),fg="dark blue")
l2.pack()
input_frame=Frame(t)
input_frame.pack()
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
t.mainloop()
