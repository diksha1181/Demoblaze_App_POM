from Libraries.libraries import Import_libraries
from Data.Config_Data import ConfigData
from Page_Functions.Login_Functions import LoginFunctions
from Page_Functions.Signup_Functions import SignupFunctions
from Page_Functions.Laptop_Functions import LaptopFunctions
from Page_Functions.Phone_Functions import PhoneFunctions
from Page_Functions.Monitor_Functions import MonitorFunctions
from Page_Functions.Cart_Functions import CartFunctions
from Page_Functions.Logout_Functions import LogoutFunctions



from Page_Processes.Login_Processes import LoginProcess
from Page_Processes.Signup_Processes import SignupProcess
from Page_Processes.Laptop_Processes import LaptopProcess
from Page_Processes.Phone_Processes import PhoneProcess
from Page_Processes.Monitor_Processes import MonitorProcess
from Page_Processes.Cart_Processes import CartProcess
from Page_Processes.Logout_Pocesses import LogoutProcess



data = ConfigData()
driver = Import_libraries.get_driver()
driver.get(data.BASE_URL)


signup_functions = SignupFunctions(driver)
login_Functions = LoginFunctions(driver)
laptop_functions = LaptopFunctions(driver)
phone_functions = PhoneFunctions(driver)
monitor_functions = MonitorFunctions(driver)
cart_functions = CartFunctions(driver)
logout_functions = LogoutFunctions(driver)





def test_signup():
    signup = SignupProcess(signup_functions)
    signup.run_process()

def test_login():
    login = LoginProcess(login_Functions)
    login.run_process()

def test_laptop():
    laptop = LaptopProcess(laptop_functions)
    laptop.run_process()

def test_phone():
    phone = PhoneProcess(phone_functions)
    phone.run_process()

def test_monitor():
    monitor = MonitorProcess(monitor_functions)
    monitor.run_process()

def test_cart():
    cart = CartProcess(cart_functions)
    cart.run_process()

def test_logout():
    logout = LogoutProcess( logout_functions)
    logout.run_process()
    
def test_driver_close():
    driver.close()


