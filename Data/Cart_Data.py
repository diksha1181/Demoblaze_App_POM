import os
import dotenv
from faker import Faker
from Model.Cart_Model import CartData, CartDetailsModel

class CartPageMother:

    def __init__(self):
        dotenv.load_dotenv()
        self.fake = Faker()
        self.name = self.fake.name()
        self.country = self.fake.country()
        self.city = self.fake.city()
        self.credit_card = self.fake.credit_card_number()
        self.month = int(self.fake.month())
        self.year = int(self.fake.year())

    def get(self) -> CartDetailsModel:
        return CartDetailsModel(
            CartData = CartData(
                name=self.name,
                country=self.country,
                city=self.city,
                credit_card=self.credit_card,
                month=self.month,
                year=self.year
            )
        )


