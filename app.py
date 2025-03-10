
#2__

class App:
    def __init__(self, name):
        self.name = name

    def run(self):
        print(f"Running {self.name}");


Documentation = """"
category class
category manager
   create, read, update, delete, list_display
product
product manager
  create, read, update, delete,  list_display
users
users manager
  create, read, update, delete, list_users
cart
  create, read, update, add, remove, list_display
"""

class category_manager:
    def __init__(self):
        self.name = name

    def create(self):
        print(f"Creating {self.name} category");

    def read(self):
        print(f"Reading {self.name} category");

    def update(self):
        print(f"Updating {self.name} category");

    def delete(self):
        print(f"Deleting {self.name} category");

    def list_display(self):
        print(f"Listing {self.name} category");

class category:
    def __init__(self, name, description):
        self.name = name
        self.description = description

class product_manager:
    def __init__(self):
        self.name = name

    def create(self):
        print(f"Creating {self.name} product");

    def read(self):
        print(f"Reading {self.name} product");

    def update(self):
        print(f"Updating {self.name} product");

    def delete(self):
        print(f"Deleting {self.name} product");

    def list_display(self):
        print(f"Listing {self.name} product");

class product:
    def __init__(self, prod_id, category_id, name, price):
        self.id = prod_id   
        self.category_id = category_id
        self.name = name
        self.price = price
        
    


