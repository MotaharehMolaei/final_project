from tkinter import *
from tkinter import ttk




#----------------Window------------------
window = Tk()
window.geometry("1200x450")
window.title("Enroll View")
window.title("Enrollment Management")

#Labels
Label(window, text="ID").place(x=20, y=20)
Label(window, text="Name").place(x=20, y=60)
Label(window, text="family").place(x=20, y=100)
Label(window, text="Phone Nr.").place(x=20, y=140)
Label(window, text="Enroll Date").place(x=20, y=180)
Label(window, text="Class").place(x=20, y=220)
Label(window, text="Level").place(x=20, y=260)
Label(window, text="Teacher").place(x=20, y=300)

#Variables
id = IntVar()
name = StringVar()
family = StringVar()
phone_number = StringVar()
enroll_date = StringVar()
class_name = StringVar()
Level = StringVar()
teacher = StringVar()

#Entries
Entry(window, textvariable=id).place(x=130, y=20)
Entry(window, textvariable=name).place(x=130, y=60)
Entry(window, textvariable=family).place(x=130, y=100)
Entry(window, textvariable=phone_number).place(x=130, y=140)
Entry(window, textvariable=enroll_date).place(x=130, y=180)

class_box = ttk.Combobox(window, textvariable=class_name, values=("English", "German", "Korean", "French", "Italian", "Chinese"))
class_box.place(x=130, y=220)

class_box = ttk.Combobox(window, textvariable=class_name, values=("A1", "A2", "B1", "B2", "C1", "C2"))
class_box.place(x=130, y=260)

Entry(window, textvariable=teacher).place(x=130, y=300)

#Buttons
Button(window, text="Save", width=18).place(x=50, y=350)
Button(window, text="Edit", width=18).place(x=50, y=380)
Button(window, text="Remove", width=18).place(x=50, y=410)

#Table
table = ttk.Treeview(window, height=21, columns=["ID", "Name", "Family", "Phone Number", "Enroll Date", "Class", "Level", "Teacher"], show="headings")

table.column("ID", width=50)
table.column("Name", width=120)
table.column("Family", width=120)
table.column("Phone Number", width=140)
table.column("Enroll Date", width=120)
table.column("Class", width=100)
table.column("Level", width=60)
table.column("Teacher", width=120)

table.heading("ID", text="ID")
table.heading("Name", text="Name")
table.heading("Family", text="Family")
table.heading("Phone Number", text="Phone Number")
table.heading("Enroll Date", text="Enroll Date")
table.heading("Class", text="Class")
table.heading("Level", text="Level")
table.heading("Teacher", text="Teacher")

table.place(x=350, y=20)
window.mainloop()
