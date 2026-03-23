from database.db_connect import connect_db




def Display_menu(code):
    conn=connect_db()
    cursor=conn.cursor()
    cursor.execute("SELECT* FROM menu_db WHERE cat_code=?",(code,))
    items=cursor.fetchall()
    print("  CODE       ITEM          Price \n ________________________________ ")
    for item in items:
        row=print(f"  {item["code"]}      {item["name"]}      {item["price"]}")
    print("\n~ All prices are exlusive of VAT")
    cursor.execute("SELECT cat_name FROM MENU_CATEGORIES_DB WHERE cat_code=?",(code,))
    chosen_category=cursor.fetchone()["cat_name"]
    return chosen_category

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
        conn=connect_db()
        cursor=conn.cursor()
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
        



      
