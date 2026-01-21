from Page_Functions.Cart_Functions import CartFunctions


class CartProcess:

    def __init__(self, cart:CartFunctions):
        self.cart = cart

    def run_process(self):
        self.cart.open_cart()
        self.cart.place_order()
        self.cart.form_visibility()
        self.cart.enter_name()
        self.cart.enter_country()
        self.cart.enter_city()
        self.cart.enter_card()
        self.cart.enter_month()
        self.cart.enter_year()
        self.cart.click_purchase()
        self.cart.verify_successful_purchase()
        