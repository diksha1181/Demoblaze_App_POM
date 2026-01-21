from Page_Functions.Laptop_Functions import LaptopFunctions


class LaptopProcess:

    def __init__(self, laptop:LaptopFunctions):
        self.laptop = laptop

    def run_process(self):
        self.laptop.open_laptops()
        self.laptop.open_laptop1()
        self.laptop.cart()
        self.laptop.verify()
