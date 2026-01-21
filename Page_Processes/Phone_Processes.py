from Page_Functions.Phone_Functions import PhoneFunctions


class PhoneProcess:

    def __init__(self, phone:PhoneFunctions):
        self.phone = phone

    def run_process(self):
        self.phone.open_home()
        self.phone.open_phones()
        self.phone.open_phone1()
        self.phone.cart()
        self.phone.verify()
