from tkinter import *
from os.path import join
import password_configs
import getpass

master = Tk()
master.iconbitmap(r'C:icon\pass.ico')
master.configure(background="#cfcfcf")
master.title("Password Generator")
master.resizable(0, 0)


def execute():
    if sc.get() == 1:
        password_configs.with_sc(c)
        from password_configs import p
        output.insert(END, p)
    else:
        password_configs.without_sc(c)
        from password_configs import p
        output.insert(END, p)
    if txt.get() == 1:
        user = getpass.getuser()
        path = r"C:\\Users\\"+str(user)+"\Desktop"
        w1 = a.get()
        u1 = b.get()
        file_create = open(join(path, str(w1))+".txt", 'w')
        file_create.write("Username/Email: " + str(u1))
        file_create.write("\nPassword: " + p)


def done():
    master.destroy()


Label(master, text='Name of Website/Service', background="#cfcfcf").grid(row=2, column=0)
Label(master, text='Username/Email Address', background="#cfcfcf").grid(row=4, column=0)
Label(master, text='Password Length', background="#cfcfcf").grid(row=5, column=0)
Label(master, text='Password Appears Here --> ', background="#cfcfcf").grid(row=8, column=0)
Label(master, text='Created by Howard F.', background="#cfcfcf").grid(row=12, column=0)
a = StringVar()
b = StringVar()
WebName = Entry(master, textvariable=a, background="#cfcfcf").grid(row=2, column=1)
Username = Entry(master, textvariable=b, background="#cfcfcf").grid(row=4, column=1)
a.set(" ")
b.set(" ")
sc = IntVar()
txt = IntVar()
Checkbutton(master, text='Special Characters', variable=sc, offvalue=0, background="#cfcfcf").grid(row=6, column=0)
Checkbutton(master, text='Save as text file(On Desktop)', variable=txt, offvalue=0, background="#cfcfcf").grid(row=6, column=1)
c = IntVar()
p1 = Spinbox(master, from_=8, to=20, textvariable=c, background="#cfcfcf").grid(row=5, column=1)
c.set(8)
submit = Button(master, text="Generate", width=10, command=execute, background="#cfcfcf").grid(row=10, column=3, padx=1, pady=1)
cancel = Button(master, text="Exit", width=10, command=done, background="#cfcfcf").grid(row=12, column=3, padx=1, pady=1)
output = Text(master, height=3, width=15, background="#cfcfcf")
output.grid(row=8, column=1)
output.insert(END, "")
mainloop()
