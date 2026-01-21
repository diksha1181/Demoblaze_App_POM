from Page_Functions.Phone_Functions import PhoneFunctions


class PhoneProcess:

    def __init__(self, phone:PhoneFunctions):
        self.phone = phone

    def run_process(self):
        self.phone.open_home()
        self.phone.open_phones()
        for i in range(1, 6):
            self.phone.open_phone(i)
            self.phone.cart()
            self.phone.verify()
            if i < 5:
                self.phone.back_to_phones()
                
