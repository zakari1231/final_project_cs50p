
def check_if_user_login(func1,login):
    def warrper_function():
        if func1 == True:
            print('you are alredy loggedin')
        else:
            return login()
        pass
    return warrper_function