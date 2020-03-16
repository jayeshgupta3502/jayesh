from tkinter import*
root=Tk()
def callback():
 b=Button(root, Text="OK", Command=callback, bg="red", fg="Green")
 b.Pack()
