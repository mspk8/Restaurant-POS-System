class POSError(Exception):
    pass

class ItemNotFoundError(POSError):
    def __init__(self, code):
        self.code=code
        super().__init__(f"ITEM Code :{code} not found in Menu")

class ItemNotInCartError(POSError):
    def __init__(self, code):
        self.code=code
        super().__init__(f"ITEM CODE: {code} not found in Cart")


class EmptyCart(POSError):
    def __init__(self):
        super().__init__("Cart Is empty, Add some Items to Proceed to Checkout")

class InvalidCouponError(POSError):
    def __init__(self, code):
        self.code=code
        super().__init__(f"COUPON CODE : {code} IS INVALID")

class InvalidPaymentMethod(POSError):
    def __init__(self, method):
        self.method=method
        super().__init__(f"Payment Method : {method} is Invalid")
        
class DataBaseError(POSError):
    def __init__(self, detail):
        self.detail=detail
        super().__init__(f"Database Error : {detail}")