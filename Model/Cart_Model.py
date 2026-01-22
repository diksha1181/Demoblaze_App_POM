from pydantic import BaseModel
  
class CartData(BaseModel):
    name : str
    country : str
    city : str  
    credit_card : str
    month : int
    year : int

class CartDetailsModel(BaseModel):
    CartData: CartData