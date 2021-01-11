from messages import Messages
from seek import Seek




class Auth():
    def check():
        """
        Check credentials then login the user, 
        """
        atm_number = input("Type in your Atm number: ")
        password = input("Type in your password : ")
        if atm_number.isdigit() == True and password.isdigit() == True:
            print( Messages.login_success())
            Seek.find()
        else:
            return Messages.login_unsuccessful()
            





