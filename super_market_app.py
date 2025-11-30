from tkinter import *
from tkinter import messagebox
from super_market_module import *
from datetime import datetime, date
from tkinter import ttk
from persiantools.digits import to_word

product_list = []


def reset_form():
    id.set(len(product_list) + 1)
    name.set("")
    brand.set("")
    quantity.set(0)
    price.set(0.0)
    expire_date.set(str(date.today()))


def save():
    try:
        product = create_product_and_validate(id.get(), name.get(), brand.get(), quantity.get(), price.get(),
                                              expire_date.get())
        product_list.append(product)
        table.insert("", END, values=tuple(product.values()))
        reset_form()
        messagebox.showinfo("Saved", "Product saved successfully!")
    except Exception as e:
        messagebox.showerror("Save Error", f"Error: {e}")


def total_price():
    try:
        total = calculate_total(product_list)
        messagebox.showinfo("Total Price", f"Total value of all products: {total}\n {to_word(total)} تومان ")
    except Exception as e:
        messagebox.showinfo("Error", f"Error: {e}")


window = Tk()
window.title("Supermarket App")
window.geometry("820x370")
# window.config(background="blue")

# id
Label(window, text="Id").place(x=30, y=30)
id = IntVar()
Entry(window, textvariable=id, state="readonly").place(x=150, y=30)

# name
Label(window, text="Name").place(x=30, y=70)
name = StringVar()
Entry(window, textvariable=name).place(x=150, y=70)

# brand
Label(window, text="Brand").place(x=30, y=110)
brand = StringVar()
Entry(window, textvariable=brand).place(x=150, y=110)

# quantity
Label(window, text="Quantity").place(x=30, y=150)
quantity = IntVar()
Entry(window, textvariable=quantity).place(x=150, y=150)

# price
Label(window, text="Price").place(x=30, y=190)
price = DoubleVar()
Entry(window, textvariable=price).place(x=150, y=190)

# date
Label(window, text="Expiration Date\n YYYY-MM-DD").place(x=30, y=230)
expire_date = StringVar()
Entry(window, textvariable=expire_date).place(x=150, y=230)

Button(window, text="Save", command=save).place(x=30, y=310, width=100)
Button(window, text="Total", command=total_price).place(x=175, y=310, width=100)

table = ttk.Treeview(window, columns=(1, 2, 3, 4, 5, 6), height=14, show="headings")

table.heading(1, text="Id")
table.heading(2, text="Name")
table.heading(3, text="Brand")
table.heading(4, text="Quantity")
table.heading(5, text="Price")
table.heading(6, text="Expiration Date")

table.column(1, width=60)
table.column(2, width=100)
table.column(3, width=100)
table.column(4, width=60)
table.column(5, width=60)
table.column(6, width=100)

table.place(x=310, y=30)

reset_form()
window.mainloop()