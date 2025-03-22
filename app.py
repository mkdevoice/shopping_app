import sqlite3
import sys
import pprint
from getpass import getpass
import subprocess

#2__
# Configuraiton section

MAX_ITEM_QTY = 10;


### Functions 
def banner_text(text):
    banner_line_len = len(text) + 12;
    print("\n", end="")
    print("=" * banner_line_len)
    print(f"****  {text} *****")
    print("=" * banner_line_len)

def app_login():
    
    global CurrentUser;
    global nav_stack;

    if CurrentUser is not None and CurrentUser.authenticated:
        render_menu_take_response("core_menu")
        return None;

    username = input("Enter username: ");
    password = getpass("Enter password: ");
    CurrentUser = User(username);

    if(CurrentUser.authenticate_user(password)):
        print(f"""
               Authentication Successful **
              --------------------------------
            ** Welcome {CurrentUser.fullname} !!! **"
        """);
        user_role = CurrentUser.get_user_roles();
        if(user_role is None):
            print("User has no role assigned. Please contact admin.");
            render_menu_take_response("main_menu")
            return None;
        else:
            print("-----------------------------")
            print(f"User role: {user_role}");
            print("-----------------------------\n")
            render_menu_take_response("core_menu")
    else:
        banner_text("Error: Invalid username or password");
        render_menu_take_response("main_menu")
    
    return(None)


def app_exit():
    print("Exit")
    sys.exit(0)

def view_cart():
    perm_key = "view_cart";

    if(not check_permission(perm_key)):
        return(None);

    CurrentUser.cart.print_cart();
    input("Press any key to continue ...")
    return(None);

def add_to_cart():
    perm_key = "add_to_cart";

    if(not check_permission(perm_key)):
        return(None);

    valid_prod_ids = display_all_products();
    prod_id = input("Enter Product Id: ");
    
    prod_id = int(prod_id);
    
    if(prod_id == "#"):
        return(None);
    
    if prod_id not in valid_prod_ids:
        banner_text("Error: Invalid Product ID");
    
    qty = int(input("Enter Quantity: "));
    
    
    if int(qty) < 1 or int(qty) > MAX_ITEM_QTY:
        banner_text(f"Error: Enter Qty within 1 - {MAX_ITEM_QTY}");
        return(None);
    
    CurrentUser.cart.add_item(prod_id, qty);
    banner_text("Product added to cart successfully");

    input("Press any key to continue ...")
    return(None);

def remove_from_cart():
    perm_key = "remove_from_cart";

    if(not check_permission(perm_key)):
        return(None);
    global CurrentUser
    CurrentUser.cart.remove_item();
    input("Press any key to continue ...")
    return(None);

def checkout():
    perm_key = "checkout";

    if(not check_permission(perm_key)):
        return(None);
    
    global CurrentUser; 
    view_cart();
    CurrentUser.cart.checkout();

def check_permission(permission):
    global CurrentUser;

    if not CurrentUser.has_permission(permission):
        banner_text(f"Operation {permission} not permitted for the user role => {CurrentUser.user_role}");
        input("Press any key to continue ...");
        return(False);
    else:
        return(True);


def display_all_products():
    perm_key = "view_product";

    if(not check_permission(perm_key)):
        return(None);

    global Db;
    valid_products = [];
    query = "SELECT product_id, prod_desc, price FROM products;"
    res = Db.db_cur.execute(query);
    products = res.fetchall();
    print("Available Products")
    print("-----------------------------------------------------")
    print("%-4s | %-30s | %-8s" % ("ID", "Product", "Price"))
    print("-----------------------------------------------------")
    for product in products:
        valid_products.append(int(product[0]));
        print(f"{product[0]:<4} | {product[1]:<30s} | {product[2]:<8}");
    print("-----------------------------------------------------")
    print("%-4s | %-30s " % ("0", "Goto Prev Menu"))
    print("-----------------------------------------------------")
    return(valid_products);

def view_all_products():
    display_all_products();
    input("Press any key to continue ...")
    return(None);

def view_product_catalog():   
    perm_key = "view_category";

    if(not check_permission(perm_key)):
        return(None);

    display_all_catalog();
    input("Press any key to continue ...")

def display_all_catalog():
    perm_key = "view_category";

    if(not check_permission(perm_key)):
        return(None);

    global Db;
    
    query = "SELECT * from categories"
    res = Db.db_cur.execute(query);
    catalogs = res.fetchall();
    valid_catalogs = [];

    print("Product Catalog")
    print("%-4s | %-30s" % ("ID", "Catalog"))
    print("-----------------------------------------------------")
    
    for ct in catalogs:
        print(f"{ct[0]:<4} | {ct[1]:<20s}");
        valid_catalogs.append(ct[0]);
    
    print("-----------------------------------------------------")
    print("%-4s | %-30s " % ("#", "Goto Prev Menu"))
    print("-----------------------------------------------------")

    return(valid_catalogs);


def add_new_catalog_item():
    perm_key = "create_category";

    if(not check_permission(perm_key)):
        return(None);

    global Db;

    catalog_name = input("Enter Catalog Name: ");
    catalog_desc = input("Enter Catalog Description: ");
    query = f"INSERT INTO categories (category_name, category_desc) VALUES ('{catalog_name}', '{catalog_desc}');"
    res = Db.db_cur.execute(query);
    Db.dbcon.commit(); 

    banner_text("Catalog added successfully");
    input("Press any key to continue ...")
    return(None);

def remove_from_catalog():
    perm_key = "delete_category";

    if(not check_permission(perm_key)):
        return(None);

    global Db;
    valid_catalogs = display_all_catalog();
    catalog_id = input("Enter Catalog Id: ");
    catalog_id = int(catalog_id);

    if catalog_id == 0:
        return(None);

    if catalog_id not in valid_catalogs:
        banner_text("Error: Invalid Catalog ID");
        return(None);

    query = f"DELETE FROM categories WHERE category_id = {catalog_id};"
    res = Db.db_cur.execute(query);
    Db.dbcon.commit();
    banner_text("Catalog removed successfully");
    input("Press any key to continue ...")
    return(None);
   

def add_product_to_catalog():
    perm_key = "create_product";

    if(not check_permission(perm_key)):
        return(None);

    global Db;
    valid_catalogs = display_all_catalog();
    catalog_id = input("Enter Catalog Id: ");
    catalog_id = int(catalog_id);

    if catalog_id == 0:
        return(None);

    if catalog_id not in valid_catalogs:
        banner_text("Error: Invalid Catalog ID");
        return(None);

    product_name = input("Enter Product Name: ");
    product_desc = input("Enter Product Description: ");
    price = float(input("Enter Price: "));
    query = f"INSERT INTO products (category_id, product_name, prod_desc, price) VALUES ({catalog_id}, '{product_name}', '{product_desc}', {price});"
    res = Db.db_cur.execute(query);
    Db.dbcon.commit();
    banner_text("Product added successfully");
    input("Press any key to continue ...")
    return(None);

def remove_product_from_catalog():
    perm_key = "delete_product";

    if(not check_permission(perm_key)):
        return(None);

    global Db;
    valid_products = display_all_products();
    product_id = input("Enter Product Id: ");
    product_id = int(product_id);

    if product_id == 0:
        return(None);

    if product_id not in valid_products:
        banner_text("Error: Invalid Product ID");
        return(None);

    query = f"DELETE FROM products WHERE product_id = {product_id};"
    res = Db.db_cur.execute(query);
    Db.dbcon.commit();
    banner_text("Product removed successfully");
    input("Press any key to continue ...")
    return(None);


    

def modify_product_in_catalog():
    perm_key = "update_product";

    if(not check_permission(perm_key)):
        return(None);

    global Db;
    valid_products = display_all_products();
    product_id = input("Enter Product Id: ");
    product_id = int(product_id);

    if product_id == 0:
        return(None);

    if product_id not in valid_products:
        banner_text("Error: Invalid Product ID");
        return(None);

    product_name = input("Enter Product Name: ");
    product_desc = input("Enter Product Description: ");
    price = float(input("Enter Price: "));
    query = f"UPDATE products SET product_name = '{product_name}', prod_desc = '{product_desc}', price = {price} WHERE product_id = {product_id};"
    res = Db.db_cur.execute(query);
    Db.dbcon.commit();
    banner_text("Product modified successfully");
    input("Press any key to continue ...")
    return(None);
   

def goto_main_menu():
    display_welcome_banner();
    while True:
        response = render_menu_take_response("main_menu", 1);
        if response == "2":
            break;

def display_welcome_banner():
    print("\n===============================================")
    print("****  Welcome to Demo Marketplace *****")
    print("=================================================");


def render_menu_take_response(menu_name, response_needed = True):
    #print(f"Menu: {menu_name}")
    global nav_stack ;
    
    nav_stack.append(menu_name);

    for key, value in menu_actions[menu_name].items():
        print(f"{key:>4}  : {value[0]:<}")
    if response_needed:
        response = input("Enter your choice: ")
        if response in menu_actions[menu_name]:
            # If user response is a valid option in the menu, then take the second element of the list and call it as function.
            menu_actions[menu_name][response][1]()
        else:
            banner_text("Error: *** Invalid choice ***")
            
    else:
        input("Press any key to continue ...")
        
    render_menu_take_response(nav_stack.pop(), 1);
    
class Dbc:
    def __init__(self, dbfile):
        self.dbfile = dbfile
        self._dbcon = None
        self._dbcur = None
    
    def db_connect(self):
        self._dbcon = sqlite3.connect(self.dbfile);
        self._dbcur = self._dbcon.cursor();
    
    def db_disconnect(self):
        if self._dbcon is not None:
            self._dbcon.close()
    
    @property
    def db_cur(self):
        self._dbcur = self._dbcon.cursor()
        return(self._dbcur);
    
    @property
    def dbcon(self):
        return self._dbcon;
    
    def __del__(self):
        if self._dbcon is not None:
            self._dbcon.close();
      

class User:
    def __init__(self, username):
        self.username = username
        self._authenticated = False
        self.user_role = None;
        self.user_permissions = [];
        self.user_id = None;
        self.fullname = None;
        self.cart = None;
        

    @property
    def authenticated(self):
        return(self._authenticated);
    
    @authenticated.setter
    def authenticated(self, value):
        self._authenticated = value;
    
    def fullname(self):
        return(self.fullname);

    def user_id(self):
        return(self.user_id);

    def user_role(self):
        return(self.user_role);

    def authenticate_user(self, password):
        global Db;

        query = f"SELECT * FROM users WHERE username = '{self.username}' AND password = '{password}' AND active = 1;"
        res = Db._dbcur.execute(query);
        user_data = res.fetchone();
        
        # compare the password. No records will come for invalid password.
        if(user_data is None):
            return False;
        else:
            self.user_id = user_data[0];
            self.fullname = user_data[2];
            self.authenticated = True;
            self.cart = Cart(self.user_id);

            return True    

        
    def get_user_roles(self):
        """Get all the roles allowed for the user username

        Args:
            username (_type_): username of the current logged in user.

        Returns:
            string: get the first available rolename of the user.
        """
        
        global Db
        
        query = f"select u.username, r.role_name from users_roles as ur INNER JOIN users as u ON ur.user_id = u.user_id INNER JOIN  roles as r ON ur.role_id =  r.role_id where u.username = '{self.username}';"
        res = Db.db_cur.execute(query);
        user_roles = res.fetchone();
        if(user_roles is None):
            return None;
        else:
            self.user_role = user_roles[1];
            return(self.user_role)

    def has_permission(self, permission):
        """verify whether the given *username* has permission for the action *permission*.

        Args:
            username (_type_): current logged in user
            permission (_type_): permission string for the action.

        Returns:
            Boolean: Return True if user has permission, False otherwise.
        """
        global Db;

        username = self.username ;
        user_role = self.user_role;

        query = f"select p.permission_name from users_roles as ur INNER JOIN users as u ON ur.user_id = u.user_id INNER JOIN roles as r ON ur.role_id = r.role_id INNER JOIN role_permissions as rp ON r.role_id = rp.role_id INNER JOIN permissions as p ON rp.permission_id = p.permission_id  where u.username = '{username}' AND r.role_name = '{user_role}' ;"
        
        res = Db.db_cur.execute(query);
        user_rights = res.fetchall();
        
    # if user has no rights or user has no role assigned, return False.
        if(user_rights is None):
            return False;
        
        user_rights = [x[0] for x in user_rights];

    # get all rights of the user role.
        
        if permission in user_rights:
            return True;
        else:
            return False;

    
class CartItem:
    def __init__(self, product_id, qty):
        self.product_id = product_id;
        self.qty = qty;

    def get_product_details(self):
        global Db;
        query = f"SELECT product_name, price FROM products WHERE product_id = {self.product_id};"
        res = Db.db_cur.execute(query);
        product_details = res.fetchone();
        return(product_details)

    def total_price(self):
        details = self.get_product_details();
        return float(self.qty * details[1]);

    def print_item(self, index=1):
        details = self.get_product_details();
        print(f"{index:<4} | {details[0]:<12s} | Qt: {self.qty:<5} | Total: {self.qty * details[1]:<8.2f}");
    
    def __repr__(self):
        return f"CartItem({self.product_id}, {self.qty})";
        



class Cart:
    def __init__(self, user_id):
        self.cart_items = [];
        self.user_id = user_id;
    
    
    def add_item(self, product_id, qty):
        self.cart_items.append(CartItem(product_id, qty));
    
    def remove_item(self):
        if(self.is_cart_empty()):
            banner_text("Cart is empty");
            return(None);
    
        self.print_cart();
        item_no = int(input("Item to remove: "));

        if(item_no > 0 and item_no <= len(self.cart_items) ):
            del self.cart_items[item_no - 1]; 
            banner_text("Item removed from cart successfully");
        else:
            banner_text("Error: Invalid item number");
            
        return(None);
    
    def get_cart_items(self):
        return self.cart_items;
    
    def get_cart_total(self):
        return float(sum([x.total_price() for x in self.cart_items]));

    def is_cart_empty(self):
        return not(len(self.cart_items))

    def print_cart(self):
        if(self.is_cart_empty()):
            banner_text("Cart is empty");
            return(None);
    
        print("Cart Items");
        i = 1;
        print("---------------------------------------------------------")
        for item in self.cart_items:
            item.print_item(i);
            i += 1;
        print("---------------------------------------------------------")
        print(f"Total: {self.get_cart_total():.2f}");
    
    def checkout(self):
        global Db;
        query = f"SELECT payment_mode_id, description from payment_modes;"
        res = Db.db_cur.execute(query);
        payment_modes = res.fetchall();
        total_amount = self.get_cart_total();
        valid_pay_modes = [];

        if(self.is_cart_empty()):
            print("** Cart is empty. Add items to Cart to checkout **");
            return(None);

        print("Payment Modes")
        print("----------------------------------------------------------")
        for mode in payment_modes:
            valid_pay_modes.append(mode[0]);
            print(f"{mode[0]:<4} : {mode[1]:<20s}");
        print("----------------------------------------------------------")
        selected_mode = int(input("Enter payment mode: "));
        if selected_mode not in valid_pay_modes:
            print("** Invalid Payment mode. Checkout cancelled **");
            input("Press any key to continue ...")
            return(None);

        pay_mode_desc =  payment_modes[selected_mode-1][1];
        print(f"You will be shortly redirected to the Payment gateway to make the payment of INR {total_amount:.2f} using ** {pay_mode_desc} ** mode...");
        del self.cart_items[:];
        input("Press any key to continue ...")
        return(None);

class App:
    def __init__(self, name):
        self.name = name
        
    
    def run(self):
        display_welcome_banner();
        global nav_stack ;

        while True:
            response = render_menu_take_response("main_menu", 1);
            if response == "2":
                break;


menu_actions = {
    "main_menu" : {
      "1" :  ["Login", app_login],
      "2" :  ["Exit", app_exit]
    },
    "core_menu" : {
       "1" : ["View Cart", view_cart],
       "2" : ["Add to Cart", add_to_cart],
       "3" : ["Remove from Cart", remove_from_cart],
       "4" : ["Checkout", checkout],
       "5" : ["View All Products", view_all_products],
       "6" : ["View All Catalog", view_product_catalog],
       "7" : ["Add new catalog", add_new_catalog_item],
       "8" : ["Remove Catalog", remove_from_catalog],
       "9" : ["Add Product to Catalog", add_product_to_catalog],
       "10": ["Remove Product from Catalog", remove_product_from_catalog],
       "11": ["Modify Product in Catalog", modify_product_in_catalog],
       "0" : [ "Goto Main Menu", goto_main_menu]
    } 
}        

if __name__ == "__main__":
    app = App("Mickoo");
    dbfile =  './mickoo.db'
    Db = Dbc(dbfile);
    Db.db_connect();
    nav_stack = [];
    CurrentUser = None;

    app.run();
    Db.db_disconnect();
    del Db;
    print("Good Bye !!!")
    sys.exit(0)
