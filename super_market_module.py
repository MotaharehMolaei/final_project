import re
from datetime import datetime

class Product:
    def __init__(self, name, brand, quantity, price, expire_date):
        self.name = name
        self.brand = brand
        self.quantity = quantity
        self.price = price
        self.expire_date = expire_date

    def validation(self):
        if not re.match(r"^[a-zA-Z\s]{3,30}$", self.name):
            raise NameError("Invalid name!")

        if not re.match(r"^[a-zA-Z\s]{3,30}$", self.brand):
            raise NameError("Invalid brand!")

        if not (type(self.quantity) == int and self.quantity > 0):
            raise NameError("Invalid quantity!")

        if not (type(self.price) == float and self.price > 0):
            raise NameError("Invalid price!")

        if not self.expire_date >= datetime.today().date():
             raise NameError("Invalid expiration date!")

    def save(self):
        print("Saving product...", self.name, self.brand, self.quantity, self.price, self.expire_date)


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



