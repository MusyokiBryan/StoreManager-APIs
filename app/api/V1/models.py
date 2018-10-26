from werkzeug.security import generate_password_hash, check_password_hash


class Products:
    """Functionality of products"""

    products = {}

    def get_all_products(self):
        """"
        get all products
        """
        if self.products == {}:
            return {"txt": "No products found"}
        return self.products

    def get_a_product(self, product_id):
        if product_id not in self.products:
            return {"txt": "product not found"}
        if self.products == {}:
            return {"txt": " Product not found"}
        return self.products[product_id]

    def create_product(self, product_name, quantity, product_price):
        if isinstance(quantity, int):
            return {"txt": "try again"}
        if product_name == "":
            return {"txt": "product name must be provided"}
        if product_price == "" or product_price is None:
            return {"txt": "price value must be provided"}
        if quantity in self.products is not int:
            return {"txt": "dfishosidsoia"}
        new_id = len(self.products) + 1
        self.products[new_id] = {"product_name": product_name, "quantity": quantity,
                                 "product_price": product_price, }
        res = self.products[new_id]
        return {"msg": "Product added successfully", "data": res}

    def edit_product(self, product_id, product_name, product_price):
        self.products[product_id] = {"product_id": product_id, "product_name": product_name,
                                     "product_price": product_price}
        return {"msg": "Sale Edited"}

    def delete_a_product(self, product_id):
        if product_id not in self.products:
            return {"txt": "product not found"}
        del self.products[product_id]
        return {"txt": "product Deleted"}


class Sales:
    """Functionality of sales"""
    sales = {}

    def see_sales(self):
        if self.sales == {}:
            return {"txt": "No sales added."}
        return self.sales

    def get_a_sale(self, sale_id):
        if self.sales == {} or sale_id not in self.sales:
            return {"txt": "Sale not found."}
        return self.sales[sale_id]

    def post_a_sale(self, sale_name, number, sell_price):
        new_id = len(self.sales) + 1
        self.sales[new_id] = {"sale_name": sale_name, "number": number,
                              "sell_price": sell_price}
        return {"msg": "added successfully"}

    def edit_sale(self, sale_id, sale_name, number, sell_price):
        if self.sales == {} or sale_id not in self.sales:
            return {"txt": "Sale not found."}
        self.sales[sale_id] = {"sale_name": sale_name, "number": number, "sell_price": sell_price}
        return {"msg": "Sale Edited"}

    def delete_a_sale(self, sale_id):
        if sale_id not in self.sales:
            return {"txt": "sale not found"}
        del self.sales[sale_id]
        return {"txt": "sale Deleted"}


class Users:
    users = {"kratos": {"email": "kratso@something.com", "password": generate_password_hash("olympus"), "admin": True}}

    def register_user(self, user_name, email, password):
        hidden = generate_password_hash(password=password)
        self.users[user_name] = {"email": email, "password": hidden}
        res = self.users[user_name]
        return {"msg": "user added successfully", "data": res}

    def login(self, user_name, password):
        if user_name in self.users:
            if check_password_hash(self.users[user_name]["password"], password=password):
                print("Logged In")
                return {"txt": "Successfully logged In"}
            else:
                print("Invalid Password")
                return {"txt": "Invalid Password"}
        else:
            print("Invalid Username")
            return {"txt": "Invalid Username"}

    def get_users(self):
        if self.users == {}:
            return {"txt": "No sales added."}
        return self.users

    def delete_a_user(self, user_name):
        del self.users[user_name]
        return {"txt": "user Deleted"}
