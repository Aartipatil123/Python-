

from tkinter import *
import tkinter as tk


from PIL import Image ,ImageTk

from tkinter.ttk import *
from pymsgbox import *


root=tk.Tk()

root.title("Dyslexic disease detection")
w,h = root.winfo_screenwidth(),root.winfo_screenheight()

bg = Image.open(r"bg2.jpg")
bg.resize((1866,600),Image.LANCZOS)
print(w,h)
bg_img = ImageTk.PhotoImage(bg)
bg_lbl = tk.Label(root,image=bg_img)
bg_lbl.place(x=0,y=93)
#, relwidth=1, relheight=1)

w = tk.Label(root, text="Dyslexic disease detection ",width=40,background="black",foreground="white",height=2,font=("Times new roman",19,"bold"))
w.place(x=0,y=15)



w,h = root.winfo_screenwidth(),root.winfo_screenheight()
root.geometry("%dx%d+0+0"%(w,h))
root.configure(background="black")


from tkinter import messagebox as ms


def Login():
    from subprocess import call
    call(["python","login.py"])
def Register():
    from subprocess import call
    call(["python","registration.py"])


wlcm=tk.Label(root,text="......Dyslexic disease detection ......",width=95,height=3,background="black",foreground="white",font=("Times new roman",22,"bold"))
wlcm.place(x=0,y=620)




d2=tk.Button(root,text="Login",command=Login,width=9,height=2,bd=0,background="#800000",foreground="white",font=("times new roman",14,"bold"))
d2.place(x=1000,y=18)


d3=tk.Button(root,text="Register",command=Register,width=9,height=2,bd=0,background="#800000",foreground="white",font=("times new roman",14,"bold"))
d3.place(x=1100,y=18)



root.mainloop()
