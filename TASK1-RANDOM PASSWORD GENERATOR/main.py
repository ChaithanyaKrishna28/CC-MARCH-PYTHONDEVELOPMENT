''' RANDOM PASSWORD GENERATOR'''
from tkinter import *
import tkinter as tk
import string
import random

def generatePassword():
    try:
        password_entry.delete(0,tk.END)
        length = int(password_len.get())
        s1 = string.ascii_letters
        s2 = string.digits
        s3 = string.punctuation
        s = []
        s.extend(list(s1))
        s.extend(list(s2))
        s.extend(list(s3))
        password = ''.join(random.sample(s, length))
        password_entry.insert(0, password)
    except ValueError:
        password_entry.delete(0, tk.END)
        password_entry.insert(0, "Please Enter a Number")
def clipper():
    root.clipboard_clear()
    root.clipboard_append(password_entry.get())
root = tk.Tk()
Frame(root)
root.config(bg='black')
root.geometry("800x400")
root.title("RANDOM PASSWORD GENERATOR")
root.resizable(0,0)

lf = tk.Label(root, text="RANDOM PASSWORD GENERATOR",font=('algerian',30,'bold'),bg='yellow',fg='black')
lf.grid(column=0, row=0, pady=20,columnspan=2)

label_frame2 = tk.Label(root, text="Enter Password length", font=('algerian',20,'bold'),bg='black',fg='white')
label_frame2.grid(column=0, row=1,pady=20)

password_len = tk.Entry(root,bd=10,width=20,font=('algerian',20,'bold'),bg='powder blue',fg='black',justify='center')
password_len.grid(column=1, row=1)
password_len.bind("<<Modified>>", generatePassword)

label_frame3 = tk.Label(root,text="Generated Password",bd=5, font=('algerian',20,'bold'),bg='black',fg='white')
label_frame3.grid(column=0,row=2,pady=5)

password_entry = tk.Entry(root,text='',bd=10, font=('algerian',20,'bold'),bg='powder blue',fg='black',justify='center')
password_entry.grid(column=1,row=2)

generate_Button = tk.Button(root, text="Generate Password", command=generatePassword,bd=5,font=('arial',15,'bold'),bg='powder blue')
generate_Button.grid(column=0, row=3, pady=20)

copy_button = tk.Button(root,text="Copy to Clipboard",command=clipper,bd=5,font=('arial',15,'bold'),bg='powder blue')
copy_button.grid(column=1,row=3,pady=20)
root.mainloop()
