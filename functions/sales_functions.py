from database.db_connect import connect_db




def get_menu_categories():
    conn = connect_db()
    cursor = conn.cursor()
    cursor.execute("SELECT cat_code, cat_name FROM MENU_CATEGORIES_DB ORDER BY cat_code")
    categories = {row["cat_code"]: row["cat_name"] for row in cursor.fetchall()}
    conn.close()
    return categories


def Display_menu(code):
    conn = connect_db()
    cursor = conn.cursor()
    cursor.execute("SELECT code, name, price FROM menu_db WHERE cat_code=? ORDER BY code", (code,))
    items = cursor.fetchall()

    if not items:
        conn.close()
        print("No items found in this category.")
        return None

    print("  CODE       ITEM                    PRICE")
    print(" __________________________________________")
    for item in items:
        print(f"  {item['code']:<8} {item['name']:<22} {item['price']:.2f}")
    print("\n~ All prices are exclusive of VAT")

    cursor.execute("SELECT cat_name FROM MENU_CATEGORIES_DB WHERE cat_code=?", (code,))
    category_row = cursor.fetchone()
    conn.close()
    return category_row["cat_name"] if category_row else None


def choice_menu_loop(menu_categories):
    print("Please select the number to explore our menu:\n")
    for cat_code, cat_name in menu_categories.items():
        print(f"                {cat_code} - {cat_name}")

    cart_option = len(menu_categories) + 1
    print("                -------------")
    print(f"                {cart_option} - Cart Actions ~ View | Edit | Proceed to Payment")
    print("\n                ~ Type 'Exit' at any stage to cancel your order")
    return input("\nEnter >>> ")


class Cart: #cart object
    def __init__(self):
        self.cart_items={} #initial variables for every cart
        self.vat_rate=0.05


    def add_items_tocart(self,code):
        conn=connect_db()
        cursor=conn.cursor()
        cursor.execute("SELECT name,price FROM menu_db WHERE code=?",(code,))
        item=cursor.fetchone()
        conn.close()

        if not item:
            return False

        item_name=item["name"]
        item_price=item["price"]
        self.cart_items.update({code:{"Name":item_name,"Price":item_price}})
        print(f"\n{item_name} ADDED | CART TOTAL : {self.CalcTotals()[0]:.2f}\n")
        return True


                        
    def get_cart_items(self): #user can view current cart items and total
        if not self.cart_items:
            print("Your cart is empty.")
            return "CART TOTAL 0.00"

        for code in self.cart_items: #every loop is one item code in the cart
            item_n_price=self.cart_items[code] #dict of the item code containing name and price
            print(f"   {code}    {item_n_price['Name']} | {item_n_price['Price']:.2f} DHS\n")
        return f"CART TOTAL {self.CalcTotals()[0]:.2f}"



    def CalcTotals(self,discount=0): #dicount is 0 if no argument given when calling.
        cart_total=0
        net_total=0
        for item in self.cart_items: #every loop is one item code dict
            item=self.cart_items[item]["Price"] #fetches price value from item code dict
            cart_total+=item #totalling
        net_total=cart_total-(cart_total*(discount/100))
        net_afterVAT=net_total*(1+self.vat_rate)
        return cart_total,net_total,net_afterVAT 

    
    def Remove_item(self,code):
        try:
            removed=self.cart_items.pop(code) #removes item dictionary from cart
            print(f"{removed['Name']} REMOVED | CART TOTAL : {self.CalcTotals()[0]:.2f}\n")
            return True
        except KeyError: #error handling incase user enters code not in cart. 
            return False
        



      
