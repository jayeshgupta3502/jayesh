from tkinter import*
top=Tk()

def helloCallBack():
    l=Label(top,text="Hii")
    l.pack()

B=Button(top,text="hello",command= helloCallBack)
B.pack()
top.mainloop()
