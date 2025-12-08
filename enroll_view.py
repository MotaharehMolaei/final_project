from tkinter import *
from tkinter import ttk
from tkinter import messagebox
from enroll_controller import EnrollController


def reset():
    id.set(0)
    name.set("")
    family.set("")
    phone_number.set("")
    enroll_date.set("")
    class_name.set("")
    level.set("")
    teacher.set("")

    status, enroll_list = EnrollController.find_all()

    for row in table.get_children():
        table.delete(row)

    if status:
        for enroll in enroll_list:
            table.insert("", END, values=enroll)
    else:
        messagebox.showerror("Error", enroll_list)


def select_enroll(event):
    enroll = table.item(table.focus())["values"]
    if enroll:
        id.set(enroll[0])
        name.set(enroll[1])
        family.set(enroll[2])
        phone_number.set(enroll[3])
        enroll_date.set(enroll[4])
        class_name.set(enroll[5])
        level.set(enroll[6])
        teacher.set(enroll[7])


def save_click():
    status, message = EnrollController.save(
        id.get(),
        name.get(),
        family.get(),
        phone_number.get(),
        enroll_date.get(),
        class_name.get(),
        level.get(),
        teacher.get()
    )

    if status:
        reset()
        messagebox.showinfo("Save", "Enrollment saved successfully")
    else:
        messagebox.showerror("Error", message)


def edit_click():
    status, message = EnrollController.edit(
        id.get(),
        name.get(),
        family.get(),
        phone_number.get(),
        enroll_date.get(),
        class_name.get(),
        level.get(),
        teacher.get()
    )

    if status:
        reset()
        messagebox.showinfo("Edit", "Enrollment edited successfully")
    else:
        messagebox.showerror("Error", message)


def remove_click():
    status, message = EnrollController.remove(id.get())

    if status:
        reset()
        messagebox.showinfo("Remove", "Enrollment removed successfully")
    else:
        messagebox.showerror("Error", message)


# ---------------- GUI --------------------

window = Tk()
window.geometry("1200x450")
window.title("Enrollment Management")

Label(window, text="ID").place(x=20, y=20)
Label(window, text="Name").place(x=20, y=60)
Label(window, text="Family").place(x=20, y=100)
Label(window, text="Phone Nr.").place(x=20, y=140)
Label(window, text="Enroll Date\n YYYY-MM-DD").place(x=20, y=180)
Label(window, text="Class").place(x=20, y=220)
Label(window, text="Level").place(x=20, y=260)
Label(window, text="Teacher").place(x=20, y=300)

id = IntVar()
name = StringVar()
family = StringVar()
phone_number = StringVar()
enroll_date = StringVar()
class_name = StringVar()
level = StringVar()
teacher = StringVar()

Entry(window, textvariable=id).place(x=130, y=20)
Entry(window, textvariable=name).place(x=130, y=60)
Entry(window, textvariable=family).place(x=130, y=100)
Entry(window, textvariable=phone_number).place(x=130, y=140)
Entry(window, textvariable=enroll_date).place(x=130, y=180)

ttk.Combobox(window, textvariable=class_name,
             values=("English", "German", "Korean", "French", "Italian", "Chinese")).place(x=130, y=220)

ttk.Combobox(window, textvariable=level,
             values=("A1", "A2", "B1", "B2", "C1", "C2")).place(x=130, y=260)

Entry(window, textvariable=teacher).place(x=130, y=300)

Button(window, text="Save", width=18, command=save_click).place(x=50, y=350)
Button(window, text="Edit", width=18, command=edit_click).place(x=50, y=380)
Button(window, text="Remove", width=18, command=remove_click).place(x=50, y=410)

table = ttk.Treeview(
    window,
    height=21,
    columns=["ID", "Name", "Family", "Phone Number", "Enroll Date", "Class", "Level", "Teacher"],
    show="headings"
)

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
table.bind("<<TreeviewSelect>>", select_enroll)

reset()
window.mainloop()
