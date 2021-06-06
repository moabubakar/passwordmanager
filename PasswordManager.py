from tkinter import *
from tkinter import ttk
from tkinter import messagebox
from db import Database
import sqlite3

# Root
db=Database("HaloSystem.db")
root=Tk()
root.title("Halo Password Managing System")
root.resizable(False,False)
windowWidth = 1000
windowHeight = 200
screenWidth = root.winfo_screenwidth()
screenHeight = root.winfo_screenheight()
xCordinate = int((screenWidth/2) - (windowWidth/2))
yCordinate = int((screenHeight/2) - (windowHeight/2))
root.geometry("{}x{}+{}+{}".format(windowWidth, windowHeight, xCordinate, yCordinate))
style = ttk.Style(root)
root.tk.call('source', 'azure-dark.tcl')
style.theme_use('azure-dark')

# Variables
application=StringVar()
username=StringVar()
password=StringVar()

# Entry Frame's

lblApplication=Label(root,text="Application : ", font=('Helvetica', 10, 'bold'))
lblApplication.grid(row=1,column=0,padx=1,pady=10)
txtApplication=Entry(root,textvariable=application,font=('Helvetica', 10, 'bold'),width=30)
txtApplication.grid(row=1,column=3,padx=1,pady=10)

lblUsername=Label(root,text="Username : ", font=('Helvetica', 10, 'bold'))
lblUsername.grid(row=2,column=0,padx=1,pady=10)
txtUsername=Entry(root,textvariable=username,font=('Helvetica', 10, 'bold'),width=30)
txtUsername.grid(row=2,column=3,padx=1,pady=10)

lblPassword=Label(root,text="Password : ", font=('Helvetica', 10, 'bold'))
lblPassword.grid(row=3,column=0,padx=1,pady=10)
txtPassword=Entry(root,textvariable=password,font=('Helvetica', 10, 'bold'),width=30)
txtPassword.grid(row=3,column=3,padx=1,pady=10)

# Fucntion

def retrieveData(event):
    selected_row = tv.focus()
    data = tv.item(selected_row)
    global row
    row = data['values']
    application.set(row[1])
    username.set(row[2])
    password.set(row[3])


def displayAll():
    tv.delete(*tv.get_children())
    for row in db.fetch():
        tv.insert("",END,values=row)
def add_account():
    if txtApplication.get()=="" or txtUsername.get()=="" or txtPassword.get()=="":
        messagebox.showerror("Error", "Invalid Fields")
        return
    db.insert(txtApplication.get(), txtUsername.get(), txtPassword.get())
    messagebox.showinfo("Success", "Account saved in database.")
    clear()
    displayAll()

def update():
    if txtApplication.get() == "" or txtUsername.get() == "" or txtPassword.get() == "":
        messagebox.showerror("Error", "Invalid Fields")
        return
    db.update(row[0],txtApplication.get(),txtUsername.get(),txtPassword.get())
    clear()
    displayAll()

def del_account():
    if txtApplication.get() == "" or txtUsername.get() == "" or txtPassword.get() == "":
        messagebox.showerror("Error", "Invalid Fields")
        return
    db.remove(row[0])
    clear()
    displayAll()
def sign_out():
    exit()
def security():
    pass
def clear():
    application.set("")
    username.set("")
    password.set("")

# Buttons

btnAdd=Button(root, text='Add', command=add_account,width=10)
btnAdd.grid(row=1,column=4,padx=5)
btnRemove=Button(root, text='Remove', command=del_account,width=10)
btnRemove.grid(row=2,column=4,padx=5)
btnSignOut=Button(root, text='Exit', command=sign_out,width=10)
btnSignOut.grid(row=3,column=4,padx=5)
btnUpdate=Button(root, text='Update', command=update,width=10)
btnUpdate.grid(row=1,column=5,padx=5)
btnSecurity=Button(root, text='NULL', command=security,width=10)
btnSecurity.grid(row=2,column=5,padx=5)
btnSecurity['state'] = DISABLED


# Table Frame
tree_frame = Frame(root)
tree_frame.place(x=500,y=15,width=450,height=175)

tv=ttk.Treeview(tree_frame,columns=(1,2,3,4))
tv.heading("1", text="ID", anchor='center')
tv.column("1",width=10)
tv.heading("2", text="Application", anchor='center')
tv.column("2",width=100)
tv.heading("3", text="Username", anchor='center')
tv.column("3",width=100)
tv.heading("4", text="Password", anchor='center')
tv.column("4",width=100)
tv['show'] = 'headings'
tv.bind("<ButtonRelease-1>", retrieveData)
tv.pack(fill=X)




displayAll()
root.mainloop()