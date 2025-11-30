import re
from datetime import datetime

def name_validator(name):
    if not re.match(r"^[a-zA-Z\s]{3,30}$", name):
        raise NameError("Invalid name!")

def brand_validator(brand):
    if not re.match(r"^[a-zA-Z\s]{3,30}$", brand):
        raise NameError("Invalid brand!")

def quantity_validator(quantity):
    if not (type(quantity) == int and quantity > 0):
        raise NameError("Invalid quantity!")

def price_validator(price):
    if not (type(price) == float and price > 0):
        raise NameError("Invalid price!")

def expiration_date_validator(expire_date):
    if not expire_date >= datetime.today().date():
        raise NameError("Invalid expiration date!")




def create_product_and_validate(id, name, brand,quantity, price, expiration_date):
    name_validator(name)
    brand_validator(brand)
    quantity_validator(quantity)
    price_validator(price)
    exp_date = datetime.strptime(expiration_date, "%Y-%m-%d").date()
    expiration_date_validator(exp_date)

    product = {
        "id": id,
        "name": name,
        "brand": brand,
        "quantity": quantity,
        "price": price,
        "expiration_date": exp_date
    }
    return product


def calculate_total(product_list):
    """Calculate the total price of all products."""
    if not product_list:
        raise ValueError("No Products", "No products available.")

    total = 0
    for product in product_list:
        total += product["quantity"] * product["price"]

    return total



