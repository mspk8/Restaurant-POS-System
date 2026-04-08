from fastapi import FastAPI 
from functions.sales_functions import *
from pydantic import BaseModel,field_validator
from typing import Optional
app = FastAPI()
cart = Cart()

class OrderItem(BaseModel):
    item_code:str
    quantity:int=1

class CheckoutRequest(BaseModel):   
    coupon: Optional[str]=''
    payment_method:str='cash'

    @field_validator("payment_method")
    def payment_method_validator(cls,v):
        allowed=["cash",'card','online']
        if v not in allowed:
            raise ValueError(f"Payment method must be one of {allowed}")
        return v


@app.get("/menu")
def get_menu_categories():
    categories=load_menu_categories()
    return categories

@app.get("/menu/{category_code}")
def get_menu(category_code: str):
    items = Display_menu(category_code)
    return {"category and items": items}  

@app.post("/cart/add/{item_code}")
def add_item(item_code: str):
    item=cart.add_items_tocart(item_code)
    return item,cart.get_cart_items()


@app.delete("/cart/remove/{item_code}")
def delete_item(item_code:str):
    cart.Remove_item(item_code)
    return cart.get_cart_items()


@app.get("/cart")
def view_cart():
    return cart.cart_items

@app.post("/cart/checkout")
def checkout(request:CheckoutRequest):
    coupon_codes=load_coupons()
    coupon_discount=0  # for initializing 
    if request.coupon and request.coupon in coupon_codes.keys():
        coupon_discount=coupon_codes[request.coupon]
        message=f"coupon CODE '{request.coupon}' APPLIED | {coupon_discount}% DISCOUNT !! "

    cart_total,net_total,net_afterVAT=cart.CalcTotals(coupon_discount)
    print(f"                                YOUR RECIPT")
    print("                            _____________________\n")
    cart.get_cart_items()
    return {
            "SUBTOTAL" : cart_total,
            "Discount": (coupon_discount/100)*cart_total,
            "NET FTER DISCOUNT  ":  net_total,
            "VAT"  : round(0.05*net_total,2),
            "GRAND TOTAL"  :  round(net_afterVAT,2),
            "Payment Method": request.payment_method,
            "message":"~ All prices are exlusive of VAT, \nThank You for Dining with Us !"
    }
        
            
            
                    
        


