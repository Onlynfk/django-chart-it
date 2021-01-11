from messages import Messages



class Auth():
    def check():
        """
        Check credentials then login the user, 
        """
        atm_number = input("Type in your Atm number: ")
        password = input("Type in your password : ")
        # month, day, cvv
        if isinstance(atm_number, int) and isinstance(password, int):
            details = Messages.login_success()
            return details
        else: 
            return Messages.login_unsuccessful()





