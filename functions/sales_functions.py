from database.db_connect import connect_db
conn=connect_db()
cursor=conn.cursor()

def load_coupouns():
    coupoun_codes={}
    coupouns=cursor.execute("SELECT* FROM coupoun_codes_DB")
    c=coupouns.fetchall()
    for x in c:
        coupoun_codes.update({x["code"]:x["discount"]})
    return coupoun_codes

def load_menu_categories():
    menu_categories={}
    categories=cursor.execute("SELECT* FROM MENU_CATEGORIES_DB")
    c=categories.fetchall()
    for x in c:
        menu_categories.update({x["cat_code"]:x["cat_name"]})
    return menu_categories


def category_menu_codes(code):
    items=cursor.execute("SELECT code FROM menu_db WHERE cat_code=?",(code,))
    return [item["code"] for item in items]



def Display_menu(code):
    cursor.execute("SELECT* FROM menu_db WHERE cat_code=?",(code,))
    items=cursor.fetchall()
    full_menu=[]
    print("  CODE       ITEM          Price \n ________________________________ ")
    for item in items:
        row=f"  {item["code"]}      {item["name"]}      {item["price"]}"
        print(row)
        full_menu.append(row)
    print("\n~ All prices are exlusive of VAT")
    cursor.execute("SELECT cat_name FROM MENU_CATEGORIES_DB WHERE cat_code=?",(code,))
    chosen_category=cursor.fetchone()["cat_name"]
    return chosen_category,full_menu

def choice_menu_loop():
    text=f"""Please select the number to explore our menu: \n
                1 - Signature Items
                2 - BBQ Items
                3 - Breakfast
                4 - Desserts
                5 - Tandoor
                -------------
                6 - Cart Actions ~ View | Edit | Proceed to Payment

                ~  Type 'Exit' at any Stage to Cancel your order
                """
    print(text)
    choice=input("Enter >>> ")
    return choice #retuns user input to main loop


class Cart: #cart object
    def __init__(self):
        self.cart_items={} #initial variables for every cart 
        self.vat_rate=0.05


    def add_items_tocart(self,code):
        cursor.execute("SELECT name,price FROM menu_db WHERE code=?",(code,))
        item=cursor.fetchone()
        item_name,item_price=item
        if item_name:
            self.cart_items.update({code:{"Name":item_name,"Price":item_price}}) #name and price fetched from item code dict and updated in cart
            print(f"\n {item_name} ADDED | CART TOTAL :{self.CalcTotals()[0]} \n ") 


                        
    def get_cart_items(self): #user can view current cart items and total
        for code in self.cart_items: #every loop is one item code in the cart
            item_n_price=self.cart_items[code] #dict of the item code containing name and price
            print(f"   {code}    {item_n_price["Name"]} ¦ {item_n_price["Price"]} DHS\n")
        return f"CART TOTAL {self.CalcTotals()[0]} " #total returned only if called with a variable in main code



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
            print(f"{removed["Name"]} REMOVED | CART TOTAL : {self.CalcTotals()[0]}\n")
        except KeyError: #error handling incase user enters code not in cart. 
            pass #errroe messAGE given in main loop
        
    def checkout(self):
        coupoun_codes=load_coupouns()
        coupoun_discount=0  # for initializing 
        while True:
            coupoun_ask=input("Please enter valid coupoun codes to avail discounts, enter 'N' to skip")
            if coupoun_ask.lower()=='n': #no coupoun
                 break
            elif coupoun_ask in coupoun_codes.keys(): #valid coupoun
                coupoun_discount=coupoun_codes[coupoun_ask]
                print(f"COUPOUN CODE '{coupoun_ask}' APPLIED | {coupoun_discount}% DISCOUNT !! ")

            else:
                print("Invalid Code, Type 'N' to skip discount or enter a valid code:")
                continue
            break
                 
        cart_total,net_total,net_afterVAT=self.CalcTotals(coupoun_discount)


        print(f"                                YOUR RECIPT")
        print("                            _____________________\n")
        self.get_cart_items()

        print(f"""
SUBTOTAL :    {cart_total} 
Discount ({coupoun_discount}%)     -{(coupoun_discount/100)*cart_total}
NET AFTER DISCOUNT    {net_total}
VAT (5%)    {0.05*net_total:.2f}
GRAND TOTAL    {net_afterVAT:.2f}
Payment Method: Cash
~ All prices are exlusive of VAT
Thank You for Dining with Us !
""")
                       
            


