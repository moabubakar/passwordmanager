import time
from tkinter import *
import tkinter as tk
from tkinter import ttk
from tkinter import messagebox
from tkinter import PhotoImage
import webbrowser
import sqlite3
import requests

root = tk.Tk()
root.title('H A L O')
windowWidth = 700
windowHeight = 330
screenWidth = root.winfo_screenwidth()
screenHeight = root.winfo_screenheight()
xCordinate = int((screenWidth/2) - (windowWidth/2))
yCordinate = int((screenHeight/2) - (windowHeight/2))
root.geometry("{}x{}+{}+{}".format(windowWidth, windowHeight, xCordinate, yCordinate))
style = ttk.Style(root)
root.tk.call('source', 'azure-dark.tcl')
root.resizable(False,False)
style.theme_use('azure-dark')

photo = PhotoImage(file="HaloLogo.gif")
panel = Label(root, image=photo)
panel.place(x=490, y=0)

checkframe = ttk.LabelFrame(root, text='Register', width=460, height=300)
checkframe.place(x=20, y=12)

def misc():
    def callback(url):
        webbrowser.open_new(url)

    def myClick():
        contactButton = Button(root, text='Twitter Contact', command=callback("https://twitter.com/awarevfx"))

    def abt():
        message2 = messagebox.showinfo("Contact", text='Twitter Contact', command=myClick())
        message2.pack()

    menu = Menu(root)
    root.config(menu=menu)
    subm1 = Menu(menu)
    menu.add_cascade(label="File", menu=subm1)
    subm1.add_command(label="Exit", command=exit)
    subm2 = Menu(menu)
    menu.add_cascade(label="Option", menu=subm2)
    subm2.add_command(label="Contact", command=abt)
    photo = PhotoImage(file="HaloLogo.gif", format="gif -index 2")
    panel = Label(root, image=photo)
    panel.place(x=490, y=0)
    checkframe = ttk.LabelFrame(root, text='Register', width=460, height=300)
    checkframe.place(x=20, y=12)

def auth():
    exit()

def register():
    with sqlite3.connect(
            'HaloSystem.db') as db:
        cursor = db.cursor()

    cursor.execute("""
        CREATE TABLE IF NOT EXISTS users(
            id Integer PRIMARY KEY,
            username text,
            password text
        )
        """)
    cursor.execute("SELECT 1 FROM users WHERE username = ?", (user_input.get(),))
    if len(cursor.fetchall()) > 0:
        messagebox.showinfo("Register", "Username already exists.")
        register2()
    else:
        if len(user_input.get()) < 4:
            return messagebox.showinfo("Register", 'Username must be greater than 3 characters.')
        else:
            if user_input.get() == "" or pass_input.get() == "":
                return messagebox.showinfo("Register", 'Invalid Fields')
            else:
                while pass_input.get() != pass_input2.get():
                    return messagebox.showinfo("Register", 'Passwords don\'t match.')
                while len(pass_input.get()) < 7:
                    return messagebox.showinfo("Register", 'Password must be at least 7 characters.')
                else:
                    cursor.execute("""INSERT INTO users(username, password)
                    VALUES(?,?)""", (user_input.get(), pass_input.get()))
                    db.commit()
                    messagebox.showinfo("Register", "Successfully registered!.")
                    root.destroy()
                    import Halo

user_input=tk.StringVar()
pass_input=tk.StringVar()
pass_input2=tk.StringVar()
emailinput=tk.StringVar()

def register2():
    global user_input, pass_input, pass_input2, emailinput
    info_user = ttk.Label(root, text="Username : ").place(x=120, y=110)
    userinput = tk.Entry(root, textvariable=user_input, font=('calibre', 10, 'normal'))
    userinput.place(x=190, y=110)
    info_pass = ttk.Label(root, text="Password : ").place(x=122, y=140)
    passinput = tk.Entry(root, textvariable=pass_input, font=('calibre', 10, 'normal'), show='*')
    passinput.place(x=190, y=140)
    info_pass2 = ttk.Label(root, text="Confirm Password : ").place(x=75, y=172)
    passinput2 = tk.Entry(root, textvariable=pass_input2, font=('calibre', 10, 'normal'), show='*')
    passinput2.place(x=190, y=170)
    accentbutton = ttk.Button(root, text='Register', style='AccentButton', command=register)
    accentbutton.place(x=150, y=205)
    def returnF():
        root.destroy()
        import Halo
    accentbutton2 = ttk.Button(root, text='Return', style='AccentButton', command=returnF)
    accentbutton2.place(x=260, y=205)

misc()
register2()

root.mainloop()